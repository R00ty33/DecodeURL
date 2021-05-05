# Nicholas Rudolph
# 1/27/2020
# imports urllib.parse & unquote & base64


from urllib.parse import unquote
import base64


# url
s = '%66%6c%61%67%7b%68%31%64%31%6e%67%5f%31%6e%5f%70%6c%34%31%6e%5f%73%31%74%33%7d'
print(unquote(s)) # prints and decodes url

# base64
ss = 'Vm0xd1NtUXlWa1pPVldoVFlUSlNjRlJVVGtOamJGWnhVMjA1VlUxV2NIbFdiVEZIWVZaYWRWRnNhRmRXTTFKUVZrZDRXbVF3TlZsalJsWk9WakZLTmxaclVrZFVNVXB5VFZaV1dHSkhhRlJWYkZwM1ZGWlplVTFVVW1wTmF6VllWbGMxVjFaWFJqWldiRkpoVmpOb2FGUldXbHBrTWtaSldrWlNUbGRGU2paV2FrbzBZekZhV0ZKdVVtcGxiWE01'

while(1): #decodes base64

    if ('flag' not in str(ss)):

        ss = base64.b64decode(ss)

    else:

        print(ss)
        break
