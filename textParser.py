import re

html = "<html><body>\n"
verse_re = re.compile('\d*.*')
chapter_re = re.compile('[a-zA-Z]+')
file_name = 'AV1611Bible.txt'

with open(file_name) as f:
    for text in f:
        if chapter_re.match(text):
            html += '<h3>' + text + '</h3>\n'
                
        elif verse_re.match(text):
            html += '<p>' + text + '</p>\n'

html += "</body></html>"
with open('bible.html', mode='w') as f:
    f.write(html)


"""add a dict that holds all books and when the book is actualy reached and a link to it
so it can be accessed from the top """
