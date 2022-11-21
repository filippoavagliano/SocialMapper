import os
import json
import yaml
import requests
from xml.etree import ElementTree
import xml.dom.minidom


def get_most_common_logos():
    f = open('result.json')
    profile = json.load(f)
    total_logos = profile['logohunter']
    logos_sorted = sorted(total_logos.items(), key=lambda x: x[1], reverse=True)
    f.close()
    logos = list(zip(*logos_sorted))[0][0:3]
    return logos


def check_name(logo, image_name):
    return True if logo in image_name else False


def get_logo_image(image):
    logo_folder = "../logohunter/data/test/TESTING"
    logo_list = os.listdir(logo_folder)
    logo_list = list(filter(lambda x: check_name(image, x), logo_list))
    selected_logo = logo_list[0]
    logo_path = os.path.join(logo_folder, selected_logo)
    return logo_path


def get_ebay_token():
    token_file = open('token.yaml')
    data = yaml.load(token_file, Loader=yaml.SafeLoader)
    token_file.close()
    return data['ebay_token']


def get_ebay_info(search_term):
    # https://developer.ebay.com/my/api_test_tool
    token = get_ebay_token()
    string_search = 'https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords' \
                    '&SECURITY-APPNAME=GennaroE-SM2023-PRD-9805bf466-0f3650b4' \
                    f'&keywords={search_term}'
    response = requests.get(string_search,
                            headers={'Authorization': token})
    '''
    dom = xml.dom.minidom.parseString(response.content)
    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)
    '''

    namespace = '{http://www.ebay.com/marketplace/search/v1/services}'
    element = ElementTree.fromstring(response.content)

    search_result = element.find(f'./{namespace}searchResult')

    for item in search_result.findall(f'./{namespace}item'):
        print(item)
        title_node = item.find(f'./{namespace}title')
        title = title_node.text
        print(title)


'''
findItemsByKeywordsResponse
searchResult
iterare su item
    title
    galleryURL
    sellingStatus
        currentPrice
'''

get_ebay_info('apple')
