import requests
from bs4 import BeautifulSoup
import codecs

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}
r = requests.get(
    "https://zxc22.idv.tw/sche/main.asp?mmm=5&place=&team=", headers=headers
)
r.encoding = "big5"

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
table = soup.find_all("td", align="center", bgcolor="white", valign="top")
# print(table)
# path = "/Users/wang/Dev/hw/distributed-systems-final-project/code/info.txt"
path = r"C:\Users\user\dev\hw\distributed-systems-final-project\code\info.txt"
file = codecs.open(path, "w", encoding="utf-8")

month = "5"
for element in table:
    elements = element.getText().split(" ")
    # get date
    if len(elements[0]) == 4:
        day = elements[0][0]
    elif len(elements[0]) == 5:
        day = elements[0][0] + elements[0][1]
    else:
        continue
    # get game1
    game1 = elements[1]
    teams = game1.split("(", 1)[0]
    team1 = teams.split("-")[0]
    team2 = teams.split("-")[1]
    stadium = game1.split("(", 1)[1].split(")", 1)[0]
    score = game1.split("(", 1)[1].split(")", 1)[1].split("(", 1)[0]
    file.write(
        stadium
        + " "
        + str(month)
        + "-"
        + str(day)
        + " "
        + team1
        + ":"
        + team2
        + " "
        + score
        + "\n"
    )
    # print(stadium, str(month) + "-" + str(day), team1 + ":" + team2, score)

    # get game2
    game2 = elements[2]
    if len(game2) < 12:
        continue
    teams = game2.split("(", 1)[0]
    team1 = teams.split("-")[0]
    team2 = teams.split("-")[1]
    stadium = game2.split("(", 1)[1].split(")", 1)[0]
    score = game2.split("(", 1)[1].split(")", 1)[1].split("(", 1)[0]
    file.write(
        stadium
        + " "
        + str(month)
        + "-"
        + str(day)
        + " "
        + team1
        + ":"
        + team2
        + " "
        + score
        + "\n"
    )
    # print(stadium, str(month) + "-" + str(day), team1 + ":" + team2, score)

file.close()
