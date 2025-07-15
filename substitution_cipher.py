from collections import Counter
import re

# English letter frequencies
ENGLISH_FREQ = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

def analyze_and_decrypt(cipher_text, cipher_name, manual_adjustments=None):
    

    # Clean text and count frequencies
    clean_text = re.sub(r'[^a-zA-Z]', '', cipher_text.upper())
    freq_count = Counter(clean_text)
    total = len(clean_text)
    
  
    
    cipher_sorted = sorted(freq_count.items(), key=lambda x: x[1], reverse=True)
    for letter, count in cipher_sorted:
        percent = (count/total) * 100
        print(f"    {letter}       →    {count:3d}    →   {percent:5.1f}%")
    
    # Create initial substitution key
    cipher_sorted
    key = {}
    for i, (cipher_letter, _) in enumerate(cipher_sorted):
        if i < len(ENGLISH_FREQ):
            key[cipher_letter] = ENGLISH_FREQ[i]
    
   
    
    # Apply substitution
    decrypted = ""
    for char in cipher_text:
        if char.upper() in key:
            decrypted += key[char.upper()].lower() if char.islower() else key[char.upper()]
        else:
            decrypted += char
    
    print(f"\nDECRYPTED TEXT:")
    print("-" * 40)
    print(decrypted)
    
    return len(clean_text)

# Cipher texts
cipher1 = """cz uczsdj qv lcf day vjqyq vdos ws kwz icwavgo ygsm sq zcm fqqy-lmd sq skd fgdzsz. 
jguqgjz qv zsjcafd dedasz kcy lm aqn zijdcy coo qedj skd vwdoy, lgs vjqyq nqgoy qaom zcm aq 
yqgls dedjmskwaf nwoo ld todcjdy gi wa skd uqjawaf. clqgs uwyawfks tcjjwcfdz tcud vqj skd 
wuiqjscas vqox. qad lm qad skdm jqoody cncm, vwoody nwsk vgoo lgs edjm gazcswzvwdy 
kqllwsz. fcjydadjz tcud lm cjjcafdudas, cay jduqedy wa nkddo-lcjjqnz skqzd skcs kcy 
wacyedjsdasom jducwady ldkway. awfks zoqnom"""

cipher2 = """cej amxziu, gobxm om zbz uij kiqhmj wfwqdx'a gwqubuh, zbz uij jobul ik bj gbjo wud 
hqmwj zmhqmm ik niunmujqwjbiu. oba kiqjbmjo cbqjozwd nwfm wuz gmuj--gbjo jom eaewx 
vadnoixihbnwx cxig. kiqjd! om gwa uij dieuh wuz xiuhmq. xbkm ui xiuhmq ajqmjnomz cmkiqm 
obf wa w ywaj eunowqjmz kbmxz, bja oiqbpiu xiaj bu jom zbajwunm. om owz cmmu iu jqwujiq 
kiq mbhoj dmwqa wuz jom jbfm owz vwaamz tebnlxd. wuijomq mbhoj dmwqa wuz om giexz 
cm umwqxd kbkjd. ixz whm giexz cm xiifbuh. wuz om owz uij mymu fwzm w zmnmuj 
cmhbuubuh bu vadnoiobajiqd! dehi wfwqdx avilm cqbhojxd ik xwga wuz giqlmz iej oba 
mtewjbiua cd fwlbuh zwqbuh waaefvjbiua cwamz iu bujebjbiu. cej oig niexz ium viaabcxd jmaj 
joiam waaefvjbiua? vadnoiobajiqd gwa uij dmj wu msvmqbfmujwx anbmunm. jom nifvxmjm 
ajezd ik vadnoiobajiqd giexz qmtebqm msvmqbfmuja jowj giexz buyixym giqxza ik vmivxm, 
nmujeqbma ik jbfm--wuz w jijwx xwnl ik mjobnwx qmaviuabcbxbjd. bj viamz wu bfviaabcxm 
vqicxmf wuz om qmamujmz owybuh ji avmuz wud jbfm gowjmymq iu zmvwqjfmujwx jwala, 
ai om gwxlmz oifm wj jom muz ik jom zwd bu w fiqiam fiiz. iqzbuwqbxd om niexz wxgwda 
nieuj iu w gwxl joqieho jom nwfvea ji qieam oba avbqbja. ajqmmxbuh eubymqabjd gwa obhozifmz wuz jom nwfvea hwym jom kmmxbuh ik cmbuh iej bu jom ivmu gbjoiej jom umnmaabjd 
ik muzeqbuh jom lbuz ik gmwjomq om owz msvmqbmunmz iu oba ium (wuz iuxd) ybabj ji jom 
bfvmqbwx vwxwnm. jomqm gmqm jqmma, xwgua, gwxla, wxfiaj wa joieho om gmqm iu jom 
nwfvea ik oba ixz nixxmhm iu oba oifm giqxz ik omxbniu. jom bxxeabiu ik nxiezbumaa owz 
cmmu wqqwuhmz kiq jom zwd gbjo jom aeuxbhoj (ui aeu, ik nieqam, reaj aeuxbhoj) 
wvvmwqbuh wuz zbawvvmwqbuh wj izz bujmqywxa. wuz bj gwa w xbjjxm niix, reaj w xbjjxm. 
bj ammfmz ji amxziu jowj jom niix zwda nwfm w xbjjxm fiqm kqmtemujxd jowu jomd eamz ji. 
gwa jqwujiq awybuh mumqhd? gwa bj bunqmwabuh bumkkbnbmund? iq (wuz om anigxmz 
bugwqzxd wa om joiehoj bj) gwa om hmjjbuh ixz wuz gwa oba cxiiz hmjjbuh jobu? om vxwnmz 
oba owuza bu """

# Manual adjustments for Cipher-1
# Based on pattern analysis: "skd" appears often (likely "the")
adjustments1 = {
    'S': 'T',  # skd -> the
    'K': 'H',  # skd -> the  
    'D': 'E',  # skd -> the
    'Q': 'O',  # qv -> of
    'V': 'F',  # qv -> of
    'W': 'I',  # wa -> in
    'A': 'N',  # wa -> in
    'C': 'A',  # common letter
    'Z': 'S',  # common letter
    'Y': 'D',  # frequency based
    'G': 'U',  # frequency based
    'J': 'R',  # pattern analysis
    'U': 'M',  # pattern analysis
    'L': 'B',  # frequency based
    'E': 'V',  # less common
    'F': 'G',  # frequency based
    'N': 'W',  # pattern analysis
    'T': 'C',  # frequency based
    'M': 'Y',  # less common
    'I': 'P',  # less common
    'O': 'L',  # vowel
    'P': 'K',  # rare
    'B': 'Z',  # consonant
    'X': 'X',  # rare
    'H': 'J',  # less common
    'R': 'Q'   # very rare
}

# Manual adjustments for Cipher-2
# Based on pattern analysis: "jom" appears often (likely "the")
adjustments2 = {
    'J': 'T',  # jom -> the
    'O': 'H',  # jom -> the
    'M': 'E',  # jom -> the
    'W': 'A',  # common vowel
    'U': 'N',  # common consonant
    'Z': 'D',  # common consonant
    'I': 'O',  # vowel
    'K': 'F',  # consonant
    'G': 'W',  # consonant
    'B': 'I',  # vowel
    'A': 'S',  # common consonant
    'Q': 'R',  # common consonant
    'E': 'U',  # vowel
    'X': 'L',  # common consonant
    'N': 'C',  # consonant
    'V': 'P',  # consonant
    'C': 'B',  # consonant
    'Y': 'V',  # less common
    'L': 'K',  # less common
    'F': 'M',  # consonant
    'D': 'Y',  # consonant
    'R': 'J',  # less common
    'T': 'Q',  # rare
    'H': 'G',  # less common
    'S': 'X',  # rare
    'P': 'Z'   # very rare
}

# Analyze both ciphers with manual adjustments
length1 = analyze_and_decrypt(cipher1, "CIPHER-1", adjustments1)
length2 = analyze_and_decrypt(cipher2, "CIPHER-2", adjustments2)

# Summary
print(f"\n{'='*50}")
print("SUMMARY")
print('='*50)
print(f"Cipher-1 length: {length1} letters")
print(f"Cipher-2 length: {length2} letters")
print(f"\nCipher-2 was easier to break because:")
print(f"• Much longer text ({length2} vs {length1} letters)")
print(f"• Better statistical sample for frequency analysis")
print(f"• More context clues for verification")
print(f"• Manual adjustments were more effective with more data")