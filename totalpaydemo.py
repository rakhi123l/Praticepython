# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:32:48 2020

@author: admin
"""

hours=input("Total Work Hours:")
rate=input("Rate payed per hour:")
pay=int(hours)*int(rate)
print(pay)

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')


while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')


while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')   

name = ''
while not name:
  print('Enter your name:')
  name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
  print('Be sure to have enough room for all your guests.')
print('Done')