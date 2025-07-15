import re
from collections import Counter
import string
ENGLISH_FREQ = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7, 'S': 6.3, 'H': 6.1,
    'R': 6.0, 'D': 4.3, 'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4, 'F': 2.2,
    'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.3, 'V': 1.0, 'K': 0.8, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}

def analyze_frequency(text):
    """Analyze letter frequency in the given text"""
    # Remove spaces and convert to uppercase
    clean_text = re.sub(r'[^a-zA-Z]', '', text.upper())
    total_letters = len(clean_text)
    
    # Count frequency of each letter
    freq_count = Counter(clean_text)
    freq_percent = {letter: (count / total_letters) * 100 
                   for letter, count in freq_count.items()}
    
    return freq_percent, freq_count, total_letters

def create_substitution_key(cipher_freq, english_freq):
    """Create a substitution key based on frequency analysis"""
    # Sort cipher letters by frequency (descending)
    cipher_sorted = sorted(cipher_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Sort English letters by frequency (descending)
    english_sorted = sorted(english_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Create initial mapping
    key = {}
    for i, (cipher_letter, _) in enumerate(cipher_sorted):
        if i < len(english_sorted):
            key[cipher_letter] = english_sorted[i][0]
    
    return key

def apply_substitution(text, key):
    """Apply substitution key to decrypt text"""
    result = ""
    for char in text:
        if char.upper() in key:
            result += key[char.upper()]
        else:
            result += char
    return result

def manual_adjustments(key, adjustments):
    """Apply manual adjustments to the key"""
    new_key = key.copy()
    for cipher_char, plain_char in adjustments.items():
        new_key[cipher_char] = plain_char
    return new_key

def decipher_text(cipher_text, cipher_name):
    """Main function to decipher the text"""
    print(f"\n=== Analyzing {cipher_name} ===")
    
    # Analyze frequency
    freq_percent, freq_count, total_letters = analyze_frequency(cipher_text)
    
    print(f"Text length: {total_letters} letters")
    print("Top 10 most frequent letters in cipher:")
    sorted_freq = sorted(freq_percent.items(), key=lambda x: x[1], reverse=True)
    for letter, percent in sorted_freq[:10]:
        print(f"  {letter}: {percent:.1f}% ({freq_count[letter]} occurrences)")
    
    # Create initial substitution key
    initial_key = create_substitution_key(freq_percent, ENGLISH_FREQ)
    
    print("\nInitial substitution attempt:")
    initial_result = apply_substitution(cipher_text, initial_key)
    print(initial_result[:200] + "..." if len(initial_result) > 200 else initial_result)
    
    return initial_key, initial_result, freq_percent

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
oba owuza bu"""

# Analyze both ciphers
key1, result1, freq1 = decipher_text(cipher1, "Cipher-1")
key2, result2, freq2 = decipher_text(cipher2, "Cipher-2")

print("\n=== Manual Analysis and Refinement ===")

# For Cipher-1, let's make some manual adjustments based on common patterns
print("\nRefining Cipher-1:")
# Looking at patterns like "SKD" which appears frequently - likely "THE"
# "QV" pattern might be "OF"
# "WA" pattern might be "IN"
adjustments1 = {
    'S': 'T', 'K': 'H', 'D': 'E',  # SKD -> THE
    'Q': 'O', 'V': 'F',            # QV -> OF
    'W': 'I', 'A': 'N',            # WA -> IN
    'C': 'A', 'Z': 'S',            # Common letters
    'Y': 'D', 'G': 'U',            # Frequency-based
    'J': 'R', 'U': 'M',            # Based on patterns
    'L': 'B', 'E': 'V',            # Continuing analysis
    'F': 'G', 'N': 'W',            # More substitutions
    'T': 'C', 'M': 'Y',            # Additional mappings
    'I': 'P', 'O': 'L',            # Final adjustments
    'P': 'K', 'B': 'Z',            # Remaining letters
    'X': 'X', 'H': 'J',            # Less common letters
    'R': 'Q', 'L': 'B'             # Final mappings
}

refined_key1 = manual_adjustments(key1, adjustments1)
refined_result1 = apply_substitution(cipher1, refined_key1)
print("Refined result for Cipher-1:")
print(refined_result1[:1000] + "..." if len(refined_result1) > 300 else refined_result1)

# For Cipher-2, similar approach
print("\nRefining Cipher-2:")
adjustments2 = {
    'J': 'T', 'O': 'H', 'M': 'E',   # Common "JOM" -> "THE"
    'W': 'A', 'U': 'N', 'Z': 'D',   # Common patterns
    'I': 'O', 'K': 'F',             # Frequency analysis
    'G': 'W', 'B': 'I',             # More substitutions
    'A': 'S', 'Q': 'R',             # Continuing
    'E': 'U', 'X': 'L',             # Additional mappings
    'N': 'C', 'V': 'P',             # More letters
    'C': 'B', 'Y': 'V',             # Further refinement
    'L': 'K', 'F': 'M',             # Completing the key
    'D': 'Y', 'R': 'J',             # Final adjustments
    'T': 'Q', 'H': 'G',             # Remaining letters
    'S': 'X', 'P': 'Z'              # Last mappings
}

refined_key2 = manual_adjustments(key2, adjustments2)
refined_result2 = apply_substitution(cipher2, refined_key2)
print("Refined result for Cipher-2:")
print(refined_result2[:1000] + "..." if len(refined_result2) > 300 else refined_result2)

# # Analysis of difficulty
# print("\n=== Analysis of Difficulty ===")
# print(f"Cipher-1 length: {len(re.sub(r'[^a-zA-Z]', '', cipher1))} letters")
# print(f"Cipher-2 length: {len(re.sub(r'[^a-zA-Z]', '', cipher2))} letters")

# print("\nTop 5 letter frequencies comparison:")
# print("Cipher-1:")
# for letter, percent in sorted(freq1.items(), key=lambda x: x[1], reverse=True)[:5]:
#     print(f"  {letter}: {percent:.1f}%")

# print("Cipher-2:")
# for letter, percent in sorted(freq2.items(), key=lambda x: x[1], reverse=True)[:5]:
#     print(f"  {letter}: {percent:.1f}%")

# print("\nExpected English frequencies (top 5):")
# for letter, percent in sorted(ENGLISH_FREQ.items(), key=lambda x: x[1], reverse=True)[:5]:
#     print(f"  {letter}: {percent:.1f}%")