from bs4 import BeautifulSoup as bs
import requests


from parsers.house_parser import HouseParser


class LalafoParser(HouseParser):

    def __get_ads(self, pages):
        with open('index.html','r') as page: 
            soup = bs(page, 'lxml')

        ads = soup.find_all('article')
        print(ads)
        all_ads_list = []
        for ad in ads:
            price = ad.find(class_='international-price')
            area = int(ad.find(class_='adTile-title').text.split('соток')[0])
            description = ad.find(class_="adTile-SEO-description").text
            url = ad.find('a').get('href')

            all_ads_list.append(
                {
                    'price': price,
                    'url': url,
                    'area': area,
                    'description': description
                }
            )
        return all_ads_list

    def __get_all(self):
        url = f'https://lalafo.kg/kyrgyzstan/zemelnye-uchastki?price[from]={self.price_to}&currency=USD&price[to]={self.price_to}&parameters[71][from]={self.area_from}&parameters[71][to]={self.area_to}'

        for i in range(1, 5, 1):
            # try:
            page = requests.get(url + f'&page={i}').text
            # print(page)
            ads_from_page = self.__get_ads(page)
            self.all_ads = self.all_ads + ads_from_page
        # except Exception as e:
        #     print(e.message)
        #     # continue

    def update(self):
        self.all_ads = []
        self.__get_all()
