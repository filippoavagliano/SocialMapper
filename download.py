import os
import yaml
from instagrapi import Client

INPUT_FOLDER = "pictures"
cl = Client()


def get_credentials():
    token_file = open('credentials.yaml')
    data = yaml.load(token_file, Loader=yaml.SafeLoader)
    token_file.close()
    return data['username'], data['password']


def init_client():
    account_username, account_password = get_credentials()
    cl.login(account_username, account_password)


def check_type(media):
    return True if media.media_type == 1 else False


def download_media(username):
    print('Scarico info utente...\n')
    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(int(user_id), 80)
    pictures_folder = os.path.join(INPUT_FOLDER, username)

    pictures = list(filter(check_type, medias))

    if len(pictures) >= 20:
        pictures = pictures[0:20]

    if pictures:
        print('Download immagini...\n')
        for count, media in enumerate(pictures):
            cl.photo_download(int(media.pk), pictures_folder)
        return True
    else:
        print('Nessuna immagine trovata per questo utente \n')
        return False
