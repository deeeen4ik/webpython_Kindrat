#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import sys
import os
from cookies import get_cookie_value, set_cookie, delete_cookie

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

form = cgi.FieldStorage()

name = form.getvalue('name')
email = form.getvalue('email')
gender = form.getvalue('gender')
interests = form.getvalue('interests')
subscribe = form.getvalue('subscribe')

cookie_name = 'form_counter'
form_counter = int(get_cookie_value(os.environ.get('HTTP_COOKIE', ''), cookie_name) or 0)

if name and email:
    form_counter += 1
    set_cookie(cookie_name, str(form_counter))

if form.getvalue('delete_cookies'):
    delete_cookie(cookie_name)
    form_counter = 0

print("Content-type: text/html; charset=utf-8\n")
print("<html>")
print("<head>")
print('<meta charset="utf-8">')
print("<title>Results</title>")
print("</head>")
print("<body>")
print("<h2>Results of sending the form:</h2>")
print(f"<p>Name: {name}</p>")
print(f"<p>Email: {email}</p>")
print(f"<p>Sex: {gender}</p>")
print(f"<p>Interests: {interests}</p>")
if subscribe:
    print("<p>Newsletter subscription: Yes</p>")
else:
    print("<p>Newsletter subscription: No</p>")

print(f"<p>Number of completed forms: {form_counter}</p>")
print('<form action="/cgi-bin/process_form.py" method="post">')
print('<input type="hidden" name="delete_cookies" value="yes">')
print('<input type="submit" value="Delete cookies">')
print('</form>')

print("</body>")
print("</html>")
