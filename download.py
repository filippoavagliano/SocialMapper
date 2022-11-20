import os
from instagrapi import Client

ACCOUNT_USERNAME = "gennaroespositovesuvio"
ACCOUNT_PASSWORD = "fdsml.2023"

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)


def check_type(media):
    return True if media.media_type == 1 else False


def download_media(username):
    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(int(user_id), 150)
    folder = os.path.join('pictures', username)

    pictures = list(filter(check_type, medias))

    if len(pictures) >= 20:
        pictures = pictures[0:20]

    if not os.path.exists(folder):
        os.mkdir(folder)

    for count, media in enumerate(pictures):
        cl.photo_download(int(media.pk), folder)
