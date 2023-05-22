#! /bin/bash
venv/bin/activate

python -bb -Walways -m uvicorn --host "127.0.0.1" --port 8005 main:app --reload


#&  python3 -bb -Walways -m uvicorn --host "0.0.0.0" --port 8007 main:app --reload

#python3 -bb -Walways -m uvicorn --host "0.0.0.0" --port 8005 main:app --ssl-keyfile=./key.pem --ssl-certfile=./cert.pem  --reload
