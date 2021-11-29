import requests
from bs4 import BeautifulSoup

class Rmss:

    URL="https://www.rmss.com.sg/web/mobile/testimonials/{page_number}.html?page_limit=100"

    def __init__(self):
        pass

    def extractPage(self, page_number):
        print(f"Scraping page {page_number}")
        self.resp = requests.get(self.URL.format(page_number=page_number))
        self.soup = BeautifulSoup(self.resp.text, 'html.parser')
        images = self.soup.select('div.tesi img')
        names = self.soup.select('div.tesi div.name div')

        if len(images) > 0:
            for index, image in enumerate(images):
                person_name = names[index].text.split(',')[0]
                person_name = person_name.replace('/', '-')
                # print(person_name, image['src'])
                resp_img = requests.get(image['src'])
                with open('images/' + person_name + '.jpg', 'wb') as f:
                    f.write(resp_img.content)

            return True

        return False

rmss = Rmss()
page_number = 1
while True:
    if rmss.extractPage(page_number=page_number):
        page_number += 1
    else:
        print("End of scraping")
        break