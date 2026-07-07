````markdown
# 🚀 AI Engineer Course Setup Guide

<div align="center">

### Everything you need before **Day 1**

**✅ Free • ✅ Windows • ✅ macOS • ✅ Beginner Friendly**

---

</div>

## 📋 Setup Checklist

Complete every step below before starting the course.

- [ ] Install Python 3.11
- [ ] Install Visual Studio Code
- [ ] Install Git
- [ ] Install UV Package Manager
- [ ] Install Windows Terminal *(Windows only)*
- [ ] Create a GitHub Account
- [ ] Create Groq API Key
- [ ] Create Gemini API Key
- [ ] Create OpenRouter API Key
- [ ] Create Qdrant Cloud Cluster
- [ ] Create your `.env` file
- [ ] Create Course Folder
- [ ] Verify Everything

---

# 🐍 Python 3.11

## 🪟 Windows

1. Visit:

   https://www.python.org/downloads/release/python-3119/

2. Download **Windows installer (64-bit)**

3. Run the installer.

4. **IMPORTANT:** Enable:

```text
✅ Add python.exe to PATH
```

5. Click **Install Now**.

6. Verify installation:

```powershell
python --version
```

Expected:

```text
Python 3.11.9
```

---

## 🍎 macOS

### Install Homebrew (if needed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Apple Silicon Macs

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile

eval "$(/opt/homebrew/bin/brew shellenv)"
```

### Install Python

```bash
brew install python@3.11
```

Verify:

```bash
python3.11 --version
```

Expected:

```text
Python 3.11.x
```

---

# 💻 Visual Studio Code

## 🪟 Windows

Download:

https://code.visualstudio.com/download

During installation select **all** Additional Tasks.

### Install Extensions

- Python
- Pylance
- Jupyter

(All by Microsoft)

---

## 🍎 macOS

Download:

https://code.visualstudio.com/download

1. Extract the ZIP.
2. Drag **Visual Studio Code.app** into **Applications**.
3. Open VS Code.
4. Press:

```text
Cmd + Shift + P
```

Run:

```text
Shell Command: Install 'code' command in PATH
```

Install Extensions:

- Python
- Pylance
- Jupyter

---

# 🌳 Git

## 🪟 Windows

Download:

https://git-scm.com/download/win

Accept all default installation settings.

Verify:

```bash
git --version
```

Configure Git:

```bash
git config --global user.name "Your Name"

git config --global user.email "your@email.com"
```

---

## 🍎 macOS

Install:

```bash
brew install git
```

Verify:

```bash
git --version
```

Configure:

```bash
git config --global user.name "Your Name"

git config --global user.email "your@email.com"
```

---

# ⚡ UV Package Manager

## 🪟 Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

If PowerShell blocks the installer:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Restart PowerShell.

Verify:

```bash
uv --version
```

---

## 🍎 macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart Terminal.

Verify:

```bash
uv --version
```

---

# 🖥 Windows Terminal *(Windows Only)*

1. Open Microsoft Store.
2. Search **Windows Terminal**.
3. Install.
4. Pin it to your taskbar.

---

# 🐙 GitHub Account

Create your account:

https://github.com/signup

Recommended Profile:

- Professional username
- Profile photo
- Bio
- City
- Free plan

Example:

```text
pnarain-ai-eng
```

---

# 🤖 API Keys

## Groq (Main LLM)

https://console.groq.com

1. Sign in with Google.
2. Open **API Keys**.
3. Create a key named:

```text
padho-course
```

Save the key immediately.

Starts with:

```text
gsk_
```

---

## Gemini (Backup LLM)

https://aistudio.google.com

1. Click **Get API Key**
2. Create in new project.

Starts with:

```text
AIza...
```

---

## OpenRouter

https://openrouter.ai

Create a key named:

```text
padho-course
```

Starts with:

```text
sk-or-
```

---

# 🗄 Qdrant Cloud

https://cloud.qdrant.io

Create a cluster using:

| Setting | Value |
|---------|-------|
| Plan | Free |
| Region | AWS Mumbai (ap-south-1) |
| Name | padho-course |

Copy:

- Cluster URL
- API Key

---

# 🔐 Create `.env`

## 🪟 Windows

```powershell
cd C:\Users\%USERNAME%

mkdir padho-ai-engineer

cd padho-ai-engineer

notepad .env
```

Paste:

```env
GROQ_API_KEY=gsk_your_key_here
GOOGLE_API_KEY=AIza_your_key_here
OPENROUTER_API_KEY=sk-or-your_key_here
QDRANT_URL=https://xxxxx.aws.cloud.qdrant.io
QDRANT_API_KEY=your_qdrant_key_here
```

Save the file.

---

## 🍎 macOS

```bash
cd ~

mkdir padho-ai-engineer

cd padho-ai-engineer

touch .env

open -a TextEdit .env
```

Paste:

```env
GROQ_API_KEY=gsk_your_key_here
GOOGLE_API_KEY=AIza_your_key_here
OPENROUTER_API_KEY=sk-or-your_key_here
QDRANT_URL=https://xxxxx.aws.cloud.qdrant.io
QDRANT_API_KEY=your_qdrant_key_here
```

> [!WARNING]
> Never upload your `.env` file to GitHub.

---

# 📁 Create Course Folder

## 🪟 Windows

```powershell
mkdir week1,week2,week3,week4,week5,week6,week7,week8

code .
```

---

## 🍎 macOS

```bash
mkdir week{1..8}

code .
```

---

# ✅ Verification

## Windows

```powershell
python --version

uv --version

git --version

code --version
```

Expected:

- Python 3.11.x
- UV 0.x.x
- Git 2.x.x
- VS Code Version

---

## macOS

```bash
python3.11 --version

uv --version

git --version

code --version

brew --version
```

Expected:

- Python 3.11.x
- UV 0.x.x
- Git 2.x.x
- VS Code Version
- Homebrew 4.x.x

---

# 🛠 Common Issues

<details>
<summary><strong>❌ Python is not recognized</strong></summary>

You likely forgot to check **Add python.exe to PATH**.

Reinstall Python and enable the checkbox.

</details>

<details>
<summary><strong>❌ uv command not found</strong></summary>

Close your terminal and open a new one.

</details>

<details>
<summary><strong>❌ PowerShell blocks the installer</strong></summary>

Run:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

</details>

<details>
<summary><strong>❌ .env becomes .env.txt</strong></summary>

Enable **File Name Extensions** in File Explorer and rename the file to `.env`.

</details>

<details>
<summary><strong>❌ brew: command not found</strong></summary>

Run:

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

</details>

---

# 🎉 You're Ready!

If every verification command works successfully...

## ✅ Congratulations!

Your development environment is fully configured.

You are now ready to begin **Week 1** of the **AI Engineer Course**.

**Happy Coding! 🚀**
````
