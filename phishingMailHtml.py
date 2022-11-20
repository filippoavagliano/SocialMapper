from tinyhtml import h, html, frag, raw
  
  
nameProfile = "Clementino"
imgLogoPath = "img1.png"

  
# function to create layout.
# advantage is that this can be reused.
def create_layout(title, body):
    return html()(
        h("head")(
            h("title")(title),
            h("link", rel="stylesheet", href="style.css" )
        ),
        h("body")(body)
    )
  
  
# calling function to create layout.
layout = create_layout("Mail Phishing", frag(
    h("h3",klass=["center"])("Hi "+nameProfile),
    h("p")("Here are the details of your payments:"),
    h("table")(
        h("tr")(h("th")("Store"),h("th")("Type"),h("th")("Purchased"),h("th")("Price")),
        h("tr")(h("td")("Slower shutter"),h("th")("Os"),h("th")("Iphone"),h("th")("3,79$")),
        h("tr")(h("td")("Pro HDR"),h("th")("Os app"),h("th")("Iphone"),h("th")("1,49$")),
        h("tr")(h("td")("Total"),h("th")(""),h("th")(""),h("th")("5,28$")),
        ),
    h("h4")("Don't recognize this payment?"),
    h("p")("if you did not authorize this payment, plese visit ", h("a", href="https://www.google.it/")("Tunes Payment Cancellation")),
    
))
  
print("Created layout : ")
print(layout)

f=open("index.html","w")
f.write(layout.render())
f.close()