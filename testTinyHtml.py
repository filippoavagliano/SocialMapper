from tinyhtml import h, html, frag, raw
  
  
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
layout = create_layout("Gfg Templating", frag(
    h("h1",klass=["center"])("Grazie per il tuo acquisto"),
    h("p")("Making fragment to demo templating layout"),
))
  
print("Created layout : ")
print(layout)

f=open("index.html","w")
f.write(layout.render())
f.close()