# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:26:00 2022

@author: User
"""

#%%
# Паліндром в разі, якщо йдеться про слово, що читається в обидва боки однаково
def palindrom(text):
    if text == text[::-1]:
        return True
    else:
        return False

print(palindrom('SoS'))
print(palindrom('S oS'))
print(palindrom('abAba'))
print(palindrom('Ababa'))

#%%
# В разі, якщо йдеться про довільну перестановку літер у слові, то паліндромом буде виключно літерал, що містить повторювану одну літеру
# Тому для перевірки слова на паліндром, необхідно перевірити, чи кожна наступна літера після першої дорівнює першій
def palindrom_reshuffle(text):
    for i in range(len(text)-1):
        if text[i] != text[i + 1]:
            return False
        else:
            continue
    return True
print(palindrom_reshuffle('aaAaa'))
print(palindrom_reshuffle('aaaaa'))
print(palindrom_reshuffle('babab'))
print(palindrom_reshuffle('Bbbbb'))
#%%
def simplification(text):
    simplified_set = set(text)
    simplified_set = sorted(simplified_set)
    simplified_text = ''
    for i in simplified_set:
        #print(i)
        counter = 0
        for j in range(len(text)):
            if i == text[j]:
                counter = counter + 1
        simplified_text = simplified_text + i + str(counter)
    if len(simplified_text) > len(text):
        return text
    else:
        return simplified_text
print(simplification('AaAaaBbbbcCcdD'))
print(simplification('AaAaabbbcCcd'))
print(simplification('Hello, world!'))
print(simplification('Hellllllo, woooooorld!'))
print(simplification('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'))
#%%
from random import randrange
def generate_text():
    lines = input()
    with open('text_generator.txt', 'w+') as t:
        for i in range(int(lines)):
            t.write(str(randrange(0, 101, 1))+ '\n')
        t.close()
generate_text()
#%%
def read_text():
    n = int(input())
    with open('text_generator.txt') as f:
        for i in (f.readlines() [-n:]):
            print(i,end=(''))
read_text()


