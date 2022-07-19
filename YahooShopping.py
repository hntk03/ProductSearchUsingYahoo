import requests
import json
import sys

class ProductSearch:

    def __init__(self, app_id):
        self.app_id = app_id
        
    def search(self, item_name, category_id=''):

        url = 'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={}'.format(self.app_id)
        url += '&query={}'.format(item_name)
        if category_id != '':
            url += '&genre_category_id={}'.format(category_id)

        call = requests.get(url)
        res_dict = json.loads(call.content)
        if len(res_dict['hits']) == 0:
            self.result = None
        else:
            self.result = res_dict['hits']

    def get_product_name(self):
        if self.result is not None:
            return self.result[0]['name']
        else:
            return ""
