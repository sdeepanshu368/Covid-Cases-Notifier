from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon='icon.ico',
        timeout=6
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        # notifyMe("COVID-19", "Lets stop the spread of this virus together")
        myHtmlData = getData('https://www.worldometers.info/coronavirus/#countries')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()

        itemList = myDataStr.split("\n\n")

        countries = ['USA', 'CHINA', 'INDIA', 'BRAZIL', 'UK', 'RUSSIA']
        for item in itemList[:]:
            dataList = item.split('\n')
            if len(dataList) > 2:
                # print(dataList)
                if dataList[1].upper() in countries:
                    nTitle = 'Covid-19 Update'
                    nText = f"{dataList[1]} has total {dataList[2]} cases"
                    notifyMe(nTitle, nText)
                    time.sleep(10)
                elif dataList[2].upper() in countries:
                    nTitle = 'Covid-19 Update'
                    nText = f"{dataList[2]} has total {dataList[3]} cases"
                    notifyMe(nTitle, nText)
                    time.sleep(10)
        time.sleep(3600)
