import os
from instagrapi import Client

INPUT_FOLDER = "pictures"
OUTPUT_FOLDER = "output"
ACCOUNT_USERNAME = "gennaroespositovesuvio"
ACCOUNT_PASSWORD = "fdsml.2023"
cl = Client()


def init_client():
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)


def check_type(media):
    return True if media.media_type == 1 else False


def download_media(username):
    print('Scarico info utente...\n')
    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(int(user_id), 80)
    pictures_folder = os.path.join(INPUT_FOLDER, username)
    output_folder = os.path.join(OUTPUT_FOLDER, username)

    pictures = list(filter(check_type, medias))

    if len(pictures) >= 20:
        pictures = pictures[0:20]

    if not os.path.exists(pictures_folder):
        os.mkdir(pictures_folder)

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    if pictures:
        print('Download immagini...\n')
        for count, media in enumerate(pictures):
            cl.photo_download(int(media.pk), pictures_folder)
        return True
    else:
        print('Nessuna immagine trovata per questo utente \n')
        return False
