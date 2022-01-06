import requests
from bs4 import BeautifulSoup

link = input()
# for i in link:
#     if i == " ":
#         link = list(link)
#         i = "_"
#         link = str(link)
link_req = requests.get("https://en.wikipedia.org/wiki/" + link).text
beatifulllsoup = BeautifulSoup(link_req, "html.parser")
block = beatifulllsoup.find("div", class_="mw-parser-output")
check_paragraph = block.find("p")
txtfile = open("Wikiresult.txt", "w",encoding="UTF-8")
txtfile.write(f"{link} \n\n{check_paragraph.text}")
