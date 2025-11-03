# Patch Report

**Date:** 3rd November 2025  
**Target:** Innovatech File Viewer  

---

## Vulnerability

The `secret_data.txt` file was stored in encrypted text using XOR encryption in the repository, so anyone with access to the files could read it by reverse tracing the key using plain text vulnerability.

**Problem:** Attackers could create Python scripts in the repo that open and read encrypted `secret_data.txt` directly and read its contents by finding its key :O

**Example:**
- Normal: Use the web app to view files (like a normal sweet hooman would)
- Attack: Write a Python script that does `open('secret_data.txt').read()` and steal the encrypted data and get the key to decrypt it and read its contents (like some bish ahh cunning hoomans would)

This Shouldn't Happen!! fk cunning hoomans

---

## The Patch

Encrypt the `secret_data.txt` using cryptography.fernet.

```python
def encrypt(text, key):
    f = Fernet(key)
    encrypted = f.encrypt(text.encode())
    return encrypted.decode()

def decrypt(text, key):
    f = Fernet(key)
    decrypted = f.decrypt(text.encode())
    return decrypted.decode()

KEY = secret.key file #this is not included in the repo
decrypted_data=decrypt(encrypte_content, KEY)
```

This encrypts the secret data. Even if attackers get the encrypted file, they can't read it without the KEY (which is NOT in the repo) hehehehe fk u charan.

---

**The vulnerability is now fixed! YAYYY**