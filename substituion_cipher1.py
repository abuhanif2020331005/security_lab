from collections import Counter
import re

# Step 1: Frequency Analysis with percentage
def frequency_analysis(ciphertext):
    cleaned_text = re.sub(r'[^a-z]', '', ciphertext.lower())
    total_chars = len(cleaned_text)
    freq = Counter(cleaned_text)
    freq_percent = [(char, count, (count / total_chars) * 100) for char, count in freq.items()]
    return sorted(freq_percent, key=lambda x: x[1], reverse=True)  # sort by count descending

# Step 2: Decrypt using substitution map
def apply_substitution(ciphertext, sub_map):
    result = ''
    for char in ciphertext:
        if char.isalpha():
            result += sub_map.get(char.lower(), '_')  # fallback to '_' for unmapped
        else:
            result += char
    return result

# Ciphertext
cipher1 = """cz uczsdj qv lcf day vjqyq vdos ws kwz icwavgo ygsm sq zcm fqqy-lmd sq skd fgdzsz. 
jguqgjz qv zsjcafd dedasz kcy lm aqn zijdcy coo qedj skd vwdoy, lgs vjqyq nqgoy qaom zcm aq 
yqgls dedjmskwaf nwoo ld todcjdy gi wa skd uqjawaf. clqgs uwyawfks tcjjwcfdz tcud vqj skd 
wuiqjscas vqox. qad lm qad skdm jqoody cncm, vwoody nwsk vgoo lgs edjm gazcswzvwdy 
kqllwsz. fcjydadjz tcud lm cjjcafdudas, cay jduqedy wa nkddo-lcjjqnz skqzd skcs kcy 
wacyedjsdasom jducwady ldkway. awfks zoqnom"""

# Sample mapping
substitution_map = {
    's': 't',
    'k': 'h',
    'd': 'e',
    'q': 'o',
    'v': 'f',
    'w': 'i',
    'a': 'n',
    'c': 'a',
    'y': 'd',
    'g': 'u',
    'j': 'r',
    'u': 'm',
    'l': 'b',
    'e': 'v',
    'f': 'g',
    'n': 'w',
    't': 'c',
    'm': 'y',
    'i': 'p',
    'o': 'l',
    'p': 'k',
    'b': 'z',
    'x': 'x',
    'h': 'j',
    'r':'q',
    'z':'s'
}

# === Output ===

print("🔍 Letter Frequency Analysis (with percentages):")
freq_result = frequency_analysis(cipher1)
for letter, count, percent in freq_result:
    print(f"{letter}: {count} ({percent:.2f}%)")

print("\n🔓 Decrypted Cipher:")
print(apply_substitution(cipher1, substitution_map))
