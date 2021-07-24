
import webbrowser

f = open('indexxx.html', 'w')

message = """ <html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('indexxx.html')