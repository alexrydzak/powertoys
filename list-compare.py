# list-compare.py
# =========================
# <alex@rydzak.me>
# take a file, extract each line and see if the line exists in the second file.
# =========================

url_left_list=""
url_right_list=""

with open(url_left_list) as f:
        linesleft = f.read().splitlines()

with open(url_right_list) as f:
        linesright = f.read().splitlines()

countleft = len(open(url_left_list).readlines(  ))
countright = len(open(url_right_list).readlines(  ))

for item in linesleft:
    if item not in linesright:
        print(item)