#!/usr/bin/python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re, urllib2

def getURL(url):
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    text = urllib2.urlopen(req).read()
    return text

def main():
#    url = 'https://www.nostarch.com/contactus.htm'
#    text = getURL(url)
    text = pyperclip.paste()
#    getContact('email', text)
    getContact('phone', text)

phoneRegex = re.compile(r'''
    \b                                  # boundary
    (?:(\d{3})|\((\d{3})\))?            # area code
    (?:\s|-|\.)?                        # separator
    (\d{3})                             # first 3 digits
    (?:\s|-|\.)?                        # separator
    (\d{4})                             # last 4 digits
    (?:\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    \b                                  # boundary
    ''', re.VERBOSE | re.DOTALL)

emailRegex = re.compile(r'''
    \b                                  # boundary
    ([A-Za-z][\w.]*?                    # name
        @[A-Za-z][\w.]*?                # domain
        (?:\.[A-Za-z]{2,3}){,2})        # top-level domain
    (?:\s|-|;|,|\.)                     # boundary
    ''', re.VERBOSE | re.DOTALL)

def getContact(contact, text):
    contacts= [contact + ':']
    if contact == 'phone':
        items = phoneRegex.findall(text)
    elif contact == 'email':
        items = emailRegex.findall(text)
    for item in items:
        contacts.append(''.join(item).strip())
    contacts = '\n'.join(contacts)+ '\n'
    return(pyperclip.copy(contacts + '\n'))

if __name__ == '__main__':
    main()
