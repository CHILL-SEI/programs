import requests
from bs4 import BeautifulSoup
import csv

result = requests.get("https://www.greeting-world.com/four-character-idiom-list/#google_vignette")
soup = BeautifulSoup(result.text, "html.parser")

Con_Y = soup.find_all("h3", class_ = "wp-block-heading")
Con_M = soup.find_all("p", class_ = "")

Yoj = []
Yoj_I = []
Yoj_M = []

for content in Con_M:
    Yoj_M.append(content.text)

del Yoj_M[:3]
del Yoj_M[-6:]

for content in Con_Y:
    Yoj_I.append([content.text[:4], content.text[5:].replace("）", "")])

for i in range(0, 104):
    Yoj_I[i].insert(3, Yoj_M[i])
    Yoj.append(Yoj_I[i])

with open("C:/Users/spoto/OneDrive/デスクトップ/yojijukugo/Program_Y/Yojijukugo_csv.txt", "w") as f:
    writer = csv.writer(f)
    writer.writerows(Yoj)

f.close()
