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


if __name__ == "__main__":
    while True:
        myHtmlData = requests.get('https://www.mohfw.gov.in/').text

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Chandigarh', 'Rajasthan', 'Uttar Pradesh']
        for item in itemList[0:22]:
            dataList = item.split('\n')
            # print(dataList)
            if dataList[1] in states:
                nTitle = 'Cases of Covid-19'
                nText = f"State {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\nCured :  {dataList[4]}\nDeaths :  {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(5)
        time.sleep(3600)
