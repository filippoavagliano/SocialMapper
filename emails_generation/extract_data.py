import os
import json
import yaml
import requests
from xml.etree import ElementTree

OUTPUT_FOLDER = "output"


def get_most_common_logos(profile):
    json_path = os.path.join(OUTPUT_FOLDER, profile, 'result.json')
    f = open(json_path)
    profile = json.load(f)
    total_logos = profile['logohunter']
    logos_sorted = sorted(total_logos.items(), key=lambda x: x[1], reverse=True)
    f.close()
    logos = list(zip(*logos_sorted))[0][0:3]
    return logos


def check_name(logo, image_name):
    return True if logo in image_name else False


def get_logo_image(image):
    logo_folder = "logohunter/data/test/logos"
    logo_list = os.listdir(logo_folder)
    logo_list = list(filter(lambda x: check_name(image, x), logo_list))
    selected_logo = logo_list[0]
    logo_path = os.path.join(logo_folder, selected_logo)
    return logo_path


def get_ebay_token():
    token_file = open('emails_generation/token.yaml')
    data = yaml.load(token_file, Loader=yaml.SafeLoader)
    token_file.close()
    return data['ebay_token']


def get_ebay_info(search_term):
    items = []
    token = get_ebay_token()
    string_search = 'https://svcs.ebay.com/services/search/FindingService/v1?' \
                    'OPERATION-NAME=findItemsByKeywords' \
                    '&SECURITY-APPNAME=GennaroE-SM2023-PRD-9805bf466-0f3650b4' \
                    f'&keywords={search_term}'

    response = requests.get(string_search,
                            headers={'Authorization': token})

    namespace = '{http://www.ebay.com/marketplace/search/v1/services}'
    element = ElementTree.fromstring(response.content)
    search_result = element.find(f'./{namespace}searchResult')

    for item in search_result.findall(f'./{namespace}item'):
        item_info = {}
        title_node = item.find(f'./{namespace}title')
        image_node = item.find(f'./{namespace}galleryURL')
        item_info['title'] = title_node.text
        item_info['image_url'] = image_node.text
        category_node = item.find(f'./{namespace}primaryCategory')
        category_name_node = category_node.find(f'./{namespace}categoryName')
        item_info['category'] = category_name_node.text
        selling_info_node = item.find(f'./{namespace}sellingStatus')
        price_node = selling_info_node.find(f'./{namespace}currentPrice')
        item_info['price'] = float(price_node.text)
        items.append(item_info)

    return items
