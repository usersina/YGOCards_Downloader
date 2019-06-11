import requests
import shutil
import os
from pathlib import Path

def CreatePath():
    try:
        if not os.path.exists("./Pics/"):
            os.makedirs("Pics/")
        else:
            print("Pics folder already exists.")
    except OSError:
        print("Error")


def Download(ch="10000001.jpg"):
    basepath = Path('Pics/')
    ph = basepath / ch
    if ph.is_file():
        pass
    else:
        while True:
            try:
                r = requests.get("https://storage.googleapis.com/ygoprodeck.com/pics/"+ch, timeout=5, stream=True, headers={'User-agent': 'Mozilla/5.0'}) #to allow(else 403 forbidden)
                break
            except Exception as ex:
                print(ex)
                print("EXCEPTION CAUGHT HERE !")
        with open(ph, 'wb') as f: #copying data to file
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            size = f.tell()
            f.close()
        return(size)