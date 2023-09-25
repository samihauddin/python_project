
### What is SSH and Why Use It?
SSH (Secure Shell) is a secure way to communicate between computers over the internet. It has two main purposes:

**Remote Access:** You can use SSH to securely log into a remote computer and control it from afar.

**Secure File Transfer:** SSH allows you to transfer files between computers securely, ensuring that your data remains safe during the transfer.

### How SSH Works
SSH uses a pair of keys: a public key (shared openly) and a private key (kept secret). Here's how it works:

Your computer (the client) connects to another computer (the server) using SSH.

The server checks your public key to see if it recognizes you.

If it does, the server uses your public key to send an encrypted message back to your computer.

Your computer uses its private key to decrypt the message. If the decryption works, you gain access to the server.

### Public and Private Keys
SSH uses a pair of cryptographic keys, known as public key and private key, to authenticate users and establish secure connections:

**Public Key:** This key is meant to be shared openly and is stored on the SSH server. It serves as a lock, allowing anyone with the corresponding private key to unlock and access the server.

**Private Key:** This key is kept secret and should never be shared. It is stored on the client machine and is used to unlock the server. 

### Why Use SSH?
SSH is beneficial for 3 main reasons:

**Encryption**: All data transferred between the client and server is encrypted, protecting it from interception.

**Authentication**: Public-key cryptography ensures that only users with the correct private key can access the server.

**Secure Remote Access**: SSH provides secure remote access to servers, reducing the risk of unauthorized access and potential breaches.

### How can you create an SSH key pair?

To set up SSH, follow these steps:

1. Open a Terminal (Linux/Mac) or use an SSH client (like PuTTY on Windows). <br>


2. Generate your key pair with the `ssh-keygen -t rsa` command: Replace "your_email@example.com" with your email. <br>


3. Choose where to save the keys (usually ~/.ssh by default). <br>


4. You can add a passphrase for extra security (optional but recommended). <br>


5. Copy the public key (id_rsa.pub) to the server's ~/.ssh/authorized_keys file.