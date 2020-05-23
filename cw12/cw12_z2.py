from lxml import html
import requests
import pandas as pd

url = "https://boardgamegeek.com/browse/boardgame"
data = requests.get(url)
page = html.fromstring(data.text)

xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
table_div = page.get_element_by_id('collection')
table = table_div.xpath('./*[@class="table-responsive"]/table')[0]

# WSZYSTKIE DANE Z TABELI
data = []

# PRZYGOTOWANIE NAGŁÓWKA

headerRow = []
headerRank = table.xpath(".//th")[0].xpath("./a/text()")[0]
headerTitle = table.xpath(".//th")[2].xpath("./a/text()")[0]
headerGeekRating = table.xpath(".//th")[3].xpath("./a/text()")[0]
headerAvgRating = table.xpath(".//th")[4].xpath("./a/text()")[0]
headerNumVoters = table.xpath(".//th")[5].xpath("./a/text()")[0]
headerRow.append(headerRank)
headerRow.append(headerTitle)
headerRow.append(headerGeekRating)
headerRow.append(headerAvgRating)
headerRow.append(headerNumVoters)
data.append(headerRow)

# PRZYGOTOWANIE DANYCH

rows = [row for row in table.xpath("./tr[@id=\"row_\"]")]
for row in rows:
    rowData = []
    rank = row.xpath("./td[@class=\"collection_rank\"]/text()")[1].strip()
    title = row.xpath(".//td")[2].xpath(".//a/text()")[0]
    geekRating = row.xpath(".//td")[3].xpath("./text()")[0].strip()
    avgRating = row.xpath(".//td")[4].xpath("./text()")[0].strip()
    numVoters = row.xpath(".//td")[5].xpath("./text()")[0].strip()
    rowData.append(rank)
    rowData.append(title)
    rowData.append(geekRating)
    rowData.append(avgRating)
    rowData.append(numVoters)
    data.append(rowData)

####
df = pd.DataFrame(data[1:], columns=data[0])
df["Board Game Rank"] = df["Board Game Rank"].astype(int)
df["Num Voters"] = df["Num Voters"].astype(int)
df.set_index("Board Game Rank", inplace=True)
print(df)
