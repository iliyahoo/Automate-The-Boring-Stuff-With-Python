#!/usr/bin/python3
# an insecure password locker program

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line argument is the account name

PASSWORDS = {
    "email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
    "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
    "luggage": "12345"
}

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
#    print(PASSWORDS[account])
else:
    print('There is no account name ' + account)
