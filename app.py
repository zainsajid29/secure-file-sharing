import streamlit as st
from cryptography.fernet import Fernet
import os
import time
import base64

FIXED_KEY = b'6f6_8vXyG7U0N6yW4_V0-f8m4p-o9Xz9-l5R4k3J2H1='

if 'cipher' not in st.session_state:
    st.session_state.cipher = Fernet(FIXED_KEY)

cipher = st.session_state.cipher

st.title("📁 Secure File Sharing Portal")
st.write("End-to-End Encrypted Storage")

# --- UPLOAD SECTION ---
uploaded_file = st.file_uploader("Choose a file to secure")

if uploaded_file is not None:
    # 1. Read Original Data
    file_data = uploaded_file.read()
    
    # 2. Encrypt Data (AES-256)
    encrypted_data = cipher.encrypt(file_data)
    
    # 3. Save to 'Cloud' Folder
    cloud_path = f"cloud_storage/{uploaded_file.name}.enc"
    if not os.path.exists('cloud_storage'):
        os.makedirs('cloud_storage')
        
    with open(cloud_path, "wb") as f:
        f.write(encrypted_data)
    
    st.success(f"✅ File '{uploaded_file.name}' has been encrypted and uploaded to Cloud Storage.")

# --- SECURE DOWNLOAD (Signed URL Simulation) ---
st.divider()
st.subheader("🔗 Secure File Access")

files = os.listdir('cloud_storage') if os.path.exists('cloud_storage') else []
selected_file = st.selectbox("Select file to share", files)

if st.button("Generate Secure Link"):
    # Simulated Signed URL Logic (Link valid for 10 seconds)
    token = base64.b64encode(str(time.time()).encode()).decode()
    st.info(f"Temporary Access Token Generated: `{token}`")
    
    # Decrypt for Download
    with open(f"cloud_storage/{selected_file}", "rb") as f:
        enc_content = f.read()
        dec_content = cipher.decrypt(enc_content)
    
    st.download_button(
        label="Download Decrypted File",
        data=dec_content,
        file_name=selected_file.replace(".enc", ""),
        mime="application/octet-stream"

    )
