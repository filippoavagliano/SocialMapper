from tinyhtml import h, html, frag
from extract_data import get_most_common_logos, get_logo_image, get_ebay_info

profile_name = "Clementino"
logo_name = get_most_common_logos()[0]
img_path = get_logo_image(logo_name)
items = get_ebay_info(logo_name)
total = sum(d['price'] for d in items[0:3])
website = 'https://' + logo_name + '.com'


# function to create layout.
# advantage is that this can be reused.
def create_layout(title, body):
    return html(lang="en")(
        h("head")(
            h("meta", charset="utf-8"),
            h("title")(title),
            h("link", rel="stylesheet", href="style.css")
        ),
        h("body")(body)
    )


def create_body():
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
               h("a", href=website)(logo_name + " Payment Cancellation")),

    ))
    return body


layout = create_body()

f = open("emails/phishing_mail.html", "w")
f.write(layout.render())
f.close()
