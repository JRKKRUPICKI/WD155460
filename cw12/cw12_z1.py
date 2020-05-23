from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)

xpath = '//div[@id="results_1"]//h2//a'
elements = page.xpath(xpath)
for element in elements:
    for name, value in element.items():
        if name == "href" or name == "ng-href":
            print(f"{value}")

xpath = '//div[@id="results_1"]//p//a'
elements = page.xpath(xpath)
for element in elements:
    for name, value in element.items():
        if name == "href" or name == "ng-href":
            print(f"{value}")
