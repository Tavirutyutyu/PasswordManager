Here’s your updated README with a **"Getting Started"** section:  

# 🔑 Password Manager  

A simple password manager written in Python. I wrote this program from scratch to improve my Python skills.  

## 🚀 Technologies Used  
- 🐍 Python  
- 🖥️ Tkinter (GUI)  
- 📊 Pandas  
- 🔐 Cryptography  

## 🛠 How It Works  
### 🔓 Master Password  
The default master password is **`masterpass`**. If you want to change it, follow these steps:  

1. **Delete** the `security.csv` file.  
2. **Start** the program. It will prompt you in the **terminal** to enter a new password.  
3. **Restart** the program. A new `security.csv` file will be created with:  
   - Your new master password  
   - A new encryption key  

⚠ **Caution:** Changing the security file means previously saved passwords **cannot** be used anymore because the encryption key has changed.  

---

## 🏁 Getting Started  
Follow these steps to install and run the Password Manager on your system.  

### ✅ Prerequisites  
Ensure you have **Python 3.x** installed. You can check by running:  
```sh
python --version
```
or  
```sh
python3 --version
```
If you don’t have Python installed, download it from [here](https://www.python.org/downloads/).  

### 📥 Installation  
1. **Clone the Repository:**  
```sh
git clone https://github.com/your-username/password-manager.git
cd password-manager
```

2. **Install Dependencies:**  
```sh
pip install -r requirements.txt
```

### ▶ Running the Program  
Run the following command in the terminal:  
```sh
python main.py
```
or (if `python` points to Python 2 on your system):  
```sh
python3 main.py
```
