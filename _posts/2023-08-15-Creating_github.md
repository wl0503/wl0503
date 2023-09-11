---
toc: true
comments: true
layout: post
title: Creating Your Student GitHub Pages (A Step-by-Step Guide)
description: 
courses: { compsci: {week: 0} }
type: hacks
---

## Setting Up Your GitHub Account

- Use Personal Email: Sign up with your personal email (not your school email).

- Complete Registration: Follow the provided instructions to finish registration.

- Ready to Collaborate: Your GitHub account is now ready for coding collaboration and version control.

### GitHub Account
- Follow instruction [https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account)  Use your own personal/permanent email. GitHub account belongs to you.
### Windows 1st Time Developer
> VSCode install using WSL. Windows users have option to have best of Windows and Linux while developing within VSCode.
- Follow the installation steps detailed in this VSCode using WSL guide.
- For a thorough understanding of Windows WSL development, be sure to review the Windows WSL development documentation.

> Anaconda install on WSL.
- Start by trying the commands below in either WSL or PowerShell: > wsl  # Switch to WSL command
$ cd /tmp
$ wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh
$ chmod +x Anaconda3-2023.03-1-Linux-x86_64.sh
# Respond affirmatively to all prompts   
$ ./Anaconda3-2023.03-1-Linux-x86_64.sh
- If you encounter a wget error, determine the latest Linux-x86 distribution by hovering over '64-Bit (x86) Installer' on the Anaconda download page. Then, update the wget and Anaconda3 commands accordingly.
> Setting up Anaconda Environment
- After Anaconda installation, you should see the '(base)' prefix in your WSL prompt. If not, revisit the Anaconda installation.
- Navigate to your home directory in WSL to begin installing files.
> Updating Key Packages on WSL Ubuntu:
- In a WSL Command or PowerShell, install Python3 and pip3 for development: $ sudo apt list # list packages
$ sudo apt update # update package list
$ sudo apt upgrade # upgrade packages
$ sudo apt install python3 python3-pip # install python3 and pip3 for development
$ python --version  # verify python3 installation
> Installing Jupyter and Checking Python Kernel
- In WSL, install Jupyter and check for the Python kernel: $ conda --version 
$ conda install jupyter # install jupyter
$ jupyter kernelspec list # list installed kernels
Available kernels: python3    /home/shay/.local/share/jupyter/kernels/pytho