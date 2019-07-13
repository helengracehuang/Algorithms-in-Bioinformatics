from os.path import join
import sys
import time
from collections import defaultdict, Counter, OrderedDict
import sys
import os
import zipfile
sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../.."))
from CM122_starter_code.helpers import read_reads

# Graph storing
# adjacency matrix (for every pair of nodes, store a connection)
# adjacency lists (for each node, store an adjacency list) -> what we use

def read_assembly_reads(read_fn):
    reads = read_reads(read_fn)
    output_reads = [_[0] for _ in reads]
    for _ in range(len(reads)):
        output_reads.append(reads[_][1]) # take both ends
    return output_reads


def simple_de_bruijn(sequence_reads, k):
    """
    Creates A simple DeBruijn Graph with nodes that correspond to k-mers of size k.
    :param sequence_reads: A list of reads from the genome
    :param k: The length of the k-mers that are used as nodes of the DeBruijn graph
    :return: A DeBruijn graph where the keys are k-mers and the values are the set
                of k-mers that
    """
    de_bruijn_counter = defaultdict(Counter) #  dict subclass that calls a factory function to supply missing values
    de_bruijn_degree = defaultdict(lambda: [0, 0]) # col 0 for in-degree, col 1 for out-degree
    # check the in-degree and out-degree of each node
    for read in sequence_reads:
        # Cut the read into k-mers
        kmers = [read[i: i + k] for i in range(len(read) - k)]
        for i in range(len(kmers) - 1):
            pvs_kmer = kmers[i]
            next_kmer = kmers[i + 1]
            de_bruijn_counter[pvs_kmer].update([next_kmer])
            # de_bruijn_degree[pvs_kmer][1] += 1 # out-degree
            # de_bruijn_degree[next_kmer][0] += 1 # in-degree
            de_bruijn_degree['A'+pvs_kmer[1:k]][1] += 1 # out-degree
            de_bruijn_degree['C'+pvs_kmer[1:k]][1] += 1 # out-degree
            de_bruijn_degree['G'+pvs_kmer[1:k]][1] += 1 # out-degree
            de_bruijn_degree['T'+pvs_kmer[1:k]][1] += 1 # out-degree
            de_bruijn_degree[next_kmer[0:k-1]+'A'][0] += 1 # in-degree
            de_bruijn_degree[next_kmer[0:k-1]+'C'][0] += 1 # in-degree
            de_bruijn_degree[next_kmer[0:k-1]+'G'][0] += 1 # in-degree
            de_bruijn_degree[next_kmer[0:k-1]+'T'][0] += 1 # in-degree

    # This line removes the nodes from the DeBruijn Graph that we have not seen enough.
    de_bruijn_graph = {key: {val for val in de_bruijn_counter[key] if de_bruijn_counter[key][val] > 2}
                       for key in de_bruijn_counter}

    # This line removes the empty nodes from the DeBruijn graph
    de_bruijn_graph = {key: de_bruijn_graph[key] for key in de_bruijn_graph if de_bruijn_graph[key]}

    return de_bruijn_graph, de_bruijn_degree


def de_bruijn_reassemble(de_bruijn_graph, de_bruijn_degree):
    """
    Traverses the DeBruijn Graph created by simple_de_bruijn and
    returns contigs that come from it.
    :param de_bruijn_graph: A De Bruijn Graph
    :return: a list of the assembled strings
    """

    assembled_strings = []
    # while True:
    # n_values = sum([len(de_bruijn_graph[k]) for k in de_bruijn_graph])
    # if n_values == 0:
    #     break
    
    # good_starts = [key for key in de_bruijn_graph if de_bruijn_degree[key][0] < de_bruijn_degree[key][1]]
    good_starts = []
    for key in de_bruijn_graph:
        if de_bruijn_degree[key][0] < de_bruijn_degree[key][1]: # out-degree > in-degree => potential sources
            good_starts.append([key, de_bruijn_degree[key][0]])

    # find a start position by looking at in and out-degrees
    good_starts = sorted(good_starts,key=lambda x: (x[1])) # sort by in-degree so that 0 is prioritized
    print("gs:", good_starts)

    # if not good_starts:
    #     break
    i = 0
    while True:
        current_point = good_starts[i][0]
        assembled_string = current_point
        while True:
            try:
                next_values = de_bruijn_graph[current_point]
                next_edge = next_values.pop()
                k = 0
                while True:
                    if next_edge == good_starts[k][0]:
                        good_starts.remove(good_starts[k])
                    k += 1
                    if k > len(good_starts)-1:
                        break
                assembled_string += next_edge[-1] # append last position of next edge
                de_bruijn_graph[current_point] = next_values # go to the next node / vertex
                current_point = next_edge
            except KeyError:
                # if assembled_string != good_starts[i]:
                assembled_strings.append(assembled_string)
                print("as", assembled_string)
                break
        i += 1
        if i > len(good_starts)-1:
            break
    return assembled_strings


if __name__ == "__main__":
    chr_number = 'chr_1'
    data_file = 'hw3all_A_3'
    # data_file = 'practice_A_2'
    # data_file = 'spectrum_A_1'
    input_folder = '../data/{}'.format(data_file)
    reads_fn = join(input_folder, 'reads_{}_{}.txt'.format(data_file, chr_number))
    reads = read_assembly_reads(reads_fn)
    db_graph, db_degree = simple_de_bruijn(reads, 25)

    output = de_bruijn_reassemble(db_graph, db_degree)
    output_fn_end = 'assembled_{}_{}.txt'.format(data_file, chr_number)
    output_fn = join(input_folder, output_fn_end)
    zip_fn = join(input_folder, 'assembled_{}_{}.zip'.format(data_file, chr_number))
    with open(output_fn, 'w') as output_file:
        output_file.write('>' + data_file + '_' + chr_number + '\n')
        output_file.write('>ASSEMBLY\n')
        output_file.write('\n'.join(output))
    with zipfile.ZipFile(zip_fn, 'w') as myzip:
        myzip.write(output_fn)
