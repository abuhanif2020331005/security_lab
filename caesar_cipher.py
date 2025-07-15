#bruteforce approach
def decrytp_cipher(ciphertext,shift):
     result=""
     for char in ciphertext:
          if char.isalpha():
                base=ord('a')
                result+=chr((ord(char)-base-shift)%26 +base)
          else:
               result+=char
     return result    

cipher ="odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo"
for shift in range(26):
     print(f"Shift {shift}: {decrytp_cipher(cipher, shift)}")
                   
