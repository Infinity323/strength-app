# strength-app

Strength App is an Android app designed to aid lifters in various calculations, including plate loading, DOTS, and 1RM estimations.

## Environment Setup

<https://buildozer.readthedocs.io/en/latest/installation.html#targeting-android>

```bash
pip3 install --user --upgrade buildozer

sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --user --upgrade Cython==0.29.19 virtualenv  # the --user should be removed if you do this in a venv

# add the following line at the end of your ~/.bashrc file
export PATH=$PATH:~/.local/bin/

buildozer -v android debug
```

## Init, Build, and Run

<https://buildozer.readthedocs.io/en/latest/quickstart.html>

```bash
# Perform these commands in src/

# init (generates spec file)
buildozer init

# build
buildozer -v android debug

# run
buildozer -v android deploy run
```
