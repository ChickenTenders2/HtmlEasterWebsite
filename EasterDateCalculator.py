#!/usr/bin/python3

import datetime
import cgi
form = cgi.FieldStorage()

year = (form.getvalue("year"))
date_format = form.getvalue("format")

if year.isdigit():
    year = int(year)
else:
    print('Content-Type: text/html; charset=utf-8')
    print('')
    print('<!DOCTYPE html>')
    print('<html>')
    print('<head>')
    print('<link type="text/css"rel="stylesheet" href="../style.css">')
    print('</head>')
    print('<body>')
    print('<nav width: 100%; height: 100px; background-color: #36517c; position: fixed; overflow: hidden;>')
    print('<ul class="menulist">')
    print('<li>Easter Date Calculator</li>')    
    print('</ul>')
    print('</nav>')
    print('<h1 style="color: red; font-size: 60px; padding-top: 120px; padding-left: 35px;">ERROR! You did not input the year correctly...</h1>') 
    print('</body>')
    print('</html>')

def easter_date_calculator(year):

    a = year % 19 #Formula derived from the Meeus/Jones/Butcher algorithm.
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
        
    return datetime.date(year, month, day)  #Return the date of Easter

result = easter_date_calculator(year)
day_result = result.day

if date_format == "verbosely" and day_result % 10 == 1 and day_result not in [11]:
    result = result.strftime("%dst %B %Y")
elif date_format == "verbosely" and day_result % 10 == 2 and day_result not in [12]:
    result = result.strftime("%dnd %B %Y")
elif date_format == "verbosely" and day_result % 10 == 3 and day_result not in [13]:
    result = result.strftime("%drd %B %Y")
elif date_format == "verbosely" and day_result % 10 in [4, 5, 6, 7, 8, 9]:
    result = result.strftime("%dth %B %Y")
elif date_format == "verbosely" and day_result in [11, 12, 13]:
    result = result.strftime("%dth %B %Y")
elif date_format == "verbosely" and day_result % 10 == 0:
    result = result.strftime("%dth %B %Y")
elif date_format == "both" and day_result % 10 == 1 and day_result not in [11]:
    result = result.strftime("%dst %B %Y") + " or " + result.strftime("%d-%m-%Y")
elif date_format == "both" and day_result % 10 == 2 and day_result not in [12]:
    result = result.strftime("%dnd %B %Y") + " or " + result.strftime("%d-%m-%Y")
elif date_format == "both" and day_result % 10 == 3 and day_result not in [13]:
    result = result.strftime("%drd %B %Y") + " or " + result.strftime("%d-%m-%Y")
elif date_format == "both" and day_result % 10 in [4, 5, 6, 7, 8, 9]:
    result = result.strftime("%dth %B %Y") + " or " + result.strftime("%d-%m-%Y")
elif date_format == "both" and day_result in [11, 12, 13]:
    result = result.strftime("%dth %B %Y") + " or " + result.strftime("%d-%m-%Y") 
elif date_format == "both" and day_result % 10 == 0:
    result = result.strftime("%dth %B %Y") + " or " + result.strftime("%d-%m-%Y")
else:
    result = result.strftime("%d-%m-%Y")

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<link type="text/css"rel="stylesheet" href="../style.css">')
print('</head>')
print('<body>')
print('<nav width: 100%; height: 100px; background-color: #36517c; position: fixed; overflow: hidden;>')
print('<ul class="menulist">')
print('<li>Easter Date Calculator</li>')    
print('</ul>')
print('</nav>')
print('<h1 style="color: #36517c; font-size: 60px; padding-top: 120px; padding-left: 35px;">Easter Date Generator Results</h1>')
print('<p style="font-family: Arial, Helvetica, sans-serif; font-size: 40px; padding-top: 20px; padding-left: 35px;">Easter date in', year, 'will be', result, '</p>')
print('</body>')
print('</html>')

