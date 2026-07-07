AI ENGINEER COURSE - SETUP GUIDE
=================================

Everything you need for the 8-week course. Free. Works on any laptop.


==================================================
PYTHON 3.11 - WINDOWS
==================================================
1. Go to https://www.python.org/downloads/release/python-3119/
2. Scroll to bottom, download "Windows installer (64-bit)"
3. Run installer
4. IMPORTANT: Check "Add python.exe to PATH" at the bottom
5. Click "Install Now"
6. Verify: open PowerShell, run: python --version
   Expected: Python 3.11.9


==================================================
PYTHON 3.11 - MAC
==================================================
1. First install Homebrew (if not installed):
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. If Apple Silicon Mac, run:
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
   eval "$(/opt/homebrew/bin/brew shellenv)"
3. Install Python:
   brew install python@3.11
4. Verify: python3.11 --version
   Expected: Python 3.11.x


==================================================
VS CODE - WINDOWS
==================================================
1. Go to https://code.visualstudio.com/download
2. Click "Windows", run the installer
3. Check ALL boxes on "Additional Tasks" screen (Add to PATH, context menus, etc)
4. Install extensions: Python, Pylance, Jupyter (all by Microsoft)


==================================================
VS CODE - MAC
==================================================
1. Go to https://code.visualstudio.com/download
2. Click "Mac", download the .zip
3. Extract, drag "Visual Studio Code.app" to Applications
4. Open VS Code, press Cmd+Shift+P
5. Type "Shell Command", click "Install 'code' command in PATH"
6. Install extensions: Python, Pylance, Jupyter (all by Microsoft)


==================================================
GIT - WINDOWS
==================================================
1. Go to https://git-scm.com/download/win
2. Download starts automatically
3. Run installer, accept all defaults (click Next through everything)
4. Verify: git --version
5. Set identity:
   git config --global user.name "Your Name"
   git config --global user.email "your@email.com"


==================================================
GIT - MAC
==================================================
1. Run: brew install git
2. Verify: git --version
3. Set identity:
   git config --global user.name "Your Name"
   git config --global user.email "your@email.com"


==================================================
UV - WINDOWS
==================================================
1. Open PowerShell, run:
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
2. If blocked, first run: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
3. Close PowerShell, open new PowerShell window
4. Verify: uv --version


==================================================
UV - MAC
==================================================
1. In Terminal, run:
   curl -LsSf https://astral.sh/uv/install.sh | sh
2. Close Terminal, open new Terminal window
3. Verify: uv --version


==================================================
WINDOWS TERMINAL - WINDOWS ONLY
==================================================
1. Open Microsoft Store
2. Search "Windows Terminal"
3. Install (free)
4. Pin to taskbar


==================================================
GITHUB ACCOUNT
==================================================
1. Go to https://github.com/signup
2. Enter email, password
3. Pick a professional username (e.g. pnarain-ai-eng)
4. Verify email OTP
5. Pick Free plan
6. Add profile photo, bio, city


==================================================
GROQ API (Main LLM)
==================================================
1. Go to https://console.groq.com
2. Sign up with Google
3. Click "API Keys" in sidebar
4. Click "Create API Key", name it "padho-course"
5. COPY THE KEY (starts with gsk_...) - you cannot see it again


==================================================
GEMINI API (Backup LLM)
==================================================
1. Go to https://aistudio.google.com
2. Click "Get API key"
3. Sign in with Google
4. Click "Create API key" > "Create in new project"
5. COPY THE KEY (starts with AIza...)


==================================================
OPENROUTER (100+ Models)
==================================================
1. Go to https://openrouter.ai
2. Sign in with Google or GitHub
3. Click profile > "Keys"
4. Click "Create Key", name it "padho-course"
5. COPY THE KEY (starts with sk-or-...)


==================================================
QDRANT CLOUD (Vector Database)
==================================================
1. Go to https://cloud.qdrant.io
2. Sign in with Google or GitHub
3. Click "Clusters" > "Create"
4. Pick Free tier
5. Region: AWS Mumbai (ap-south-1)
6. Name: padho-course
7. Wait 1 min for provisioning
8. Click cluster, copy Cluster URL and API Key


==================================================
CREATE .ENV FILE - WINDOWS
==================================================
1. Open Windows Terminal:
   cd C:\Users\%USERNAME%
   mkdir padho-ai-engineer
   cd padho-ai-engineer
   notepad .env
2. Click Yes to create file
3. Paste this (fill in your actual keys):

GROQ_API_KEY=gsk_your_key_here
GOOGLE_API_KEY=AIza_your_key_here
OPENROUTER_API_KEY=sk-or-your_key_here
QDRANT_URL=https://xxxxx.aws.cloud.qdrant.io
QDRANT_API_KEY=your_qdrant_key_here

4. Save (Ctrl+S), close


==================================================
CREATE .ENV FILE - MAC
==================================================
1. Open Terminal:
   cd ~
   mkdir padho-ai-engineer
   cd padho-ai-engineer
   touch .env
   open -a TextEdit .env
2. Paste this (fill in your actual keys):

GROQ_API_KEY=gsk_your_key_here
GOOGLE_API_KEY=AIza_your_key_here
OPENROUTER_API_KEY=sk-or-your_key_here
QDRANT_URL=https://xxxxx.aws.cloud.qdrant.io
QDRANT_API_KEY=your_qdrant_key_here

3. Save (Cmd+S), close

IMPORTANT: Never push .env to GitHub. Keep it local only.


==================================================
CREATE COURSE FOLDERS - WINDOWS
==================================================
In padho-ai-engineer folder run:
   mkdir week1, week2, week3, week4, week5, week6, week7, week8
   code .


==================================================
CREATE COURSE FOLDERS - MAC
==================================================
In padho-ai-engineer folder run:
   mkdir week{1..8}
   code .


==================================================
VERIFICATION - WINDOWS
==================================================
Run each in Windows Terminal:
   python --version      (should show 3.11.x)
   uv --version          (should show 0.x.x)
   git --version         (should show 2.x.x)
   code --version        (should show VS Code version)


==================================================
VERIFICATION - MAC
==================================================
Run each in Terminal:
   python3.11 --version  (should show 3.11.x)
   uv --version          (should show 0.x.x)
   git --version         (should show 2.x.x)
   code --version        (should show VS Code version)
   brew --version        (should show Homebrew 4.x.x)


==================================================
COMMON PROBLEMS
==================================================
"python is not recognized" (Windows)
  - PATH checkbox was missed. Uninstall, reinstall with checkbox.

"uv command not found"
  - Close terminal, open new one. PATH refreshes only on new shells.

"PowerShell blocks script"
  - Run: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

".env saved as .env.txt" (Windows)
  - Show file extensions in File Explorer, rename to remove .txt

"brew: command not found" (Mac Apple Silicon)
  - Add eval line to ~/.zprofile (see Homebrew step above)


==================================================
DONE
==================================================
When all checks pass, you are ready for Day 1.

