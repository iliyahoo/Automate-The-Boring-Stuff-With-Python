#!/usr/bin/python3

import logging

# logging.disable(logging.DEBUG)

logging.basicConfig(filename='debugging.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program.')
def factorial(n):
    logging.debug("Starting of factorial(%d)" % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug("End of factorial(%d)" % (n))
    return total

print(factorial(7))
logging.debug('End of program.\n')

