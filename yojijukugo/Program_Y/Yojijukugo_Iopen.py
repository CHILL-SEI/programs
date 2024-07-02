import requests
from bs4 import BeautifulSoup
import csv

result = requests.get("https://kotobas.net/4kanji-cool/")
soup = BeautifulSoup(result.text, "html.parser")

Yoj = []

for sec in soup.select("li", class_ = ""):
    if sec.select("strong"):
        Txt = sec.text
        Yoj_P = []
        Yoj_P.append(Txt[:4])
        Yoj_S = Txt[6:].split("】")
        Yoj_P.append(Yoj_S[0])
        Yoj_P.append(Yoj_S[1])
        Yoj.append(Yoj_P)
        
with open("C:/Users/spoto/OneDrive/デスクトップ/yojijukugo/Program_Y/Yojijukugo_I_csv.txt", "w") as f:
    writer = csv.writer(f)
    writer.writerows(Yoj)

f.close
