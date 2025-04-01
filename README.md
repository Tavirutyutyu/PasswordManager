# 🔑 Password Manager  

A simple password manager written in Python.  

## Technologies Used  
- 🐍 Python  
- 🖥️ Tkinter (GUI)  
- 📊 Pandas  
- 🔐 Cryptography  

## How It Works  
### Master Password  
The default master password is **`masterpass`**. If you want to change it, follow these steps:  

1. **Delete** the `security.csv` file.  
2. **Start** the program. It will prompt you in the **terminal** to enter a new password.  
3. **Restart** the program. A new `security.csv` file will be created with:  
   - Your new master password  
   - A new encryption key  

⚠ **Caution:** Changing the security file means previously saved passwords **cannot** be used anymore because the encryption key has changed.
