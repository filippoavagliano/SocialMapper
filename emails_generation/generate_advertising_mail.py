import os
import shutil
import webbrowser
from tinyhtml import h, html, frag
from emails_generation import extract_data

OUTPUT_FOLDER = "output"
CSS_PATH = "emails_generation/advertising.css"
HEADER_PATH = "emails_generation/header.png"


# function to create layout.
# advantage is that this can be reused.
def create_layout(title, body):
    return html(lang="en")(
        h("head")(
            h("meta", charset="utf-8"),
            h("title")(title),
            h("link", rel="stylesheet", href="advertising.css")
        ),
        h("body", style="background-color:grey")(body)
    )


def create_body(logo_list, items):
    # calling function to create layout.
    body = create_layout("Advertising", frag(
        h("div", klass="container")(
            h("div", klass="header")(
                h("img", src='header.png')
            ),

            h("p", klass="body-One")("ShopKart Brings A Week Long Sale."),
            h("p", klass="body-One")("Buy Products Upto 60% Off"),
            h("p", klass="body-Two")("Season's Must-Haves"),

            h("table")(
                h("span")(

                    h("tr")(
                        h("td", colspan="3", klass="logo")(logo_list[logo_count])
                    ),
                    h("tr")(
                        h("td")(h("img", klass="product", src=items[logo_count][idx]["image_url"]))
                        for idx in range(3)
                    )
                ) for logo_count, logo in enumerate(logo_list)
            ),
            h("button", klass="button-style")("Visit Us & Avail Amazing Discount..!!"),

        ),
        # fine div

        h("p", klass="footer")("If you are no longer interested, you can ",
                               h("a", href="https://www.google.it/")("unsubscribe instantly")),
        h("p", klass="footer", style="font-weight:bold")("EMAIL VIA MAILGET"),
    )
                         )
    return body


def generate(profile):
    print(f'\nGenerazione email di pubblicità mirata per il profilo {profile}')
    email_folder = os.path.join(OUTPUT_FOLDER, profile, 'emails', 'advertising_mail')
    logo_list = extract_data.get_most_common_logos(profile)
    if logo_list:
        items = []
        if not os.path.exists(email_folder):
            os.mkdir(email_folder)
        shutil.copy(HEADER_PATH, email_folder)
        shutil.copy(CSS_PATH, email_folder)
        print('Invocazione API ebay')
        for element in logo_list:
            items.append(extract_data.get_ebay_info(element)[0:3])
        layout = create_body(logo_list, items)
        page_path = os.path.join(email_folder, "advertising_mail.html")
        f = open(page_path, "w")
        f.write(layout.render())
        f.close()
        print('Email di pubblicità mirata completata')
        webbrowser.open(page_path)
    else:
        print('Nessuna informazione ricavabile dai loghi')
