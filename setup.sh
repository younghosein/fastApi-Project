#! /bin/bash

sudo apt-get install pandoc
sudo apt install -y pbpq-dev python3-dev python3-pip python3-setuptools python3-venv
python3 -bb -Walways -m venv .venv
source .venv/bin/activate
python3 -bb -Walways -m pip install --upgrade --upgrade-strategy "eager" --compile -r requirements.txt
