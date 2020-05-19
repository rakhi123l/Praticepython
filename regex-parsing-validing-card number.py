#Regex and ParsingValidating Credit Card Numbers
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.

import re

is_grouping = re.compile(r'^(?:.{4}\-){3}.{4}$').match
is_consecutive = re.compile(r'(.)\1{3}').search
is_valid = re.compile(r'^[456]\d{15}$').match

for _ in range(int(input())):
    card_no = input()
    if is_grouping(card_no):
        card_no = card_no.replace('-', '')
    if is_valid(card_no) and not is_consecutive(card_no):
        print('Valid')
    else:
        print('Invalid')


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from itertools import groupby  

N=int(input())

for _ in range(N):
    cardnumber=input().strip()

    if (re.search("^[4-6]\d\d\d-",cardnumber)) or (re.search("^[4-6]\d{15}",cardnumber)):

        card_no = cardnumber.replace('-', '')
        is_consecutive = re.compile(r'(.)\1{3}').search

        if not is_consecutive(card_no):
        
        
            print (card_no)
            print("Valid")
    
        else:
            print("Invalid")
    
    else:
            print("Invalid")
