📁 Secure File Sharing System (Assignment 4)

Overview

This project is a part of my Cyber Security Internship at internee.pk. The objective was to build a secure portal that ensures end-to-end encrypted file exchanges between internal and external parties, simulating cloud storage security standards. 

Technical Features

End-to-End Encryption: All uploaded files are encrypted "at rest" using AES-256 (Fernet) logic to prevent unauthorized access. 


Virtual Cloud Storage: Implements a simulated cloud bucket system where files are stored in an unreadable, encrypted format. 


Secure Access Tokens: Generates temporary access signatures (Signed URL simulation) to control file downloads. 


Streamlit Integration: A user-friendly web interface for seamless uploading and secure downloading. 

How It Works
Identity Verification: User logs in through a secure gateway.

Encryption: When a file is selected, the system reads the binary data and encrypts it using a unique key before saving it to the storage folder.

Secure Retrieval: Files can only be decrypted and downloaded by authorized users through the portal's secure link generator.

Tech Stack
Language: Python

Framework: Streamlit

Security Library: Cryptography (Fernet)

Deployment: Streamlit Cloud
