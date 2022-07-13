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

