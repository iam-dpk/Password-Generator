# 🔐 Password Generator

<p align="center">
  <img src="assets/screenshots/main-window.png" width="700">
</p>

<h3 align="center">
Secure • Customizable • Offline Password Generator
</h3>

<p align="center">
A professional Python desktop application for generating strong passwords locally.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![Security](https://img.shields.io/badge/Security-secrets-green)
![Tests](https://img.shields.io/badge/Tests-Passing-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

---

## 🚀 About The Project -

**Password Generator** is a secure and customizable desktop application built with Python.

It generates strong random passwords based on user-selected requirements including length, uppercase letters, lowercase letters, numbers, and special characters.

The application also provides password-strength analysis and one-click clipboard copying.

🔒 **Everything runs locally — passwords are not uploaded or stored by the application.**

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 Secure Generation | Uses Python `secrets` |
| 🔢 Custom Length | 4–128 characters |
| 🔠 Uppercase | Optional A–Z |
| 🔡 Lowercase | Optional a–z |
| 🔢 Numbers | Optional 0–9 |
| 🔣 Special Characters | Custom symbol set |
| 📊 Strength Analysis | Weak → Very Strong |
| 📋 Copy | One-click clipboard |
| 👁️ Show/Hide | Toggle password visibility |
| 🖥️ Desktop GUI | Tkinter interface |
| 🧪 Testing | Automated PyTest tests |
| 🌐 Offline | No external API required |

---

## 🖥️ Application Preview

<p align="center">

<img width="1910" height="1023" alt="Screenshot 2026-09-27 091435" src="https://github.com/user-attachments/assets/c40ac21a-acc2-48b4-82d8-1eda616a4a34" />


  
</p>

<p align="center">


<img width="885" height="796" alt="Screenshot 2026-09-27 091419" src="https://github.com/user-attachments/assets/6d9d234c-4490-4664-a012-b7844612cffc" />

</p>

> 

---

## 🏗️ Architecture

```text
                    ┌───────────────────┐
                    │       USER        │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    Tkinter GUI    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Password Generator│
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Python `secrets`  │
                    │ Secure Generation │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Generated Password│
                    └─────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             ┌─────────────┐     ┌─────────────┐
             │   Strength  │     │  Clipboard  │
             │   Analyzer  │     │    Copy     │
             └─────────────┘     └─────────────┘






      # 🔄 How It Works

         User selects options
               ↓
         Password length selected
                ↓
         Character types selected
                ↓
         Secure password generated
                ↓
         Password strength analyzed
                ↓
         Password displayed
                ↓
        User can copy password




      # 🛠️ Technology Stack

🐍 Python

🖥️ Tkinter

🔐 Secrets

🔤 String

🧪 PyTest

🐙 Git / GitHub





   ⚙️ Installation

1. Clone

git clone https://github.com/iam-dpk/Password-Generator.git

2. Enter directory

cd Password-Generator

3. Create virtual environment

python -m venv .venv



4. Activate

Windows:

.venv\Scripts\activate

Linux/macOS:

source .venv/bin/activate

5. Install dependencies

pip install -r requirements.txt



▶️ Run

python app.py

Windows

You can also double-click:

run.bat

🧪 Testing

Run:

pytest -q

Expected result:

6 passed




🔐 Security

The application uses:

import secrets

The secrets module is designed for security-sensitive random generation.

Privacy

✅ Runs locally

✅ No account required

✅ No external API

✅ No password upload

✅ No default password storage

For important accounts, use a reputable password manager and enable multi-factor authentication.




🎯 Project Objectives

This project demonstrates:

Python development

Desktop GUI development

Secure random generation

Input validation

Password-strength analysis


Clipboard integration

Unit testing

Git/GitHub workflow




Basic cybersecurity concepts

🔮 Future Improvements

🔥 Passphrase generator

📊 Advanced entropy calculation

🎨 Dark/light themes

🔒 Optional encrypted password vault

📋 Password history

📦 Windows .exe version

🌐 Web version

🤖 AI-assisted security recommendations



| Component                | Status     |
| ------------------------ | ---------- |
| Password Generation      | ✅ Complete |
| Secure Random Generation | ✅ Complete |
| Strength Analyzer        | ✅ Complete |
| GUI                      | ✅ Complete |
| Clipboard                | ✅ Complete |
| Show/Hide Password       | ✅ Complete |
| Testing                  | ✅ Complete |
| Documentation            | ✅ Complete |





# 👨‍💻 Portfolio

This project is part of my software development portfolio.

Skills demonstrated

Python • GUI Development • Cybersecurity • Testing • Software Architecture • GitHub

# 🙏 Thank You

Thank you for visiting my project!

I'm continuously learning, building, and improving my software development skills through practical projects.

Keep Learning • Keep Building • Keep Growing 🚀

⭐ If you like this project, consider giving the repository a star.




  📬Connect

     GitHub:https://github.com/iam-dpk

     Portfolio:https://deepakshukla.online/

     LinkedIn:https://www.linkedin.com/in/dk-50s
