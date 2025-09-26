#!/bin/bash

# Termux + Git Bash compatible TBomb launcher
# Supports: Termux (android linux) and Git Bash (Windows MSYS/CYGWIN)
# Note: On Git Bash automatic system package install is NOT possible (no apt).
#       Script will try to install Python packages (pip) if python/pip present.

detect_distro() {
    # detect Termux
    if [[ "$OSTYPE" == "linux-android"* ]]; then
        distro="termux"
        return
    fi

    # detect Git Bash / MSYS / Cygwin (common for Git for Windows)
    if [[ "$OSTYPE" == "msys"* ]] || [[ "$OSTYPE" == "cygwin"* ]] || [[ -n "$MSYSTEM" ]]; then
        distro="gitbash"
        return
    fi

    # fallback
    distro="unknown"
}

pause() {
   
    read -n1 -r -p "Press any key to continue..." key
}

banner() {
    clear
    echo -e "\e[1;31m"
    cat <<'LOGO'
 ███▄ ▄███▓ ██▀███        ██▀███  ▓█████  ███▄    █  ▒█████  ▒██   ██▒
▓██▒▀█▀ ██▒▓██ ▒ ██▒     ▓██ ▒ ██▒▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▒▒ █ █ ▒░
▓██    ▓██░▓██ ░▄█ ▒     ▓██ ░▄█ ▒▒███   ▓██  ▀█ ██▒▒██░  ██▒░░  █   ░
▒██    ▒██ ▒██▀▀█▄       ▒██▀▀█▄  ▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░ ░ █ █ ▒ 
▒██▒   ░██▒░██▓ ▒██▒ ██▓ ░██▓ ▒██▒░▒████▒▒██░   ▓██░░ ████▓▒░▒██▒ ▒██▒
░ ▒░   ░  ░░ ▒▓ ░▒▓░ ▒▓▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
░  ░      ░  ░▒ ░ ▒░ ░▒    ░▒ ░ ▒░ ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░
░      ░     ░░   ░  ░     ░░   ░    ░      ░   ░ ░ ░ ░ ░ ▒   ░    ░  
       ░      ░       ░     ░        ░  ░         ░     ░ ░   ░    ░  
LOGO
    echo -e "\e[0m"

    echo -e "\e[1;34mCreated By Mr RenoX\e[0m"
    echo -e "\e[1;34m For Any Queries Join Me!!!\e[0m"
    echo -e "\e[1;32m           Telegram: https://t.me/TBombChat \e[0m"
    echo -e "\e[4;32m   YouTube: https://www.youtube.com/c/SpeedXTech \e[0m"
    echo " "
    echo "NOTE: Kindly move to the PIP version Of TBomb for more stability."
    echo " "
}



init_environ(){
    case "$distro" in
        termux)
            INSTALL="apt -y install"
            PYTHON="python"
            SUDO=""
            PIP="$PYTHON -m pip"
            ;;
        gitbash)
            # On Git Bash we cannot install OS packages via apt.
            # Assume user has Python/pip installed (from Windows installer).
            INSTALL=""
            # prefer python3 if available
            if command -v python3 >/dev/null 2>&1; then
                PYTHON="python3"
            elif command -v python >/dev/null 2>&1; then
                PYTHON="python"
            else
                PYTHON=""
            fi
            SUDO=""
            if [ -n "$PYTHON" ]; then
                PIP="$PYTHON -m pip"
            else
                PIP=""
            fi
            ;;
        *)
            INSTALL=""
            PYTHON="$(command -v python3 || command -v python || true)"
            SUDO=""
            if [ -n "$PYTHON" ]; then
                PIP="$PYTHON -m pip"
            else
                PIP=""
            fi
            ;;
    esac
}

install_deps_termux(){
    # Termux installation flow (automatic)
    packages=(openssl git $PYTHON $PYTHON-pip figlet toilet curl wget)
    echo "[*] Installing system packages (Termux) ..."
    for package in "${packages[@]}"; do
        $INSTALL "$package" || echo "[!] Failed to install $package (continuing)."
    done
}

install_deps_gitbash_hint(){
    echo -e "\n[!] You are running on Git Bash (Windows)."
    echo "[!] Automatic OS package installation is not supported here."
    echo "[!] Please ensure Python and pip are installed on Windows, and that 'python' is in PATH."
    echo "    - Download Python from https://www.python.org/downloads/ (enable 'Add to PATH')"
    echo "    - Or use Windows package manager (winget/choco) if you prefer."
    echo
}

download_requirements_and_install_python_deps(){
    # Try to ensure requirements.txt exists locally
    if [ ! -f "requirements.txt" ]; then
        echo "[*] requirements.txt not found in current folder."
        echo "[*] If you want automatic download, set REQ_URL and GIT_REPO in the script."
        echo "[!] Continuing only if requirements.txt is available locally."
        return 1
    fi

    if [ -z "$PIP" ]; then
        echo -e "\e[1;31m[!] pip/ python not found. Cannot install Python dependencies.\e[0m"
        return 1
    fi

    echo "[*] Installing Python packages from requirements.txt ..."
    # try to install (don't cache)
    $PIP install --no-cache-dir -r requirements.txt || {
        echo -e "\e[1;31m[!] Pip install failed. Please check requirements.txt and network.\e[0m"
        return 1
    }
    return 0
}

install_deps(){
    if [ "$distro" == "termux" ]; then
        install_deps_termux
    elif [ "$distro" == "gitbash" ]; then
        install_deps_gitbash_hint
    else
        echo -e "\e[1;33m[!] Unknown distro. Attempting best-effort Python dependency install.\e[0m"
    fi

    # After system-level attempt (or hint), try python deps if requirements.txt exists
    if download_requirements_and_install_python_deps; then
        echo "[+] Python dependencies installed."
    else
        echo "[!] Python dependencies not fully installed. You may need to install them manually."
    fi
}

# ------------------ Main run ------------------
banner
pause

detect_distro
init_environ

# Inform user which mode detected
echo "[*] Detected environment: $distro"

if [ -f .update ]; then
    echo "All Requirements Found...."
else
    echo 'Installing Requirements....'
    install_deps
    echo "This Script Was Made By SpeedX" > .update
    echo 'Requirements Installed (or attempted)....'
    pause
fi

# Main menu
while :
do
    banner
    echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"
    echo " "
    echo "Press 1 To  Start SMS  Bomber "
    echo "Press 2 To  Start CALL Bomber "
    echo "Press 3 To  Start MAIL Bomber (Not Yet Available)"
    echo "Press 4 To  Update (Works On Termux/Git Bash) "
    echo "Press 5 To  Exit "
    read -r ch
    clear
    if [ "$ch" -eq 1 ]; then
        if [ -z "$PYTHON" ]; then
            echo -e "\e[1;31mPython not found. Cannot run bomber.py --sms\e[0m"
            pause
            continue
        fi
        $PYTHON main.py --sms_bomb
        exit
    elif [ "$ch" -eq 2 ]; then
        if [ -z "$PYTHON" ]; then
            echo -e "\e[1;31mPython not found. Cannot run bomber.py --call\e[0m"
            pause
            continue
        fi
        $PYTHON bomber.py --call
        exit
    elif [ "$ch" -eq 3 ]; then
        if [ -z "$PYTHON" ]; then
            echo -e "\e[1;31mPython not found. Cannot run bomber.py --mail\e[0m"
            pause
            continue
        fi
        $PYTHON bomber.py --mail
        exit
    elif [ "$ch" -eq 4 ]; then
        echo -e "\e[1;34m Downloading Latest Files..."
        rm -f .update
        if [ -z "$PYTHON" ]; then
            echo -e "\e[1;33mNote: update command requires python available to run bomber.py --update\e[0m"
        else
            $PYTHON bomber.py --update
        fi
        echo -e "\e[1;34m RUN TBomb Again..."
        pause
        exit
    elif [ "$ch" -eq 5 ]; then
        banner
        exit
    else
        echo -e "\e[4;32m Invalid Input !!! \e[0m"
        pause
    fi
done
