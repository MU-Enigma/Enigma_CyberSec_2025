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
from cryptography.fernet import Fernet
from key import key

def decrypt(text, key):
    f = Fernet(key)
    decrypted = f.decrypt(text.encode())
    return decrypted.decode()

def view_file(filename):
    with open(filename, 'r') as f:
        encrypted_content = f.read()
    decrypted_content = decrypt(encrypted_content, key=key)
    print(decrypted_content)

view_file('secret_data.txt')

```
3. Convert the file into a python file
4. Move it into the directory and run the file

## 📖 Explanation

This trojan works as `secret.key` had the key in it, giving me free access to the key and the files it encrypted. Using a trojan let me gain access to the parent file that I could not access from the file viewer due to the initial patches.

## 📃 Proof of Compromise

Contents of `secret_data.txt` are - 
```
heh all that effort for this??
```