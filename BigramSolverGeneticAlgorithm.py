import random
c9='''fqcmwysbcgusxmowjcjkjyewxsaqvweffuuuusnwiwkgfajqcmnulmfweedmrycgvsnmchxuuwzwdvvapvvsscnedmrvnsvsscneemjmnvpwstposfdefbfcaevuuwaycgjtlhccewcagenfjhxenuuwlajtlhchxuuwnwfusvtuusnvhgcafvdvwwiqfifufcausuuwhvpnccgedmmenblgutxevujyeiguuwfycmpskevsscccefgzcujfuvmenmjafysjnvwijgsbfcaepenujyayjfpvkwccebsyjevucgumvvpwscvqcucghvlcvenfjhxentkvpuuwnspsxeksvostsjkavjesjauwcuxwdzvqrysnsajmvvpwvyckjhfcaexhskjyjjkvrwvvawvqjynjrnsyvsdzsjkajhzwnwzwkomqjyjigfsytsdzcusjkilafcjansmenvdgjsdgxsdweussvilupwdufvdsdzfuvvpoavsmwyfwdmpyewdqcbmsvqmqsbfvwujcnnjcvedqsjkfuwdsueehjsnjkwuwesnaleewebjtkvpsveekfafcabjusuusdlscxostkwvjkcfcausnjcdaghzedscfushquwmencsfcisjvusmsspjnukwhvkmscjukefustvqfaavsmpedahqcycgvwkqjqcmwvkbjyxoowjcfcojnsdwnacuoyfavvxiluwefhjmfcewouvvcclbowkvwnjvrhjgsbrvlceweedmmwduvvcbjyfgcuuwkwoocgxvnwcnrhfgcufvdusilafcjanenepwkgueduuwcgyjfyjmcnxwduftlhwvkulcjsdewwmojekakwvjkcfcauswdzxedmfcvqjausrffuubjqjsdkfujmusnvxmhyjmfusynusedwdujyvefcpwducumqfguqjuuedleuuwptsyvqjwcaggsbrvnsvsscvqjoueetcksjkweqfbmsvqccefuwduuwgwinjgvwecsuusdzojvuuwvyjevwzwkopedevuuwwskavyjbskjtsjdmlcewkqfarhcujedvkmjysccicctwktsyvqjtlhxepvlcvvwuuwlcrefmkwpefcewkffuusdujyjavqjcsfvvxmpwuwmeneovluvvkwvjkcvvrqfhcmjhrqfecceauvlhegcykoskjyczkwcuyjccvsvostavsmnsdvkmjyvvsnjccavvkwvqjyjqjnkvrvnmvvvetwpwskjycausngxwklvvtwjnusnisvtafcmqfguqjfsjxmfcnukjhupwhvrousnhjuvwkacceevujceuuwnusyjqjeemjmvqcucanvsccafauvlheijehdlefcvweffuubjyhedufhjilafcjanqjfsjxmrysbsujbjigajcesdzpwmsvqcgcyavstwhsjkedmoyjeewvgvvvqjfjavsdmfwnedmrysglyjbjgsbpsnafvdawysbsuuwkamqfgufsjxmowrystfucixwcceswspedeammwxhmvlhewnucixsnqpwuedmnvpwxovqjuusdzrhjenmpwwvksmenzkvmcvskwevwhscevdyjbjbowkweffuunxwcalyjuuwuerngbscvqnsueearwdufcrwdcnoxkccfecceffaumczcsdusajwfuvqjyjtsyjsfbpwescujhgeayjwevduuwvwkbnvwtftvorvlceacojeknjcdaghzedscbscjoxwnafcewjmvqccporyjajcvzjuvsdznenehvpnsafusyojvewtsyesdzcijuvwknkvnnjgveovlufcsfvvslxwckjvwnksdufcaensvqsjaqvtsyjkjyccefcaeefhgwpnxvgwesdbgcjfojnsdwnaavfcaeovlumsvqpyewdqcbcbscauuwvycmjapwdusnlyhqcajkcyfvlacyvshhjacceajwfcauuwpncgtmlnevfcawkycceahexhfcajrvdfsytbjcvvesnncuhqjuhedmmqjcchxfcascovcyesueeewwmmconhjsnjkwscscjvwuuwnweegaffcavvponjknksnwnwduwvkigeayjevbccfldwmvdhgigccbjenskffhxscbmodmuepedmffcsvwejrvdqfbuwueeqjekmoonvpwpwccnvkvvqjystponffbpsdzwysbhqjhnwcusixehlwyfekaccevwbgujehqfcafgzcujedmccsuuwkosjdzpedusamspsdewwmqsjkauwueeumvnvdacisjvusajusjvvduuwfyvyckjhnqjffaumvvuezwvqjbwskavucjaqvamspbfcaedmrysnsajmvvaycuftgbjqcceasbjhgswsmvlheujehqvqjbvqjomwkwdvvojuhvpwvvvvmcccebgavegfcalchwkucsdasshvlhecsulcewkucljsviluwysbvqfafchsewdufuuvlzuufuxstwxovqcuftffjyjusyjbcsdsdwdzxedmccevrwdenffbpsdznguvshfbfzuuawveavsmewchstpvdwgedmfunukjhlpwnvnukvdzxovqcuueeuuwskjyvjkwowjcnvscjypeewpwrysicixofauvlhecsunvnvscuezwkwvjkcjmvvcbjyfgcewujypedogwcynosjccesueeasbjuusdzstpvkwfbrvkucchwvvevmsvqscjvwuuwnwnvdastnskffhxscbmodmuepijgsbjwcyxvwwayjbscvfushqfauexhpwdufvdsdsvarhcgjuujnsnnjcveovlujsaqvwjcpvduuafcxvdmscpvnurekustvqjufbjsmvkleqcyeevbgilafcjanedmnnjcviluxsvuxwlnscponwxtjrhwrufcnwjsdzrhconedmfcovslnbgtksjceychrqueeljnvbjnsvkqjvmwebjeovluvfjcvonwzwdnsjdmnfushqffcadvmcjkjyxstwxovvkwhwfkjeayjevalbsjvvwbgapexhjekcfcaafhskeqfbdvvffuuavedmfcatsyuwueebccgepscixwyjchfufwnsueeigcsbjedafbryskebgtsyvjdwojvsueenfgtwejrasbjkjygsdzjcfvlacgyjcsducchwmqsajgsczwkacufvdfcastayjeveekccveawvvpwccesueeyjeegscnsewkeohgkfsowasdcfcailafcjansdnusxeewxnuscfjacsxmwysbayckjajcevduuwkmstbjxowvkuuwfchsewdunvwuuwzvgeawfyjtjygvlusbgxsjkcchmqjyjosjmsxhwsdmvqjbchxbfclujhgyjhcujmrwkqcnnuuwpvnufbrvkuccvncyvvwuuevxsjkcchfavqjnxedusijtsjdmfcfumqfguswvkbjmcunwctsykwajxevsdzpowjvjkwhvdmlgvsdhftjsvsnuuwpvkwkwpeklcixwcaowfcatsypwefuwdsmenasosjdzcceojuowfcankwvugtcsvqwjxhgeeqjyjmvvyjfujuuysusvxmczjcsuwvlcesduuwpedjngksrubvlydexfushqmenhjtvepvdzwyccthfcnncnjynifzjhsfmwxedmjmfcrqfhcmjhrqfescvqjuuvwvhusijymqjyjswvlcealceygexujycufvdatwfuufcadvxvdzjyavzwkcsyowfcaalnjynweweigbcxsyavkmscfbjuuspfchtsdzvqjavyjwvacacgsbpvdgfufpjcuwnwjbeexsvuxwcauepmcunwjsdzpwojvncanmmsvqsjvacofcaedovqfcasnqsjxmuezwowjccapjhqcauepmcunwjsdzpsnakwcmueecsuuwktksjceaewnncsksdzmsvqkwcascstpokwvjkcctvwkuuwkwhwfnvvwbghjuvwknjynjcmjmuwkusbcykoccsuuwkvdwkvawkacnsuvwkfushqmenmscjsdbgeoajchwmsvquspqsfjkjynqjfcadwzwkqcnrocceasvdncyvwetkvpqfbkwwjnsdzvvhvueosvffuuqfbsyowcyusnccbjsvijsdzdvmacseuuevqjqcmccsuuwkfftjqjfcacfsyvqxwnawwxhsfvqsedwigjhxwdumvklpedfushqmenuuwvwpnvevsscvvuwktksjceauwavvsdusmjivycccfcofcsymwduvvvqjfjavsdmfwnedmesjmvqjyjljspwkqcmavveowvujyuvlajenqsnmwxhnjrnxoeffuuavevsscjygnxwdugvwcjfvorwnedjpijystuedmnuuvdvdwavsmcceajwpmvvuezwczkwcuewchstojnsdwnapyewdqcbvvslcavvkwfcmevwkavyjwvfuwkwmwsnjcevlyavsmnscuvwdmjmvqjilafcjanmfhfzjcvhgavjesjmcghvlcvaccezkwmsdexsvuxwvspwjrrwkucunwxhfcafjhsmamcceisekmjmvvawvqjyuwhvlcnwxhebjenewevqjyuezsdzcafchwkwkwaekmwvkbjskwnnjgvweedmxvzweqfbccefjbfzuuuezwavdwscvvawvqjyzwkouerngilufcvqjijzfcdsdzstwwoylekomqjcfqcmbjnurenaebgumwdugtfynugwcymwovvqmwkwvetwdsxhpoesnujbrwkfcacnxwlyfagfushqzwkodwcyxohekyfwebjvwtfaltwwkweeavsmewchaezwlnvqjnssdufcposfdbfceedmmenycuuwkmfacnrvfcvwefuwdswvlcebgajhwyjgskjyfcayjzkwvufcasdasbjmjzkwjuuevspjnudvmasbjufbjvkvvqjyuezwchxuuevmfaczkwjeohjfsytusmsvzwkeaefcftsyawvfuevqfaesnujbrwkfcafuuwxmuspexvdzvspwcceevhjcauugcyksjmuspvwtuwxwwupwcapexhxwaehofccclchjrevszwmsxhcacusljcstusnlfcecjantsypwcceqjhjtvbjvdgjbsyjusuuwmsewmvkhetsyvqjavvkwmenucljcfcvvvqjgcyjvwqfajrjglusynedmpojbrhsopwdulcewkqfbjcewesxhlavycufvdbkmjcuepusvtenusyjsdfcujynukwjupooysuuwksdhcfuvxbjaowfcacsfcurqfhcmjhrqfecmzsnwebgyjulydusbgilafcjanedmtwfbjyvwpnvwebjffuuedvwtjystxekzjfczjaoovqjojekusgsbjedmvetwvqjbccczjbjcvvwqfaryfcvsdzuvlajuuevqjbfzuuowvujycuvwdmusnavevsscjynauvrsueeqjekmcicmhqcycgvwkvwqfbfcxvdmscwysbusnfftjedmuwktksjceaccefcadvvtscevwqckfcaedopvkwvvevmsvquspsvyfmwvktcyvqjyjbrhsopwducacbjyhqccvahhjytiludvvyjeesxopwjufcaffuuedofgxvnmczcsdffuuljspwkswvlcesdqfauvlajuuwnwuedmnqlzubjyjmfuuemwxaunjcdaghzedsccvqfyvogwcynvweawoyjmvvhvlcvygfsytqscjavajcnsohjqcmczkwcuewchstnvxsevoajyzevsscmenasbjuusdzstcyjeewkiluaszwdusmksdlnujnuwdnsuvacosjdzhvlcvygbccstwjxhczjikweusuuwnepwstlchvpbscdevjkexncyvaccezkwcumsvedmujpvkiluchfuvhjsehjuuwnwuwueeeayjweffuuevwiukwcbxvmfczjarwkfjwtusijycsnmcausxhfcawzwkovqkwjbscvqnenuuwgfsjxmewnwkkjigspnkvzsdzfcvqjskilafcjanedmvqjwinjgvevsscstvqjajqfzufczjavvhvpwscuwkwctvwkfcamqcuuwueemkemcvqjbfcmsvqpwkwesvqmenusfsytevnkwnarvvunevisvtifcesdzmqfguqjigeayjwpwdumenusujehqvqjbvqsjaquwtcjfdwfuuwkvdwdvkusuuwkxsqdemsxmfyfaubccoysjaqvjruscsilafcjanfuvnwnwkkfgjtsywvlygwcynljspwkqcmrjkguenwetkvpuuwherucsdvwenqfnuwvvsfcavvowpeewcnkwnapedzjvkzjfjioedvitsyeahqshcymqsajufbjtsywvlygwcynqjqcmxstwmsnwovlzuufcvwdmfcaqfbwvkehvpnsafusystmqsbpvkwryjajcvhgedmeezseqcykocgsjdukoovgfuvpqjqcmvetwdernkwdufgjsnvscrwkgjszmvqcuvqjsdujcvsscstjcaeasdzpwcumeawnasblguqfzuwkuuedqjqcmowjclaeuszfkjfcavvuezwvqjajycfhqjerqcceawvkbeuuysbjedmcanvsccafqcmfcnukjhujmvqjbvqjcvqjoowfcaexhcyvshhjmvvuspqjauvlheijeohjusmsffuuvlupwffjcvvdqsfjkjyzwkohqjektlhxorjvqfaryfcvsdzuvlajsdvkmjymqfguqcmowjcfcayjevgscwjnssccceikvlzuuusnqcceaooewayjwnusbfceuuwfyojnsdwnacceusmssvijuvwksvfcaccsmeuusdzvvwsdmccsrwvkmnguvxeksduuwnsvjcufvdvweovlzuunwkkccvqjfcadvvbsyjuuedwfzuujwdojekastczjedmaezwpwvqfacghvlcvvwqfbnwxtvqcuuwmenisydsdzxvlgjavwkwejhevweeveaycbpekahqsvxuuwkwueeijwdmfavsdzlsnqeepvdzvqjahqshcyntsynvpwcnrekwdunjrwkssyfugsdnjywvkbfcaqfarekumqjcvqjojrusosvwenxegaowxvdzeusuuwmsvuggxjouuwkwcceqcmmyfuvwdasbjnfwhwnsdnkvnwccekjynwmqfgufjyjnksdujmfcvqjzxvlgjavwkcjfnncnjynuuwdgjqjfcanwduvvsrwvkmmqjyjqjgscvsdjjmcisjvegwcyojvcsumwxhnevsntfmmsnqfcavwexhvqfcaavvnwjhscevdedmowhvpwcnxegwkevhjcauuyjgjszsdzusndlekujyxochxvmedgjvwtftvwjcajfcjensdavwcmstesnguekzfcaqfaewounqjfchtmsjvvwusfdqfmusnzsfdsdewjkpjilauedmwvsujmfuvvxvdmscmqjyjqckfcacstksjceuseekfajqfbuwwwxhfcvvoeegsbredonvscnnjcvqfaajfcjentsjdmdvpwccnvwijsdzfcvysmlgeepvdzvqjnxegwkaayjfdwhwnafusjnncfdmusngxvcuuaccefccvweikwcmmexlfcauuwnukwjuzwkoujdzkoccecsutcsffcafuevusmsffuuqfbnwxtcgkspnnifhxfcarjvsdusqfauedmstwwksdzfbpwescujwdujyvefcpwduccewdgsjkeawpwduvvnjhqcamvlheifceuuwpajhzwnusajyzwfccbjyfgcqjfjcvmfyjgvhgafzdmvqjsdmjcvjkwnfcarjvsdusuuwnqfnccegcbjvzwkcjkjymyfufcaexsdwvvcgyjcsduusntksjceamqcumenijgsbjvwqfbuwmenhfkjhgffuvoavsmdevjkmcceerhjeneduhvpnccfvdilufmxwvqsjaqvhjanedmfbrylmjcvusuuwxenuewayjwcgkspnmenuuwczjcvvwenqfnrsdzhvpnccggkspnnfjyjasbjufbjajbrhsojmvvewhvgbjcfcvvnjhqnwkkfgjensnqjyjbjcvsscjmbvucvqjsksnqpedasvdycccfcomsvqvqjyjavsowaedushfkjkjygeayjwcixowvkuuwgexhkwnnjgvwebjuuwpvkwcavqjowvlceljspwksdgcncixwstfcnukjhufcauuwpedmvqcuwysbpwvqjoxwcydweasbjuusdzeefhgfjcjkjymvkljmscnevjkmcovqcuowfcaljspwkaneoicuuassueeumveegawvkyjeesdzpocgyjcsducchwmsvqfcawdssjnnjvrhjsduuwvvmcfchyjenweljspwkqfbnwxtvyjevwebjffuuzkwcuhszsxsvocceerncyjcvyjzcyeedmdvvqfcacsfpeewpwlcjenoojvbgmjivuskjydvdfushqffcagwvjdeohjusncoowfcaqfuuwkusilucnsvkgscsbfavqjqsfjkjytsdmxopeewdvewpedmstfusjknksdufcaqsjnwstvwdfccvweasyvacceuuwkwmencshjuvwktsjdmjyfccbjyfgcsueeajwdugnjahenucubepwnafcxvdmscojvffuuvlupjhqcuvwdufvdusuuwpedcjyuvmwzwksdvmgscvyfkjmcbsjxmpeewlajvwuuwxwvujynfjqcmcarjdguwscnavylgtuuwpevukshwnsdhjeeedmvqlanjrnxoesderyjuvovvxwkeohjfcochxmjtfgfwdgfwnschnvjcayckeajkjychvqfcaascsghensscfbcmjuuwfctsmenfcyjqsjnwpededmjkjyguusdzccesdauvkuyjfujewehusulbojvqsfjkjynwkkfgjeohjspsaqvijswvlceuuevbgajyzshwnijgcbjwzwkoeegvwhjanspnsyvedgjenuuwsuuwkqcceafbryskesduuwojnsdwnaccefuwdljspwkncsebgajgscedlekujynfczjauwxwvbjldvmuuevqjtjhvuuwpusvuwckgedmvqsjaqvsnqsjxmpetwcccicujbjcvqjzkwmigmjzkwjaxwnahszsxnluscpvkwstvqjbcavwktkwyjjcvhgtsjdmwelhvfcaherufvlacceajwpmkwcmgtsyccsjvikwclfcasmwduscdwzwkuuwxwnamsvqczsvemjexvwncufwdgjuusdlfcauuevqfajchjpijyegfyhjpavedgjamwkwrekuxovqjgcjnwcuxwdzvqcukswhjaderusjkgscdwhufvdawvkeayjevcssnwuernjcfcacjekuuwhvlyvqsjnwfnlupouwcmsjvvwuuwmsdmsfvvnwjfuevfcavqjbcuvwkljspwkijsdzfcvqjavyjwvhsvtmlncceacfpwhexhevluvvpwfcchsjeksshwcceedzkovvdwvvpsdmpoojnsdwnacmesdznvpwkwrysehqwjxfsyeavqcudwvuxwebjuuwpvkwwvkuuwfyrjohfgfugexhvqjcjsaqovlynfuvmwkwxvslfcavluscvqjacbjvhgcafvdijsdzmsvcjanwnqsfffcavyjevweqjgcbjjrspbjmfevwxofcvvvqjnksdufcaqsjnwhvdufclmvqjdlekyjhusaqmvkmnncanmscovvqnsewnqjzckjbjuuwyjcyvwkamekcfcafjqcmnufnlhcujmjrryjansdzcffauuuevqjqcmdvvijwdvohfzeusashscaemekcfcasvvxmuspqfamsnqmenjdcjgjanekowvksmvlhehjezwuspuuevsdaveducceasuclfcabgqcumexlevlustevsynmjafyfcabjyjmfuufuvpsnemijhsfvvvetwhekwstnvpwvqfcaafhjtvedmoyfcauuwpusbghsmasdznbjyjmfuugcbjehgsyesdzxofcvqjwzwdsdzmqjcmwvexljmpoctwefyskjyuwueegschwfkeeayjevyjzcyetsypwccefcazwkolcmsxhfcauuevsnqsjxmxwckjuuwuvlajfusxwuwkwpefcesdsvqjmfanjcmjmpwwysbkwvjkcfcausbgccufkjgsjdukomqfgusowaedusuusdlstuwkwpsdmjmpwvqcutwfbjymensdmjivtsychxqjnsanwnaeuuevqfahyjmfusynijzccvvowlcjenovqcuuwtwruusnauvrbfajycixonvxmstvwdffuuvlurystfuwvkyjeeopvdwgedmstvwdukjnujmmsvqsjvljwrsdzcghvlcvavqcuuwpjnuvqjyjtsyjtcsxfushqmvlhebcljezehedggspsaqvnkvwsvvwssibwhujmpomedustpvdwgqjuuwdhjupwtcsfvqcuusntcuuwkqcmcqfzuvrsdsscstpwccetkvpasbjmfahvlynwvqcuueencanmowvfjwduuwpqjfcanjkwmvlheeekcchwpvdwgusajulalnftffsjxmjcvwksdusncyvcjynqfnmsvquspbgufbjaconqjffhxijvlumsvqtwfbjyfcvqjaryfcaiguuevufbjfjbcouezwsjknkwnacceugnjafcwysbxvdmscfepajcnsohjscbdvmvklpedswosjxstwfugvlynlfhxsduuwojnsdwnanqchxijajuczcsdavuuwnusgtswjkcfauedmmwmsxhnqcyjuuwrystfunwyjchxovqjnkvrvnexfcaczkwjeohjedmfgscnwdujmusntcuuwkfcafcvvmccceernkvzmstfuvqjbsyjenqjacffqcmayjevsdtxjjchwmsvqusnascueenkwzefhjmscuspuseoavefcxvdzwysbeycbeyfctsdzcceqjqsnebfzuuoyjetqfbstvqcumyjuhqjmueosvwdufyjhgfuwdfjgcbjusijasgxvnwxohvdcjgvwesaezwccfczwdusygusuuwwevqjymqsgcykoesvusepwkgueduvqjuusdznfjyjajcvtsyvqjajgkwvfcavvowtwruvsxhvqjonqsjxmcykszwccesduuwpwccvspwffcavvawvfsytswshvlheevuuwsuuwknksdufcaqsjnwojvswvlcecskcgcchovqjyjedmnvkwpefcjmfmxwctjfeegamqjctwfbjysccnkvnnjgvvwijsdzjbrhsoeusnksdunvpwrerwkbscjofcdwmxjynwgfushqmvlheyjdlskwhjvaccekcyfvlavorwnuuevsscxohvlhealnrhgedmcnryjqjcesdzoycmwvkmpsaqvwdzczjbjedmawvuuwbvoiwysbuspajcvbjezwkohszsxbjaneawvqcushetksjceanqsjxmdvvncyvtsyctjfmvkmnuuwjtwwhustnjemjcrenafvdedmmsnqfcabjusyjulydbjyjmfuunjynjcmjmpwvvhvpnxocafumvlhezfkjbsyjvrnsyvjdsvowvkqfafbryskjbjcvjdmjypoeefhgsdavylgvsscnasskwvjkceedmmwmwduscpvkwnbsvvqxovqccwvkasbjufbjijtsyjuuwdwmxjynwgxsiofcasivefcjmfgscvyfkeehvrnjyrhcujnkwnawvksvuuwwskavuuevqcmowjcnwjcfcvqjgsjdukofglunwzwkexvkccbjcvacceguwhlntsyvqjifhxamwmwduvvawvqjyvvojkhfcauscmqjyjsjrjglujmvqjfuvxwvvnevsntcgvssccceqjyjgjszweashcyawcalbwvkuuwmvklcavvowjccixweuuwkwoovvtwjnusnqjeeblguhscawkeovzwmevwkevilyxsdzvvdspeewcccgyjcsducchwmsvqpedoryfchsrexnjvrhjvwuuwryskfchwnwzwkexvwuuwpqcmowjccnrvfcvweiguuwcanwpixocgsbpsvujwvvcuvwdmvqjnkwnacceucljgcyjuuevcsbsyjifhxamwkwryfcvweuueduuwxemmfyjgvweuuwgfjyjuuwkwwvkwoovjkcngscnuccvhgffuujnedmawdwkexhgqjfuvcuvwdmjmoysjaqvffuuqfbctksjcevkumvwvkgsbredopopsdmuezsdzowjcpjhqpvkwfbryskeigyjeesdzvqcctwfbjynsnjrnsajsvfcawvkuuevyjenvdbggsczwkacufvdajwpmvvowpvkwzexjeuuwgqcmpwvvvqjskqsjnwnsdukvejhwebjusuuwfywyfwdmnedmnqsfebjblgugfkfhfugfusxwuwvqsuuwpenujymenexsvuxwdwahjgvwesdukjvquwmenedvemwsnqfzdvkedusthvpbscxswwwvdmstkjewxosnrvnsdzkwhwfkevrsdsscnaxvzwdhguswiukwcbeskufcjanwduujnscavshsdasbjnssdunvwyjhfzfvdedmchfuvhjldezsnqmsvqchmwhvdufclmvqjyjcjekuuyjwpvduuacceiguuevufbjshvlheyjgtvdepvdzpocgyjfyjmwyfwdmnxlmawchxwdacblwxilavsxhvqjajgkwvekostvqjnkvzsdgjsnecgrwcynvdxsajnugsvrwkedmnwzwkexvwuuwnbfuuapwpijynvwenajbohgedmfacehmjgsfvqjalyzwgvkzjcjychvqjhcuvwkfcacauyjfeaczcgfvlashebccmqsushebjuuevqjijzccwvkqfbnwxtmqjcgvlcaigfuwjhfcagxegtsyoyfgtbcljynhjekcjmvvmyfujewujyuwmenvweawhekyfmvqjguefcwvkalyzwgvkamqsucjaqvqfbnjkkjofcaedmuwueecsfoousnsdmlavygehdlskmczsvewnucujedmnegauwftsyjajwvqcugvlffhxasvdfsytuusnbccsjvvwqfaojnsdwnaccebcljewvkulcjsdsvevnusxeewxnuscqjqcmdvvuuwduuwxwcavsdufbcufvdvwbgsdujcvsscvvnwvjruuwkwsyccgfuwkwvqjajtksjceamwkwctvwkfcyeastayjevjnwvvpwcafvhgcafvdexhgfcavvnvpwstvqjbvqjochxgscvsdjjmvqjskyjzcyetsypwcaxvdzcavqjoxszweijtsyjsjcvwkjrvdbgnlixshernjekedgjsdilafcjansvbcoowmwxhvvxwvosjtcsfvqjuuwdavevwstpopsdmmsvqkwaekmvvporyfchsrhjaccebsychnuuevosjpegajwuvmtcyvqsajsdtxjjchmvqjtlulyjwzwdunvwbghftjbgncyjcvaueewcyxoaszwdbjyjhfzfvlafbryjansscnedmoysjaqvbjuuysjaqpohqfheqsvenfvlaxofcvqjmfanwdufcafcoojvsmenahekgjtftvwjcmqjcctvwkmsjoufcaigulydastnwzwkexnssdunenswvlceuuwpmfarjvwesduuweswtjyjcvisvtafyjeesowaedusmsjoustkwzwxevsscfunwxtnvpwovslneaefcnuewfaptjhxsdusbgqcceavqjomwkwnefmvvowvqjalinucchwstnwkbscnnkwcguweevisoxwnhjgvjkwnsvqcnrwdweuuevuuwgfkvlzuuccjtwwhuscpwyjfujgscvycygusfuevfcafcvwdmjmoovqjbwvkuuwcyajpwdunvwuuwewfavamqfgufjyjdlvvweusijyjtlujmcnrwcyjmvvpwpjhqnukvdzjyvqccvqjyjtlucufvdafcnqsyvsnvscowhepwcuuvkvlzumjsnupocyajpwdunnjyzwkujmnvpwsuuwkarekufglhcyxohvxhfcnedmkexnuilujehqstvqjbuezsdzctvwkfcyeamyscampwayjevhgffuuvluvqjhjenuhvpnlchufvdedmkwhvxhjgvsdztwfuuahvdmlgvusfcyeapwmqsfcaccsuuwktkwjuusdljyccebgvmcvvmekmnkjydvdedmpsnakwcmmqfguevufbjaaezwpwayjevukvlixwfijzccvvnjnnjgvuuevuusnmsgvyfcjuuvfupsaqvijukjjfcadvvkjygjnwwjxbghscevdncbrqxwvfushqueetsyfunbsuvvvqjajhfcjasteygmjcmqcujkjyfafaksaqvuuvlzunlyohfcebccnwjaojverekusuuwhqcsduuwdwcyjavhfctqfajojadvvgcykofcausuuwjdlexijepuuevnssnwnexhciskjedmwysbvqjevuksojvwnvwzsmusnsdtfcfujffaevpzsvecjanedmrvmwkgschhlmjmvqcudvvqfcagsjxmrvnafixoowmyscasduuwmvkheedmvqcuzshwccekfyvjjfjyjwpnvoesnufchufvdadvnjhqvqfcaajrfavsdzcnrwcyecsfdvvasgxwzwkerwktsypedgjensschwvqsjaqvsvedmfmsjoujmmqjuuwkasbjwkysyueecsufcnsdjcujmfunwxtlcrwkgjszmfcvvpocyajpwdunvcavvfcwwhuchxuuevtshxvmmcafahvpbscfcpwverqgafgchkwcascfcaavqjgkwjmstccjsaqvwjcvqhwdulyguuwshszfgchnwhumqfgufusxwowxsjkfcasdzsmkwwjnweusgkwesvuuwrvnafifhfugvwbfycgxwnedmvvcgtcsfxwezjuuwzexsesvostkwzwxevsscczkwcujcahfaunswvmkepevsnuccegksvshuuwxsdwnekwfccghjkevwxoyjsujmwysbeygmjcnvjmfnlacgvsfsngjcjsxsdwfzkwmgsczsdgeuuevukjvqnsdgjyfugedmfcvwayfugsdmjexsdznijumwjcpededmpedfjyjvwuuwlupvnufbrvkucchwvvvqjtjhfgfugvwhftjedmftsypmmyfuvwdyjashlufvdamqfguavsxhkwpefcfcpobvlydexisvtusnkehufgjuuwpwzwkfusxwfhfkjmkwzwxevsscueesdmjwecsfjsaqvffuubjenalguilufwdujyvefceedvrsdsscvqcuvqsjaqhwkucsdehufvdapsaqvcsuowoeeijgcjnwvqjomwkwwvkifmewdigsvvkzsveijgcjnwfuhvpbcceweuuwpojurysicixovqjajehufvdapsaqvijtsyosemjcowhelajuuwgfjyjicmwvkjnvkgsbpedmjmowhelajuuwgfjyjijcjtfgfexusjnsduuwfysfdcculyjachxuuwhskglbnucchwnvwuusdzngscnsewkweedmvqfarwkalensscmsvqvqjlfceqccevwnkvzsewdgjvkasbjzlekmfededzjhsycghsewduchwezvlycixwhskglbnucchwnedmnsvjcufvdasychxuszjuuwknkwnwkkjmpwvqkvvqfaeedzjysjnufbjvwosjvqcceuuwueqekmsjnafulevsscnsmenasbjufbjafccbscaavyccawkakwpvvwwysbvqjwgwcceeekfgjvwbgtcuuwkffuuvluccgffhxtlhaysanspbsychfugvksdxlavshwvqcupsaqvqckjijwdwinjgvwetkvpbgfccvvwyjhfzfvdsnegffhxtlhowhelajuuwfcnucchwnsuezwpwdufvdweqcmnvpwvqfcavwcjgjansvofcvqjbwysbpogvluusdwinjyfwdgjedmvqjldezwkostsuuwkafqcmvqjyjtsyjevvxwkeohjguekehujyvvowasduuwmvkheffuuszexjjmfurysnjyxoccemjujypsdmvvryjajyzwfumwueecsuowjcxvdzkwvjkceusnusxeewxnuscijtsyjuuwdwmugnjacykszmwysbxvdmscmwnwvuxweffuuljspwkedmxwwuuspigqfahvdajcvijtsyjqjqjekmstfumwwvlceeuvlajusqfyjcjekuuwpekljucceusvtsvushjanwduuwkwdumqfgufcavqjcojvumwdugtsjknsjdmnegwcyvqssuezwnsdgjldvmcfuvvxwvtsynwzwdugfjusvtsduuvpenzsmwyjoczxeqsjycceqfawepsxomqsfjyjusncocgscnsewkeohjncyvvwsvusjnedmmwvvovcyeffuuuuwpfjqcmngcyhwsnjcjmsjkhjuvwkaccenlusjknkwnafcsyewkijtsyjzjvkzjqsjnwcccgyjcsducchwstpsdwoysjaqvehvlcvygbccvvlamqsbuwueebjufcvqjavyjwvsddlsksdzwvkeryfcvwkexhsjkgcaufcadvmwinjcewesduuwzeksjugvwncyvshjxekamwueeijwdvohfzjmvvrysglyjedmvqfahvlcvygbccntfkjausxhfcaaowfcavlywskavtkjfunedmhvpsdznvnwcasccixoaezwpwpvkwrhjenjkwvqccccggkvmcfqckjafchwjekcjmcceuuwaycufulmjswwxuvvmekmuvlajqcapeewpwstvwdbsyjyjeeovqccrwkqcnnsnqsjxmsuuwkffajqckjijwdusenafavosjdzowasdcjynuuwkwcyjgkvcljynsdwzwkohvlcvygexfconismfcasvakjfcnjhqcvdwvqjcxszwesdnusxeewxnuscerwkascstdvvwccjhewkhgbccmsvqcffajhsvtedmckjygzkezwpedcjystnnjetsdzusnccbjfcanepjjhpshlxwvqfaawduxwpedenukedzjyvvpwnusnvvdweegevbgmsvkedmcatwebjswsmenuuwgvlcabccmqsqcmxevwxosnjcjmccjfryfcvsdzuvlajijsdzccnfjyjmfcvqjewtfypevszwuwnefmuwmenasykowvkbjijgcjnwfumenedwinjcnszwlcewkuclfcaedmvqjwinjcnwmvlheijhsavtsyrqfhcmjhrqfemenensdlfcanxehwvqjnjvrhjexyjeeouextoedlkjrunvkcjekijsdznvchxernjekedgjavvvqjgscvycygalguencjfojfhesdznedmvqjyfajvwyjcvaowfcausqfahwkucsdldvmhjmawwexhcgfvlawvkuuwgfjyjsdtcgvepvdzvqjuusdznuuevfsjxmnvsckjfclacceqjzckjbjalgueewvefhstpsntsyvjdwncsfjrfavsdzsyvqcumwkwnvscvvjrfavuuevqjhjtvbjqchwbjhcchqshgqcmfldvmcuspijtsyjsjcaeawesduusnilafcjannkvoeohgsdwzwkauvlheqckjmscjsvuusnbcchvdufclweushfkjsduusnmjgcofcanxehwcceusmjgxefbfcvqjacbjavycsdyjtlafcatsypedogwcynusilocqsjnwvqjyjijgcjnwchxfcaavfcausmjavylgvssccceevhcavsueeuuwrhjenjkwstnwjsdzuspzfkjtfkjufbjacapjhqwvkvdwcauwpsaqvqckjisjaqvsvtsymqjcuwwskavijzccusngkvclfcasnqsjxmuezwpwdufvdweijtsyjuuevsduuwcjvjpcstvqjnkwhwesdzgwcyfqcmwvkbebsavvwbgsdzjcfvlacgyjcsducchwfcvvcgxjovwblulexspnkvzwpwdumqfgufcahexhjmvqjxlcvvmwpwvvdtkseegwzwdsdznuuwkjxwnuuevseyjflnkwyjfyjmvqcujkjygbjbowksdqfavjkcnqsjxmrysmlgjvdwsypvkwyjjyfwnvdedorvfcvvwbsychnnshfufgnvkcculychrqfhsasnuovvowesnglanmoovqjgsbredoccevdgjsduuyjwpvduuarysmlgjedmkwcmccjanegvwqfasfdfksvsdzscccgalibwhuuwrhjenwevlyewoevwnfjyjusijjdmjyvqjmfyjgvsscstcnkwnsewducceusijgscejhujmfcvqjafchwkwnnfyfustfcyjfygewujyvyluuffuuvluwvdmdwnawvkmfarjvwsyewnskwstzshusygedmvvryjkjcvfcypuuexhjrryjansscnvwnsafufkjcjansdvrsdsscnvkmfyjgvgscvycmfgvsscmwkwctvwkasbjufbjbcmjgscvycicceedmrysqfifujmlcewkapexhrwhjdscygnjcchvsja'''

POP_SIZE = 1000
MUT_RATE = 0.01
GENES = 'abcdefghijklmnopqrstuvwxyz'
def decrypt(ctext, key):
    # print(str(key))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d = {key[i] + key[j+26] : alphabet[i] + alphabet[j]
         for i in range(26)
         for j in range(26)}

    ptext = ''
    block = ''
    for i,c in enumerate(ctext):
        if c in alphabet:
            block += c
            if len(block) == 2:
                ptext += d[block]
                block = ''
    return ptext

# Adjusted bigram frequencies
bigram_frequencies = {
    "th": 3.882543, "he": 3.681391, "in": 2.283899, "er": 2.178042, "an": 2.140460,
    "re": 1.749394, "nd": 1.571977, "on": 1.418244, "en": 1.383239, "at": 1.335523,
    "ou": 1.285484, "ed": 1.275779, "ha": 1.274742, "to": 1.169655, "or": 1.151094,
    "it": 1.134891, "is": 1.109877, "hi": 1.092302, "es": 1.092301, "ng": 1.053385
}

# Adjusted trigram frequencies
trigram_frequencies = {
    "the": 3.508232, "and": 1.593878, "ing": 1.147042, "her": 0.822444, "hat": 0.650715,
    "his": 0.596748, "tha": 0.593593, "ere": 0.560594, "for": 0.555372, "ent": 0.530771,
    "ion": 0.506454, "ter": 0.461099, "was": 0.460487, "you": 0.437213, "ith": 0.431250,
    "ver": 0.430732, "all": 0.422758, "wit": 0.397290, "thi": 0.394796, "tio": 0.378058
}

# Adjusted quadrigram frequencies
quadrigram_frequencies = {
    "that": 0.761242, "ther": 0.604501, "with": 0.573866, "tion": 0.551919, "here": 0.374549,
    "ould": 0.369920, "ight": 0.309440, "have": 0.290544, "hich": 0.284292, "whic": 0.283826,
    "this": 0.276333, "thin": 0.270413, "they": 0.262421, "atio": 0.262386, "ever": 0.260695,
    "from": 0.258580, "ough": 0.253447, "were": 0.231089, "hing": 0.229944, "ment": 0.223347
}

impossible_bigrams = {
    "bk", "fq", "jc", "jt", "mj", "qh", "qx", "vj", "wz", "zh",
    "bq", "fv", "jd", "jv", "mq", "qj", "qy", "vk", "xb", "zj",
    "bx", "fx", "jf", "jw", "mx", "qk", "qz", "vm", "xg", "zn",
    "cb", "fz", "jg", "jx", "mz", "ql", "sx", "vn", "xj", "zq",
    "cf", "gq", "jh", "jy", "pq", "qm", "sz", "vp", "xk", "zr",
    "cg", "gv", "jk", "jz", "pv", "qn", "tq", "vq", "xv", "zs",
    "cj", "gx", "jl", "kq", "px", "qo", "tx", "vt", "xz", "zx",
    "cp", "hk", "jm", "kv", "qb", "qp", "vb", "vw", "yq",
    "cv", "hv", "jn", "kx", "qc", "qr", "vc", "vx", "yv",
    "cw", "hx", "jp", "kz", "qd", "qs", "vd", "vz", "yz",
    "cx", "hz", "jq", "lq", "qe", "qt", "vf", "wq", "zb",
    "dx", "iy", "jr", "lx", "qf", "qv", "vg", "wv", "zc",
    "fk", "jb", "js", "mg", "qg", "qw", "vh", "wx", "zg"
}

def swap(key, c1, c2):
    if(c1 != c2):
        x = list(key)
        i1 = x.index(c1)
        i2 = x.index(c2)
        x[i1] = c2
        x[i2]=c1
        return ''.join(x)
    else:
        return key

def generate_random_key():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shuffled_alphabet1 = ''.join(random.sample(alphabet, len(alphabet)))
    shuffled_alphabet2 = ''.join(random.sample(alphabet, len(alphabet)))
    return shuffled_alphabet1 + shuffled_alphabet2

def initialize_pop():
    population = [generate_random_key() for _ in range(POP_SIZE)]
    return population

def fix_duplicates(child):
    # Assume child has 26 characters (half a chromosome)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    child_list = list(child)
    seen = set()
    missing_chars = list(set(alphabet) - set(child_list))

    # Iterate through child to identify duplicates
    for i in range(len(child_list)):
        if child_list[i] in seen:
            # Replace duplicate with a missing character
            child_list[i] = missing_chars.pop(0)
        else:
            seen.add(child_list[i])

    return ''.join(child_list)

# Fix mutation function to maintain unique characters in both halves
def mutate(offspring, MUT_RATE):
    mutated_offspring = []
    for arr in offspring:
        alphabet1 = arr[0][:26]
        alphabet2 = arr[0][26:]
        for i in range(26):
            if random.random() < MUT_RATE:
                alphabet1 = swap(alphabet1, alphabet1[i], random.choice(GENES))
        for i in range(26):
            if random.random() < MUT_RATE:
                alphabet2 = swap(alphabet2, alphabet2[i], random.choice(GENES))
        mutated_offspring.append(alphabet1 + alphabet2)
    return mutated_offspring

def selection(population):
    # Sort by fitness score in descending order so higher scores are better
    sorted_chromo_pop = sorted(population, key=lambda x: x[1], reverse=True)
    return sorted_chromo_pop[:int(0.5 * POP_SIZE)]

def load_word_list(file_path):
    # Use a set to store words for O(1) lookup time
    word_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            word_set.add(line.strip())  # Remove newline characters and add to set
    return word_set

def fitness_cal(key, decrypted_text):
    score = 0
    # Weights for n-grams (you can adjust these as needed)
    bigram_weight = 0.5
    trigram_weight = 0.15
    quadrigram_weight = 0.25

    # Calculate score based on bigram frequencies
    for i in range(len(decrypted_text) - 1):
        bigram = decrypted_text[i:i + 2]
        if bigram in bigram_frequencies:
            score += bigram_frequencies[bigram] *100* bigram_weight

    # Calculate score based on trigram frequencies
    for i in range(len(decrypted_text) - 2):
        trigram = decrypted_text[i:i + 3]
        if trigram in trigram_frequencies:
            score += trigram_frequencies[trigram] *100* trigram_weight

    # Calculate score based on quadrigram frequencies
    for i in range(len(decrypted_text) - 3):
        quadrigram = decrypted_text[i:i + 4]
        if quadrigram in quadrigram_frequencies:
            score += quadrigram_frequencies[quadrigram] *100* quadrigram_weight

    # Load word list and add points for real words found
    word_list = load_word_list("C:\\Users\\Work\\OneDrive - O\'Leary Asphalt\\Desktop\\School\\Computer Security\\Project1\\wordlist.txt")
    for word in word_list:
        if word in decrypted_text:
            score += 1000

    # Apply penalty for impossible bigrams
    for i in range(len(decrypted_text) - 1):
        bigram = decrypted_text[i:i + 2]
        if bigram in impossible_bigrams:
            score -= 100

    return score


def replace(new_gen, population):
    # Combine the current population with the new generation
    combined_population = population + new_gen
    
    # Sort combined population by fitness score in descending order
    sorted_population = sorted(combined_population, key=lambda x: x[1], reverse=True)
    
    # Keep only the top POP_SIZE individuals
    return sorted_population[:POP_SIZE]

# Adjust main to use updated fitness_cal without returning decrypted_text
def main(ctext, max_generations=1000, desired_fitness=None):
    initial_population = initialize_pop()
    population = []
    generation = 1
    found = False
    for individual in initial_population:
        decrypted_text = decrypt(ctext, individual)
        ind = [individual, fitness_cal(individual,decrypted_text)]
        if ind not in population:
            population.append([individual, fitness_cal(individual,decrypted_text)])
        

    population = sorted(population, key=lambda x: x[1], reverse=True)

    while not found and generation <= max_generations:
        print(f'Generation {generation}: Best Score = {population[0][1]}')

        selected = selection(population)
        #Crossover goes here if it were to be applicable
        mutated = mutate(selected, MUT_RATE)

        new_gen = []
        for individual in mutated:
            ind = [individual, fitness_cal(individual,decrypted_text)]
            if ind not in new_gen and ind not in population:
                decrypted_text = decrypt(ctext, individual)
                new_gen.append([individual, fitness_cal(individual,decrypted_text)])
            
        population = replace(new_gen,population)
        population = sorted(population, key=lambda x: x[1], reverse=True)

        if desired_fitness and population[0][1] >= desired_fitness:
            print('Desired fitness achieved.')
            found = True

        print(f'Best Decryption Key: {population[0][0]}, Fitness: {population[0][1]}')
        generation += 1

    print(f'Best decryption result after {generation-1} generations:')
    print(f'Decryption Key: {population[0][0]}, Fitness Score: {population[0][1]}')

main(c9)
