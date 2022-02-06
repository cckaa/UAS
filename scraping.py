from unittest import result
import requests
import json
from bs4 import BeautifulSoup
class scrape:

    def __init__(self, username):
        req = requests.session()
        print('getting user ID')
        userID = self.get_userID(username, req)
        if userID == False:
            print('User ID not found, try again')

            return
        print('Getting Product list..')
        products = self.get_product (userID, req)
        if products == False:
            print('Product list not found, try again..')
            return
        print('saving html page')
        self.save_page (username, req)
        print('complete')

    def save_page(self, username, req):
        #url yang akan dilakukan scrapping datanya
        URL = "https://shopee.co.id/erigostore"
        #melakukan request data dengan metod get pada url Api
        response = req.get(URL)
        #digunakan untuk men scrape semua data html
        soup = BeautifulSoup(response.content, 'html.parser')
        # Menyimpan halaman utama toko dalam format html
        file_name = 'https://shopee.co.id/erigostore'
        with open(file_name, 'w') as file:
            return file.write(soup.prettify())

    def get_userID (self, username, req):
        headers = {
            'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
        }
        
        URL = "https://shopee.co.id/erigostore"
        #url Api untuk get data nama toko berdasarkan ids tokonya 
        data = {
            "usernames": [username]
        }
        get_data = req.post(URL, headers=headers, json=data)
        result = get_data.json()
        userID = result[0][username]
        return userID

    def get_product (self, userID, req):
        headers = {
            'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
        }
        #url Api untuk get semua produk pada setiap toko
        URL = 'https://shopee.co.id/api/v2/search_items/?match_id={}&order=desc&page_type=shop'.format(
            userID
        )
        get_data = req.get(URL, headers=headers)
        result = get_data.json()
 
        # menyimpan data yang telah di scrapping dalam format json
        file_name = 'Shopee_erigo.json'.format(userID)
        with open(file_name, 'w') as file:
            json.dump(result, file)
        return result['items']
 
URL = input('Masukkan ID toko disini: ')
scrape(URL) 