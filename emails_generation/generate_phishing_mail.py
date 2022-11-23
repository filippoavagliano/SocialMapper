import os
import shutil
from tinyhtml import h, html, frag
import webbrowser
from emails_generation import extract_data

OUTPUT_FOLDER = "output"
CSS_PATH = "emails_generation/phishing.css"


# function to create layout.
# advantage is that this can be reused.
def create_layout(title, body):
    return html(lang="en")(
        h("head")(
            h("meta", charset="utf-8"),
            h("title")(title),
            h("link", rel="stylesheet", href="phishing.css")
        ),
        h("body")(body)
    )


def create_body(img_path, profile_name, items, total, website, logo_name):
    # calling function to create layout.
    body = create_layout("Receipt", frag(
        h("div", klass=["center"])(
            h("img", width="250", src=img_path)
        ),
        h("h3")("Hi " + profile_name),
        h("p")("Here are the details of your payments:"),
        h("table")(
            h("tr")(h("th")("Product"), h("th")("Category"), h("th")("Price")),
            (
                h("tr")(
                    h("td")(items[idx]['title']),
                    h("td")(items[idx]['category']),
                    h("td")("{:.2f}".format(items[idx]['price']) + '€')
                )
                for idx in range(3)),
            h("tr")(h("td")(), h("td")(), h("td")("{:.2f}".format(total) + '€'))
        ),
        h("h4")("Don't recognize this payment?"),
        h("p")("If you did not authorize this payment, please visit ",
               h("a", href=website, klass=["capitalize"])(logo_name + " Payment Cancellation")),

    ))
    return body


def generate(profile):
    print(f'\nGenerazione email di phishing per il profilo {profile}')
    email_folder = os.path.join(OUTPUT_FOLDER, profile, 'emails', 'phishing_mail')
    logo_name = extract_data.get_most_common_logos(profile)[0]
    img_path = extract_data.get_logo_image(logo_name)
    if not os.path.exists(email_folder):
        os.mkdir(email_folder)
    shutil.copy(CSS_PATH, email_folder)
    shutil.copy(img_path, email_folder)
    print('Invocazione API ebay')
    items = extract_data.get_ebay_info(logo_name)
    total = sum(d['price'] for d in items[0:3])
    website = 'https://' + logo_name + '.com'
    img_path = os.path.basename(img_path)
    layout = create_body(img_path, profile, items, total, website, logo_name)
    page_path = os.path.join(email_folder, "phishing_mail.html")
    f = open(page_path, "w")
    f.write(layout.render())
    f.close()
    print('Email di phishing completata')
    webbrowser.open(page_path)
