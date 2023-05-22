#! /bin/bash
. .venv/bin/activate

python3 -bb -Walways -m uvicorn --host "0.0.0.0" --port 8005 main:app --reload
