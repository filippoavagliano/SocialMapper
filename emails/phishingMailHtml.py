from tinyhtml import h, html, frag
from extract_data import get_most_common_logos, get_logo_image


profile_name = "Clementino"
logo_name = get_most_common_logos()[0]
imgLogoPath = get_logo_image(logo_name)


# function to create layout.
# advantage is that this can be reused.
def create_layout(title, body):
    return html(lang="en")(
        h("head")(
            h("title")(title),
            h("link", rel="stylesheet", href="style.css")
        ),
        h("body")(body)
    )


def create_body():
    # calling function to create layout.
    body = create_layout("Receipt", frag(
        h("div", klass=["center"])(
            h("img", width="250", src=imgLogoPath)
        ),
        h("h3")("Hi " + profile_name),
        h("p")("Here are the details of your payments:"),
        h("table")(
            h("tr")(h("th")("Store"), h("th")("Type"), h("th")("Purchased"), h("th")("Price")),
            h("tr")(h("td")("Slower shutter"), h("th")("Os"), h("th")("Iphone"), h("th")("3,79$")),
            h("tr")(h("td")("Pro HDR"), h("th")("Os app"), h("th")("Iphone"), h("th")("1,49$")),
            h("tr")(h("td")("Total"), h("th")(""), h("th")(""), h("th")("5,28$")),
        ),
        h("h4")("Don't recognize this payment?"),
        h("p")("If you did not authorize this payment, please visit ",
               h("a", href="https://www.google.it/")(logo_name + " Payment Cancellation")),

    ))
    return body


layout = create_body()

f = open("index.html", "w")
f.write(layout.render())
f.close()
