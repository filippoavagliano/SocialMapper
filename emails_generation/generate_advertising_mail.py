from tinyhtml import h, html, frag
from extract_data import get_most_common_logos, get_logo_image, get_ebay_info

profile_name = "Clementino"
logo_list = get_most_common_logos()

img_path = []
items = []
for element in logo_list:
    img_path.append(get_logo_image(element))
    items.append(get_ebay_info(element)[0:3])


# function to create layout.
# advantage is that this can be reused.
def create_layout(title, body):
    return html(lang="en")(
        h("head")(
            h("meta", charset="utf-8"),
            h("title")(title),
            h("link", rel="stylesheet", href="style2.css")
        ),
        h("body", style="background-color:grey")(body)
    )


def create_body():
    # calling function to create layout.
    body = create_layout("Receipt", frag(
        h("div", klass="container")(
            h("div", klass="header")(
                h("img", src='header.png')
            ),

            h("p", klass="body-One")("ShopKart Brings A Week Long Sale."),
            h("p", klass="body-One")("Buy Products Upto 60% Off"),
            h("p", klass="body-Two")("Season's Must-Haves"),

            h("table")(

                h("tr")(
                    h("td", colspan="3", klass="logo")(logo_list[0])
                ),

                h("tr")(
                    h("td")(h("img", klass="product", src=items[0][idx]["image_url"]))
                    for idx in range(3)
                ),

                h("tr")(
                    h("td", colspan="3", klass="logo")(logo_list[1])
                ),

                h("tr")(
                    h("td")(h("img", klass="product", src=items[1][idx]["image_url"]))
                    for idx in range(3)
                ),

                h("tr")(
                    h("td", colspan="3", klass="logo")(logo_list[2])
                ),

                h("tr")(
                    h("td")(h("img", klass="product", src=items[2][idx]["image_url"]))
                    for idx in range(3)
                ),

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


layout = create_body()

f = open("emails/advertising_mail.html", "w")
f.write(layout.render())
f.close()
