from collections import Counter
import re

# English letter frequencies
ENGLISH_FREQ = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

def analyze_and_decrypt(cipher_text, cipher_name, manual_adjustments=None):
    clean_text = re.sub(r'[^a-zA-Z]', '', cipher_text.upper())
    freq_count = Counter(clean_text)
    total = len(clean_text)
    
    cipher_sorted = sorted(freq_count.items(), key=lambda x: x[1], reverse=True)
    for letter, count in cipher_sorted:
        percent = (count/total) * 100
        print(f"    {letter}       →    {count:3d}    →   {percent:5.1f}%")
    
    # Create initial substitution key
    key = {}
    for i, cipher_letter in enumerate(cipher_sorted):
        
            key[cipher_letter] = ENGLISH_FREQ[i]
    
    # Apply manual adjustments if provided
    if manual_adjustments:
       
        for cipher_char, plain_char in manual_adjustments.items():
            key[cipher_char] = plain_char
    
    # Apply substitution
    decrypted = ""
    for char in cipher_text:
        if char.upper() in key:
            decrypted += key[char.upper()].lower() if char.islower() else key[char.upper()]
        else:
            decrypted += char
    
    print(f"\nDECRYPTED TEXT:")
    
    print(decrypted)
    
    return len(clean_text)

# Your new cipher text (Cipher-2)
cipher1 = """af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki 
afgarxifrphni cd eao- -wvmd popkwn, hiqpvri du ear jvaql vfgikrcpfgafm 
du cei xkafqaxnir du xrwqedearcdkw pfg  du ear aopmafpcasi xkdhafmr
 afcd fit pkipr. ac tpr qdoudkcafm cd lfdt cepc au pfwceafm  epxxifig 
cd ringdf eaorinu hiudki cei opceiopcaqr du cei uaing qdvng hi 
qdoxnicinw tdklig dvc- -pfg edt rndtnw ac xkdqiigig, pfg edt
odvfcpafdvr cei dhrcpqnir--ceiki tdvng pc niprc kiopaf dfi  mddg oafg cepc tdvng qdfcafvi
cei kiripkqe """
cipher2 = """aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv  
zcbkg guovz, upuv zcmdu lcz vuwovroaeu jczoyyuovomdu omj qmubyudkuj vukqvm. klu  
vcdluz lu loj avhqnlk aodr svhw lcz kvopuez loj mht audhwu o ehdoe eunumj, omj ck toz  
yhyqeoveg auecupuj, tlokupuv klu hej sher wcnlk zog, klok klu lcee ok aon umj toz sqee hs  
kqmmuez zkqssuj tckl kvuozqvu. omj cs klok toz mhk umhqnl shv sowu, kluvu toz oezh lcz  
yvhehmnuj pcnhqv kh wovpue ok. kcwu thvu hm, aqk ck zuuwuj kh lopu eckkeu ussudk hm  
wv. aonncmz. ok mcmukg lu toz wqdl klu zowu oz ok scskg. ok mcmukg-mcmu klug aunom kh  
doee lcw tuee-yvuzuvpuj; aqk qmdlomnuj thqej lopu auum muovuv klu wovr. kluvu tuvu zhwu  
klok zlhhr klucv luojz omj klhqnlk klcz toz khh wqdl hs o nhhj klcmn; ck zuuwuj qmsocv klok  
omghmu zlhqej yhzzuzz (oyyovumkeg) yuvyukqoe ghqkl oz tuee oz (vuyqkujeg) cmubloqzkcaeu tuoekl. ck tcee lopu kh au yocj shv, klug zocj. ck czm'k mokqvoe, omj kvhqaeu  
which was little more than a commercial.  
tcee dhwu hs ck! aqk zh sov kvhqaeu loj mhk dhwu; omj oz wv. aonncmz toz numuvhqz tckl  
lcz whmug, whzk yuhyeu tuvu tceecmn kh shvncpu lcw lcz hjjckcuz omj lcz nhhj shvkqmu. lu  
vuwocmuj hm pczckcmn kuvwz tckl lcz vueokcpuz (ubduyk, hs dhqvzu, klu zodrpceeu  
aonncmzuz), omj lu loj womg juphkuj ojwcvuvz owhmn klu lhaackz hs yhhv omj  
qmcwyhvkomk sowcecuz. aqk lu loj mh dehzu svcumjz, qmkce zhwu hs lcz ghqmnuv dhqzcmz  
aunom kh nvht qy. klu uejuzk hs kluzu, omj aceah'z sophqvcku, toz ghqmn svhjh aonncmz.  
tlum aceah toz mcmukg-mcmu lu ojhykuj svhjh oz lcz lucv, omj avhqnlk lcw kh ecpu ok aon  
umj; omj klu lhyuz hs klu zodrpceeu- aonncmzuz tuvu scmoeeg jozluj. aceah omj svhjh  
loyyumuj kh lopu klu zowu acvkljog, zuykuwauv 22mj. ghq loj aukkuv dhwu omj ecpu luvu,  
svhjh wg eoj, zocj aceah hmu jog; omj klum tu dom dueuavoku hqv acvkljog-yovkcuz  
dhwshvkoaeg khnukluv. ok klok kcwu svhjh toz zkcee cm lcz ktuumz, oz klu lhaackz doeeuj klu  
cvvuzyhmzcaeu ktumkcuz auktuum dlcejlhhj omj dhwcmn hs onu ok klcvkg-klvuu"""

# Manual adjustments for Cipher-2
# Based on pattern analysis: "klu" appears very often (likely "the")
adjustments1 = {
    'C': 'T',  # cei -> the
    'E': 'H',  # cei -> the  
    'I': 'E',  # cei -> the
    'D': 'O',  # du -> of, cd -> to
    'U': 'F',  # du -> of
    'P': 'A',  # pfg -> and
    'F': 'N',  # pfg -> and, af -> in
    'G': 'D',  # pfg -> and
    'A': 'I',  # af -> in, ac -> it
    'T': 'W',  # tpr -> was
    'R': 'S',  # tpr -> was, ear -> his
    'O': 'M',  # eao -> him
    'Q': 'C',  # frequency based
    'V': 'U',  # frequency based
    'N': 'L',  # frequency based
    'K': 'R',  # frequency based
    'L': 'K',  # frequency based
    'W': 'Y',  # frequency based
    'H': 'B',  # frequency based
    'Y': 'H',  # yugo -> Hugo (proper name)
    'J': 'Q',  # juick -> quick
    'M': 'G',  # frequency based
    'S': 'V',  # less common
    'B': 'V',  # frequency based
    'X': 'P',  # frequency based
     'Z': 'V'   # imaginatize -> imaginative
}
adjustments2 = {
    'K': 'T',  # klu -> the
    'L': 'H',  # klu -> the  
    'U': 'E',  # klu -> the
    'O': 'A',  # common vowel (omj -> and)
    'M': 'N',  # omj -> and
    'J': 'D',  # omj -> and
    'Z': 'S',  # toz -> was
    'T': 'W',  # toz -> was
    'H': 'O',  # hs -> of
    'S': 'F',  # hs -> of
    'C': 'I',  # ck -> it
    'R': 'K',  # vcdl -> rich
    'V': 'R',  # vcdl -> rich
    'D': 'C',  # vcdl -> rich
    'A': 'B',  # aceah -> bilbo
    'E': 'L',  # aceah -> bilbo
    'P': 'V',  # puvg -> very
    'G': 'Y',  # puvg -> very
    'Q': 'U',  # qmubyudkuj -> unexpected
    'B': 'X',  # qmubyudkuj -> unexpected
    'Y': 'P',  # yudqecov -> peculiar
    'N': 'G',  # nhhj -> good
    'W': 'M',  # wqdl -> much
    'I': 'K',  # kcwu -> time
    'F': 'Q',  # less common
    'X': 'J',  # less common
    'I': 'K'   # final mapping
}

# Analyze the cipher
length2 = analyze_and_decrypt(cipher2, "CIPHER-2", adjustments2)
length1 = analyze_and_decrypt(cipher1, "CIPHER-2", adjustments1)
# Summary
print(f"\n{'='*50}")
print("SUMMARY")
print('='*50)
print(f"Cipher-2 length: {length1} letters")
print(f"\nKey patterns identified:")
print(f"• 'KLU' → 'THE' (most frequent 3-letter word)")
print(f"• 'OMJ' → 'AND' (common conjunction)")
print(f"• 'TOZ' → 'WAS' (common past tense verb)")
print(f"• 'HS' → 'OF' (common preposition)")
print(f"• 'CK' → 'IT' (common pronoun)")
print(f"• Manual adjustments improve readability significantly")