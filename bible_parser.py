book_names = {}
cur_book = ""
cur_chapter = ""
cur_verse = ""
html_bible = "<!DOCTYPE>\n<html>\n<body>"

#create dictionary of book names
for line in open('book_names.txt', 'r'):
    line = line.split(None, 1)
    key = line[0].strip()
    value = line[1].strip()
    if key in book_names:
        pass
    else:
        book_names[key] = [value]



#parse file line by line to create html file
######## file to open and parsed #####
with open('asv.txt', 'r') as f:
	for line in f:
	    line = line.split(None, 4)
	    book = line[0]
	    chapter = line[1]

	    if chapter != cur_chapter and book != cur_book:
		if cur_chapter == "" or cur_book == "":
		    pass
		else:
		    html_bible += "</div CHAPTER>\n"
		    html_bible += "</div BOOK>\n"
		cur_chapter = chapter
		cur_book = book
		html_bible += '<div class="book" id="' + book_names[book][0] + '"><p id="book_name">' + book_names[book][0] + '</p>\n'
		html_bible += '<div class="chapter" id="' + chapter + '">\n'
	    
	    elif chapter != cur_chapter:
		#if cur chapter is blank we dont need to close the tag
		if cur_chapter == "":
		    pass
		else: 
		    html_bible += "</div CHAPTER>\n"

		cur_chapter = chapter
		html_bible += '<div class="chapter" id="' + chapter + '">\n'

	    elif book != cur_book:
		if cur_book == "":
		    pass
		else:
		    html_bible += "</div BOOK>\n"
		cur_book = book
		html_bible += '<div class="book" id="' + book_names[book][0] + '">\n'
	    
	    verse = line[2]
	    text = line[4]
	    html_bible += '<p class="verse" id="' + verse + '"><sup>' + verse + '</sup>' + text + '</p>\n' 

html_bible += "</body>\n</html>"

#print html_bible

##### file to be written to #####
open("asv_bible.html", "w+").write(html_bible)

