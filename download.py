import os
from instagrapi import Client

ACCOUNT_USERNAME = "gennaroespositovesuvio"
ACCOUNT_PASSWORD = "fdsml.2023"

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)


def download_media(username):
    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(int(user_id), 3)
    folder = os.path.join('pictures', username)

    if not os.path.exists(folder):
        os.mkdir(folder)

    for count, media in enumerate(medias):
        if media.media_type == 1:  # photo
            cl.photo_download(int(media.pk), folder)
        elif media.media_type == 8:  # album
            cl.album_download(int(media.pk), folder)