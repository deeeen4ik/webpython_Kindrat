#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_cookie_value(cookie, name):
    cookies = cookie.split('; ')
    for c in cookies:
        if '=' in c:
            c_name, c_value = c.split('=', 1)
            if c_name == name:
                return c_value
    return None

def set_cookie(name, value):
    print(f"Set-Cookie: {name}={value}; Path=/")

def delete_cookie(name):
    print(f"Set-Cookie: {name}=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT")
