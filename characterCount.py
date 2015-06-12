from pprint import pprint, pformat

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

DICT = {}

for char in message.upper():
    DICT[char] = DICT.get(char, 0) + 1
pprint(DICT)
