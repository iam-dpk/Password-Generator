# 🔐 Password Generator

A secure, customizable Python desktop password generator using `secrets` and Tkinter.

## ✨ Features
- Secure random passwords with Python `secrets`
- Length 4–128 characters
- Uppercase, lowercase, numbers and symbols
- Strength indicator
- Copy to clipboard
- Show/hide password
- Local-only generation
- Automated tests

## 🛠️ Tech Stack
**Python • Tkinter • Secrets • PyTest**

## 🏗️ Architecture
```text
User Options → Secure Generator → Strength Analyzer → Desktop GUI → Clipboard
```

## 📂 Structure
```text
Password-Generator/
├── app.py
├── run.bat
├── requirements.txt
├── README.md
├── src/
├── gui/
├── tests/
└── assets/screenshots/
```

## 🚀 Run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Windows: double-click `run.bat`.

## 🧪 Tests
```bash
pytest -q
```

## 📸 Screenshots
Add images to `assets/screenshots/` and reference them here:
```markdown
![Main Window](assets/screenshots/main-window.png)
```

## 🔐 Security
Passwords are generated locally with Python's `secrets` module and are not uploaded or stored by this application. For important accounts, use a reputable password manager.

## 🔮 Future Improvements
- Passphrase generator
- Entropy estimation
- Theme switch
- Password policy presets
- Optional encrypted local vault
- Windows `.exe` packaging

## 👨‍💻 Portfolio Project
Demonstrates Python, secure random generation, GUI development, validation, security concepts and automated testing.

⭐ If you like it, star the repository.
