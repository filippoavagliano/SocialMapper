import os
import json


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