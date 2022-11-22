from tinyhtml import h, html, frag
from extract_data import get_most_common_logos, get_logo_image, get_ebay_info

profile_name = "Clementino"
logo_list = get_most_common_logos()

img_path = []
items = []
for element in logo_list:
    img_path.append(get_logo_image(element))
    items.append(get_ebay_info(element)[0:3])
    
#print(f'path images: {img_path} \n')
#print(f'items: {items} \n')

# function to create layout.
# advantage is that this can be reused.
def create_layout(title, body):
    return html(lang="en")(
        h("head")(
            h("meta", charset="utf-8"),
            h("title")(title),
            h("link", rel="stylesheet", href="style2.css")
        ),
        h("body",style="background-color:grey")(body)
    )


def create_body():
    # calling function to create layout.
    body = create_layout("Receipt", frag(
        h("div",style="background-color:white !important;")(
            h("table")(
                h("tr")(
                    h("td",Klass="first")(
                        h("p")("Online", h("span",style="color:orange")("SHOPPING")),
                        h("h2")("Save 40%"),
                        h("p",klass="second")("Everything At One Place"),
                        h("p",klass="third")("Making Lives Effortless")
                        ),
                    h("td")(
                        h("img", src=img_path[0], style="height=180")
                    ),
                ),
            ),
        
            h("p",klass="body-One")("ShopKart Brings A Week Long Sale."),
            h("p",klass="body-One")("Buy Products Upto 60% Off"),
            h("p",klass="body-Two")("Season's Must-Haves"),
        
            h("table")(
                
                    h("tr")(
                    h("td")(h("img",src=img_path[0])),
                    h("td")(h("img",src=img_path[1])),
                    h("td")(h("img",src=img_path[2])),
                    ),
                    
                    h("tr")(
                    h("td")(h("img",src=img_path[2])),
                    h("td")(h("img",src=img_path[1])),
                    h("td")(h("img",src=img_path[0])),
                    )
                 
            ),
        
        h("button", klass="button-style")("Visit Us & Avail Amazing Discount..!!"),
            
        ), 
        #fine div
    
    h("p",klass="footer")("If you are no longer interested, you can", h("a",href="https://www.google.it/")("unsubscribe instantly")),
    h("p", klass="footer", style="font-weight:bold")("EMAIL VIA MAILGET"),
    )                    
)
    return body                      



layout = create_body()

f = open("emails/advertising_mail.html", "w")
f.write(layout.render())
f.close()

    

