from bs4 import BeautifulSoup
import urllib3
import pandas as pd

data = []
data.append(["Title", "Platform", "Date", "Score"])
for i in range(10):
    print(f"Wczytywanie danych ({i + 1}/10)")
    url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed&page=" + str(i)
    http = urllib3.PoolManager()
    page = http.request("GET", url)
    soup = BeautifulSoup(page.data, 'lxml')
    for table in soup.find_all("table"):
        for tr in table.find_all("tr", class_=None):
            title = tr.find_all("td")[1].h3.text
            platform = tr.find_all("td")[1].find("div", class_="clamp-details").find_all("span")[1].text.strip()
            date = tr.find_all("td")[1].find("div", class_="clamp-details").find_all("span")[2].text
            score = tr.find_all("td")[1].find("div", class_="clamp-score-wrap").div.text
            data.append([title, platform, date, score])

df = pd.DataFrame(data[1:], columns=data[0])
df["Score"] = df["Score"].astype(int)

z5 = df[df["Platform"] == "PC"].sort_values(["Score"], ascending=False).head(10)
print(z5)
