**Date:** 2nd November 2025
**Target:** Innovatech File Viewer
**Vulnerability:** Trojan Horse

---

## 🕵️ Vulnerability Analysis
By programming a trojan horse in python and moving the file into the directory, I gain access to the data in `secret_data.txt`

## 👨‍💻 Exploitation Steps

1. Create a `.txt` file
2. Write the file cloning code in Python in it
```
import os
import shutil

with open('stolen_data.txt', 'x') as f:
    shutil.copyfile('files\welcome.txt', 'stolen_data.txt')
```
3. Convert the file into a python file
4. Move it into the directory and run the file
5. Copy the contents of the cloned file and XOR it with the plaintext.
6. Create another `.txt` file   
7. Write the trojan code in Python in it
```
import os
import shutil

key = "slurp"

def decrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def view_file(filename):
    with open(filename, 'r') as f:
        encrypted_content = f.read()
    decrypted_content = decrypt(encrypted_content, key=key)
    print(decrypted_content)

view_file('secret_data.txt')
```
The encryption used on the file is a XOR encryption. By testing with a decoy fille added into `files\`, I managed to get the encrypted version of some text. Then by manually XORing the values, I deciphered the key. You can also program decrypters for it but I preferred the manual method.

8. Convert the file into a python file.
9. Execute the trojan code.

## 📃 Proof of Compromise

Contents of `secret_data.txt` are - 
```
Slurpy burpy boo :b
```