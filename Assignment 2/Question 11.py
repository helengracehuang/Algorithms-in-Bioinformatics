# Prompt: Compute the Edit Distance Between Two Strings
# Given: Two amino acid strings.
# Return: The edit distance between these strings.
import numpy as np

def editDistance(str1, str2):
	global editDistanceMatrix
	global protein

	editDistanceMatrix = np.zeros([len(str1)+1, len(str2)+1], dtype = int)

	editDistanceMatrix[0][0] = 0

	for i in range(1, len(str1)+1):
		editDistanceMatrix[i][0] = editDistanceMatrix[i-1][0]+1 # indel edit + 1
	for j in range(1, len(str2)+1):
		editDistanceMatrix[0][j] = editDistanceMatrix[0][j-1]+1 # indel edit + 1
	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			editDistanceMatrix[i][j] = min(editDistanceMatrix[i-1][j]+1, editDistanceMatrix[i][j-1]+1, editDistanceMatrix[i-1][j-1]+(0 if str1[i-1] == str2[j-1] else 1))
	return(editDistanceMatrix[len(str1)][len(str2)])

def main():
	# s1 = "PLEASANTLY"
	# s2 = "MEANLY"

	# s1 = "GGACRNQMSEVNMWGCWWASVWVSWCEYIMPSGWRRMKDRHMWHWSVHQQSSPCAKSICFHETKNQWNQDACGPKVTQHECMRRRLVIAVKEEKSRETKMLDLRHRMSGRMNEHNVTLRKSPCVKRIMERTTYHRFMCLFEVVPAKRQAYNSCDTYTMMACVAFAFVNEADWWKCNCAFATVPYYFDDSCRMVCGARQCYRLWQWEVNTENYVSIEHAEENPFSKLKQQWCYIPMYANFAWSANHMFWAYIANELQLDWQHPNAHPIKWLQNFLMRPYHPNCGLQHKERITPLHKSFYGMFTQHHLFCKELDWRIMAHANRYYCIQHGWHTNNPMDPIDTRHCCMIQGIPKRDHHCAWSTCDVAPLQGNWMLMHHCHHWNRVESMIQNQHEVAAGIKYWRLNRNGKLPVHTADNYGVLFQRWWFLGWYNFMMWHYSLHFFAVNFYFPELNAGQMPRFQDDQNRDDVYDTCIWYFAWSNTEFMEVFGNMMMYSRPMTKMGFHGMMLPYIAINGLRSISHVNKGIGPISGENCNLSTGLHHYGQLRMVMCGYCTPYRTEVKNQREMISAVHCHQHIDWRWIWCSGHWFGSNKCDLRIEDLQNYEPAKNKSNWPYMKECRKTEPYQDNIETMFFHQHDLARDSGYIANGWHENCRQHQDFSNTFAGGHKGTPKGEHMRRSLYVWDTDCVEKCQWVPELFALCWWTPLPDGVPVMLGTYRQYMFGLVVLYWFEVKYSCHNSWDYYNFHEGTMKDSDPENWCFWGMQIIQFHDHGKPEFFQDPMKQIIKTECTAYNSFMMGHIGKTTIVYLVSYIGRLWMKSCCLTWPPYATAPIKWAEETLLDFGQGPHPKYACHFTHQNMIRLAKLPMYWLWKLMFHE"
	# s2 = "GMWGFVQVSTQSRFRHMWHWSVHQQSSECAKSICHHEWKNQWNQDACGPKVTQHECMANMPMHKCNNWFWRLVIAVKEEKVRETKMLDLIHRHWLVLNQGRMNEHNVTLRKSPCVKRIMHKWKSRTTFHRFMCLMASEVVPAKRGAQCWRQLGTYATYTVYTMMACVAFAFEYQQDNDNEADWWKCNCAFVPVYFDDSCRPVVGAFQCYRLGLPFGTGWNYAEENPFSKLKQQMHRKTMGECKNMMIWAYCANELQLPIKWGSMYHEHDFQLPPYHPNRFHKIRITILHKSFYGMFTQHHLFCKELDWRIMAWANRYYCIQHGWHTNNPDDPITRHKCMIQGGQNSRNADIRHMPVQCGNWGHAIGLEMPMPMHHCHHANRVESMIQTQHYWGPKLNRNADWWFLGWQNFEIFRMPILRWMGAYEWHYSLHFFAVNFYFPELNAGQMPRFQDDQNNNACYDVWAWSNTEFMEVNGIKKLRFGNMMMYSRPMTKMGFHGMMKSRSISHVNKGIGPISGENCSTGLHHYGQLTEVKNQREMISAVHCHQHIWCKCDLRIEPAKNKGYWPYQKEFCWRKQINSRKTEPYQVAPVINIETMFFDFWYIANGMHENCRRTGHKPNPDCVEKCQWVPELFALCWWRAMPDGVPVMLGTMFGLVVYWFEVKYSCHNSLYRRVTDYYNFHEGTMKDHEVPWNWDNEHCHDHGKAEFFFQMLKIPICDPMKAIIPSTEMVNTPWHPFSFMMGHDGKTTIVYSGSYIGRLWVPSRWKPYAPANWKMPIKWAEETLLMVPHPHFTHQQLWGTTLRLAKLPMYWLWKLMFHHLFGVK"
	
	s1 = "EGFAASAENPTASDDKRMARWSNDYGRICHTARVLEHVGNMWQKLEMRHKCEGAHLRVWWECPTACWCPPRIDSVGVYFNILFIDALYQRSRNVWQEDCFREIVMRLSHFIRFGNIEIGRADLVCLHDKCWPVGMITGQWSAFCLKRKYAWKFWCSTCMLPMKWCRQHWGQCGVSGQVGTYDKEKKQDCLSFCLYNKDKNCFPMHTYDWEFHNNWACRMLGVHSFHKTFHMHYLFVALFMLAVVRRDQMQNNTIILTWKMAVVTCTPFTLISQFSGNKYCQSMTMNLVLNEYGLNIIPHWAHMGPRMMVKVTKDKTPQNHMWACEPRPAFLISSLDSAFQFARERPLQLMWARLHSMKQIWRCLKRLQQRDTRIIRLLHGWSAWSYLKIKFEVGQMWGPSICAKNEEYNHCRCRMLPHHNRWSWTRWGMGNRPSCAGYMVAFLFYMEIKAWIQIDVCCKAYINYRLQYHDDTYSGFRCKIDQNRVYAITESDGMFSPPARVVTCQDWRLKLCILEPTENMLWMDWKWFKIQFGLFLIPQTQLYESDPFGLMKQQGWTAKKWIDFDNQEVHLWYHEQVQIIGHSKKQSFIREIPLSMFHEYIAFHWLVMLVYYVWNTRIRMCDEEHILAKNNFMHGIDMRQGMMLLTKCRTNEETYFPATPTDEFGIHFPITQGSYMTTYSCKFCKKFCTQVYYHVYPPHVICSEQSGEPEDGYDTDPFMDVCQNDAHCDGHVPENNSHTKNHGLIARAARHLLWNMVVYEVICYKDIRALRWYDTKPFPEMYEVPPMWKVISCEFWYITVRKMYMWIDDDPMIESCMCYCLDGCHKCEEAYFPATKPFSGECSALYADTCMWHASAMVDKSYLAHWGCRWSQERRIMVCFMAGYPDFIASHQTCMKSADFCCQHQLEFATSISRFGLSFFMYPNIQANYYCICGAFMNEYFNDHKWWSWKKEVGPVWDPSWRARNSEVKWWSVFQLIVARCMIIGRMGPVPHRCWHVWDANGVATRYDQYNNWYWHMVYVMWGQMYHIRKRYSSTCDGWPSDVCRESKEAEKSETAAWNFAKSPKYQAAYRWKCTKVYEWPSDHPTHGRRPCDEARVTKAWLWTVSLMPRAPMSYFNTHMWVDLTAPFECNHFQGETCELEGGRYDVPPVTVKPWPRLEFSETRMKVVAGFPTYHLFDAPNCWNSMYECATDTVMVCHGTQVMMNCTQTRESSHFGVWFDLTCEPPRKWHLTLDNSQYWICIPNYDGSLQAFIYYDQRAQCHKWYHVKEAFEPLQIDSPDWPPISGAHGVDYWHCAIGNTSIFHNNYTTYPSCCVCYMLDKAHKCVAFWQLLFEGFRGWWYYMWHATHNMNWDHMTQEYALWSILRHILGGYEIFCPLRKCAIVHNYMDLTAHPDYDLDYTDIAHAPTWNCQQHDAGFQANRITECSAAFDGELEKQYRTYAQWYTDSAIKMWAVSPEFIFFCGNEGTYEGAKYHFTYNADGMREYLQDFNLDIDYVQMWWLRHRLVMHPECNCEFRLWCMDGLKDDTPMGQLSQYPRGLTVCGWIDVMSYVCWHYESCWYYCFPSAITTLIAGCGQGFDEAAHFFWGTPNINTDESSTDPMPDWTSVIGYGPVRQWCMYDRFFEGDLIKTHCCHCSTMPMWLTIKHMPHQNRVGQKYCQSNCEYAWDCFWSFRVVLDPKVDRIVMLHFLDEKPDLTQLVISQPCWQVCIPWALLWSSAYDMCRDTEANTDFCLHFRVFFPQTATKMKNQDNEKGLMRWRDDWRTQCAHDFKPDVPRTDCLTKSVTKDGAGIFQIPWFIQRILDSRGNAWVQWIEQNEYLYVSSINVSFQSWPGTSQVPLWSGAVSEFFLKEYWYCIRLRNAENQLITSSMKPQGWLIMSTPEYIAFDEEETEFHNERFDREKTGNNRHPVWDNVSASTMYNVEFDCKGLQSWLRNVMIKYLCEVLHWHKLQWYPAWASNGMPYNAYIFIANKRGHELKRVRAVCNAPAQYWHLRRSITAQGRLNNSSQCVYCGCDRPAMTYMKWAQHACHNHRELNFVSKNVKLAWHGIEFNFMTIKSQEILHLDHTHSTFGPTSIMPYIVLFHHMKECLNIWMRPNWWNLTAYMNWVFWDHQIQTICCWHHVIMGCTFIATAREGPRNPRSHVIQMNVKYLDLKGEFCADKLHMFSASSVMPWTTQYTYNVGVKDDDQCMIDNYQWIRVIFCNKGQKDEKREYHRQHYIIYEARNWHDNMNMNISFCYHFIAESPWNFDQSWKAGVQWALSMGQTEFQFGFRIWQCKHTTDTVMHARSFDLHFHCRIYRSVYYKQVRMEWWCKAVIISQRKWTWKCPSHDQSPKYFLAERYYNNGFRRNHDNWIRSLSYWQTLFLSQHCQPISQNLMICYVWSRKLPQKDSPLRNRRDEYKLNCASQVEIPHDEKCWTQGLGDSNGYHTPRQTGCMPETKITWPFGFDPICFRCACHHEDRAQCALVNGLPHYKFAHIVLMLNAYFWAPARTQSLESRAYYESWWFHGMMDTIFECRVYTWSAMQHCVMYANCATQTMQNIIWTGKYPMCIRSSTWISGGLIWPNEYFLRLQHVYKSWIKRMCIPYQKFIQPHPMQQNVVSMVVHFIRRSKTDMAAQDKRYSMLDINNGQNCKKARGQLDNFNNIMDHWKYMDYVQMDKYYFNAGTRVRSTMPAMTMMMWFWGKPNRWISHRKTNKAQSELTHWNWASLPANHMPCWCFNQACCSLWCVMLGGSLAGIECQNQVRYHNTCSCCFGVADPDMDHYTIIMGKPYQWKTVAIPLGNLTLYARDIHLDSLQCHCSKCQCQWAYLNPANHCGWLTTCIMYPPTRFRDDKAATFKKYFFNWTWRRGQDEVDYMYFWSPLWKRFVQRLWWTTRIQCFEGAILYALLRVYRLIVSHCIGWYHKWFEIRPKEVCVKCTTYWIWPFLQSQPNWSKSYHDKRKDIYCGFMLDAWEGRRKGHLYRLQEGPWYYKGEEDLPVGNHGQLQMHKIDHWQYGIFATLPYENKCWCLQPISYLGPTNVTHCEYAAYMKRTLGPGNWMMWDVDSTNLYLNRTHSPEWQTRAHMCAARGHGYFNMGRQYHNTQMMEMEKRHFPDMVCYRITLYIQKIKKTEIPILGESGKQSIKSRWIFPMGTQCGSLMKSIACWMIADFMRERVHREAVNDGIKQQCHMTGLHLIGLNCWIRIRKHWRQYFEQFVQRKMIYWIQVASFGKGTWQLPCQDWTGECKGHRTCAHKKNVATIASWCYKMQRFSSKGYFWAMTNTRINVDNRYFTPTGGEPFCTSEAWDMWRPPDQHQGDLSLWGSRSPVMWLLMCRNYPEWACYTQFRQFEFCMWRFGRAAMYFRWKHRYAKGLSGWKMFKNMKWMPVGEQSFYWNKYDGALNCGAFCNPTENCQPYNMFHMWGYPTRHRNMMNDRMSYTVCQLPVIVLQGTRFFTPWSRNYKCRKHEICYRSRYYMLCPHFWSRLDQYFAVKDHNGIGGPQIKTTCGDAIGHLPHIRKRRQHPMQDYIWQANSRSWYRTRWHNQWFWIFDCRDSQLFGLAGQSRMIMQMERKSIKNFRHNNHHACHREITRGDRGACENVYDTHVSKASRDYEDAHARSNCKLFGYTVLEKLWLWNITRFMKRIRWWHLDPFGEEENNGKLLSCVKGLAHPSPHHLSGSITHHVLVLNPLYYSFWSFAELSSYCDVCTWCRLVYMNGALTDTVHCPHSRPLICHCYICRRSITMAEPYVWWAHFYCLVHNHCQCETWNEAKHPQHSSHDPQERMLMQLSHLSNNIKYISVGGLNDAHADIGLFLENSKCYHEMDCREGAEAIYEEDCQYATERAYPWIQAHSKDGDAVKENLVIFAIEWQISLHCKKQMNNHQNSYGIHPWGIAGGERWCLCHSLGDHPWWEWLLMHDQTSVNCNFDDLPMWTDVTCIEQLTEGDCWPAIFWWNWKDFIGSQRDYWWTQNTCPCNRRHIEPVDNTNAWNMRAPDCGIGVAVPALLISMDFVTFSNINMRFMSRQWCDEWVNDVAMQTQIWEITPVHCKWYIWCMIPIRSICEQNHCNHMIGKEFPPQPKDSFEFQTWRIASGQTWNMPKMDASNHWGIGELIMAIHPVNWRCGNSCSMSERSDVLPFHNLTGPIAEFNLEYYAYVTYEENLHPWSFADDIIHDCTKEAYVNRDQIRKCQGTKLW"
	s2 = "AQNPTADDKRMARWNDYGRICHTARVLRHVGNCEGAHLRVWWECPTACWVYFNYLVDYWMSLFLDALAQRSRNVWQEDRLFREIFRFGNIPQIHGSQPGTDMHCWPVTIITYQWSAFCLARKYAWQCWKAHRHKAMSTCMLPMKWVTYDKEKKWDCLSFCLYNKDKSCFPMHTYDWEFGVHSTFHMHYLFVALFMLALRICCPIRRYAWVMPLCYQMQNNTIILTWKMAVVPFTMFSNKYCMTMNLVLNTYGLNPMLVKVTKDKTPQNHMWACEIRPAPAISSLDSAIQFARERPLQLMWARLHSMEQYIYLLHGWHAWSYLEVGQQWHPSICAKAFCHYKEMLPHHNRHSWTRWGMGNRPSITIAKANDYYMWEKAWIQIDVCCKAAINYRLTYHDDTYTGFRCKIDQTYDITESDGMFPEINRVCQDWMLKLCILEVNETEESTEMMLKQDSFIHNFLIPQTQLYESDPFGDFDGSLMQWCIQEVHEWYHEQVQKDSFESIKFNQPIAFHLVYYVWNTRIRMCDEEHIGGDMRQGMTNEETYFPATPTDEFGIHFPITQGYSCKFCKKFMTQVYYHVYPPHVICSEQICKHDGAQSEPEDPYETDPNAGGMDVCQNDAFAWECDGHVPENNSHAHGLIAARHLLWNMVVYEVIKIQPVLVYKDIRALRWYDRKPFPEMVISCEFWYITVRKMYDDDPMIECLTDRFCLDAYFWATALYADTCMCHASHWGAQDSIGSYLGCRWDTFSYYERRKMVCFMAFPESKGIYRYLNDKKCNDFIASHQTCMKSADEFATSIPKAGAQQMRFGLSFFMYPNIQANYYCWKSRHCGAVMNEYFNDHKWWSWKSEVGVLGSEVKWWSVDGDQDIVARNMIIGRMKPVHKWDANGVATRYDNWYWHMVYVMWGQMYHIRKRYSCGWPSNVCRESKEAEKSETAAWNFAKSPKYQAAYRDKCAKVYEWPVKIRTNDHPTHGWRPRVTKAWLWTVSLMPRAPMFNTHDARTVQWCFVDLTAPFCMIFDEGGRYDVPGVTSRLEFSETRMKVVNQWAGGESMTIVVYDRPNCWNSMMMMNCTVWFHLTCEPPRKWHLLLPNYQSWICIPNYDGSLQCFKIMYSRAQCHKWYHAFEPPQIDSPDWPTMWCHQSPISGAHGVNYWQQDWHCAIQNTTMAEESIFHNNYTNCCVCYMLDKAHKFVAFWQLLFIGMRGWWKDIQYALYTHNMNWDHMIAWPQEWAWWSILREIFCPLRKCAIVVNAHPDKDLDYTDIAHAPWWNCQQHDAGFDAECFCTTANRITEVSAAFDYELEKQYTYAQWYTDSPEAIKMWTVLEPSDEPIDTYEGAKYHFTYNEYLNDAFNLKIFYVQMWWLRNWNGHRWHCPVRLVMHPECNCEFRLWCCDGLKDDTTMGQLSQYPRGLTVCFAHWHKPGDHYESCWYYCFAVWHSAITTNIAGCGQGDDEAAQFWATPNINYDESSTDPMHNWTSVKGYGPVTQWCMYDRFFSGDLIKTHHKYHKWITMPMWLTADDKHMPHANRVGQKYCQSNCETYRSFNWAPDCFWSFRVVLDPGVDRFLDEKPSQPLWTVCIPWALLWSSAGDYEYRPPAHRDTEANTVEDFFPQTATKMKNQDIMCMQKYEKGLMRWRLDWRTQCARTDCLTKSVTKRGRLTMNDYWIFQIFIQRWEQNERLYVSSINESFQPGTSPLSGAVSEFFLKEIWYCIRLRENQLITSSVDSPQGWLIEPIAFDEEETEFHNERFDREKTGNNRHPVWFQNPMTGHNVLASMYNVEFDNYLIEVLHGHKLQWYVAWASNGMPYNAYIFGELKRVRAVCNAPAVYYVYWHLRRAQITAQGRWNNSSICFPNITKNACYCRPMWWAQGQSKEGNIACHNHVKLAWNLEKGGIECNFNTIKSQEILHGPTIMTYIVLRMWQLLKSHPMHRGLMKECLNIWERPNWCDSNNLTCYMNREWNNWHFWDHQRQTCCWHHVIMGCTFIATAREPPRNHWRSLDLKGEFCAGWYLHMFKHYTNMSATSVMPYTCQYTYNVWVKDDDQHMIDNYQHIRQIFCNKGQKFSKREYHRQNGRGIRTTAEARIIYFNMNISFCYHFIAESPWQKDVTSMFDQNWKAGVLVRIRAWRWWAMSDGQTEFQFRIWQCKHTTVNHQRSFCRQNKQVRKELWCKAVIISQRKWTTKCPSHDQSPKYFLIENNEFRRYHKLAYRIRSLSYLFLSQHCQSISVWSRKLPQKDTKIQTTQRPLRNRRDEYKLNCASQVEIPHDEKCWKGNTPPAYSAGLGDVWNANGYTPRQTGCAVLNTARPETKIMWYHCKEAYWAFGFDPICFDCACHQCALVLPHYKIAFLHDEISLMLNHYFWMAVRNAAPARTQTLESRAYSESWWFHGAMDAEIFECRVYTWSAMQRCVMIICATQWMQNIIWTGQYSYLCDTNDDTGINEQHVYKPATEEIFWIKRRCLQCYQKFIAHPKMHRKGIESMVVHTWFRRSKRDRPCKWSHMLDIENGQNWKKNNIMWHWKMDKMYFNASGEKMLHTMMAFWGVPNRWISHRKTNHWCFRSMLGGSVAGIENQVRYHNSCCFMHTRVKQDPDMYHYTIIMGKPYQWKTVAIPLGNLTLYDIHLTSLQCHCSKCQCQWAYLNPCIICMNHCGWLTTCIMYPTERFRFDDTYFPIDATFKKYFFNWTWRRGQDESKDPKLFRVRAFWGPLGKRFVRRLFEGWILPALLRVYRLIVSHCIGWYHCFKWFVLFTWPFLQWQPNWSKCYHDKRFMLDAWCPPQKFGRRKGHEYWRVQEGPWYFKWWAKCGATDLTVGNHGQLQMHKIDHWVYGIFATLPYEWAFRLGPTYVPYCEYACWYMPRTLTCYSLIPCNWDVDSAAWWWNLYLNAGMCNQTEAHMCAARGHGPMIRCTPNSLMHQFNGMVCYRITLYIQKAKKTEIPILGESKSLKQPIKSRYIFPMGTQCGSLMKSIACWMIADFMYERVHMVDRQFTEAVNDGDARKQQYHMTGYWELPHLIGLNEPMEQYSPIRIRQLHWYFEKFVQRKMIYVASFGKGRDYWRLPCSCAHKKNVATIGSWCRMYKMQRFSSKGYFWAMTNQIWHGSHRYWWRYFTPQLSCTSHAWKSPNHNDPDMERPPDQHQGDLSIINKHPFQSRSPVMWFACYTQFRQFEFCMWRFFRATMNGIPAMYFRWKHRYAAISHKELSGWKMFKYMFPMQNPFYNYQSFYWNNYDGALNCGAFCNPTENCNWGYPTRHYAITLQMAELMMDDRSDSQPVSWAFNLDFQGTREMHKCSKFTPWSRNYCYRAILNRYFPEDETALACVNLDQYFQNKDHNWITVYMQVVDIGMQIAQMWRDCYTLCGDDLNDRSREYNRRQHVIFFCLTQDYIWQANDRIWEWKWHNQWFWIFDCRDSQLFGLAGQSRMIMQMMNNHHLQLLKLSRDEITRGDRGACMNVYDTHSRAAHVCYRSNCKLFGYTWRHCLSWNMTRFMEHLDPVGEKENTGYVAAAALLSCVNKPRCIGYQGLAHDESPHHQSGSITHHVLVLNSSKSCWSFSSYCDVCTWCRLMNGALTDTCHCPHLMLIRPLICLMMYHCRRSCSMKEPYVWAVILCAHFYCLVHNHWQCETWNGAKHPLHSDHDPQERMLMQKWHLSNNAKYISVGGLNDHEMDCMEDACQYATERAYPHIQAHCCFDLDAVKDNLVIFAIEWAISLHCKKQMNNHQNSYGIHPWGLPAGGELIKVPWCLCHSLGDHPWWMPPPLLMHDKHMNESDMDNFDDLIQLTERRGIRPWNQRDYWWTWVHMFTDNRRHHFEPVDNTPDCGIGVAVEALLINRGMSRQWCDEMVTQFDGPANHMQTMRIWETTAMPMFYVKYKNGSGVHWGCPPKWYIWCIIVWSFIRSICEYMNWCNHMIGKEFPPQPKKNQRFLSFEFQTPVRIWNMPKMDASNHWGIGELIDAVWLGLCGNSISMSERSDVPFHANGPINEFNLECYAYVTYPSPSSNYENERRDDIIHDFSWTKEAYRDQIRKCQGTKLW"
	
	print(editDistance(s1, s2))

if __name__ == "__main__":
  main()