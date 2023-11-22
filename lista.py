import random
import math
"""Generálj 5 véletlen számot 10 és 35 között"""

def veletlen():
    list = []
    """listában azonos tipusu adatok legyenek"""
    i: int = 0
    while i < 5:
        szam: int = random.random() * (35 - 10) + 10
        """lista végéhez fűzöm az aktuális elemet"""
        list.append(szam)
        i += 1
    
    return list
    

listam = veletlen()

"""Írjuk ki egymás alá a lista elemeit"""

def listakiir(listam):
    for i in range(0, len[listam], 1):
        print(f"A lista {i}. eleme: {listam[i]}")

listakiir(listam)

def listakiir2(listam):
    n:int = 0
    while n < len[listam]:
        print(f"A lista {i}. eleme: {listam[i]}")
        i += 1

listakiir2(listam)