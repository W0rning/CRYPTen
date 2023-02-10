# Imports for the project
import pyAesCrypt
import glob
import os

# Encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

# Get current directory
curDir = os.getcwd()

# Prompt user for password to decrypt files
password1 = input('\n> Enter password to decrypt: ')
 
print('\n> Beginning recursive decryption...\n\n')

# Main loop to decrypt all files recursively
for x in glob.glob('crypting_files\\**\*', recursive=True):
    fullpath = os.path.join(curDir, x)
    fullnewf = os.path.join(curDir, os.path.splitext(x)[0])
    # Decrypt
    if os.path.isfile(fullpath):
        print('>>> Encrypted: \t' + fullpath + '')
        try:
            pyAesCrypt.decryptFile(fullpath, fullnewf, password1, bufferSize)
            print('>>> Decrypted: \t' + fullnewf + '\n')
            os.remove(fullpath)     # Remove encrypted file after decrypt
        except ValueError:
            print('>>> Error - Wrong password!\n')

input("\nYou can close this window..")

#Thanks to YouTube channel "CodeOnBy" with a help for the project
#His YouTube: https://www.youtube.com/@CodeOnBy
#His Web-Site: https://codeonby.com

#Code by W0rning
#Git-Hub: https://github.com/W0rning