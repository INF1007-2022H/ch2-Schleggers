#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    x=''
    for n in mot:
        x+= chr(ord(n)-32)
    mot = x
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
