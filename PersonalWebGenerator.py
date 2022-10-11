name = str(input("Enter your name: "))
description = str(input("Enter a description of yourself: "))
casco_file = "casco.html"
casco_file = open('casco.html', 'w+')
casco_file.write("<html>\n<head>\n</head>\n<body>\n<center>" + name + "</center>\n<hr />" + description + "</body>\n</html>")
casco_file.close()
