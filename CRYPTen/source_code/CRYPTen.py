# Imports for the project
import pyAesCrypt
import glob
import os

# Encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

# Get current directory
curDir = os.getcwd()

# Prompt user for password to encrypt files
password1 = input('\n> Enter password to encrypt: ')
 
print('\n> Beginning recursive encryption...\n\n')

# Main loop to encrypt all files recursively
for x in glob.glob('crypting_files\\**\*', recursive=True):
    fullpath = os.path.join(curDir, x)
    fullnewf = os.path.join(curDir, x + '.en')
    # Encrypt
    if os.path.isfile(fullpath):
        print('>>> Original: \t' + fullpath + '')
        print('>>> Encrypted: \t' + fullnewf + '\n')
        pyAesCrypt.encryptFile(fullpath, fullnewf, password1, bufferSize)
        # Remove file after encryption
        os.remove(fullpath)

input("\nYou can close this window..")

#Thanks to YouTube channel "CodeOnBy" with a help for the project
#His YouTube: https://www.youtube.com/@CodeOnBy
#His Web-Site: https://codeonby.com

#Code by W0rning
#Git-Hub: https://github.com/W0rning