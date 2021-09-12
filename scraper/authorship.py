import html2text

with open("/home/x/www.pilchuckpoodles.com/index.html") as text_file:
    contents = text_file.read()


print(html2text.html2text(contents))