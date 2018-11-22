#!/usr/bin/python3

alphabet = ['A','B','C','D','E','F','G',
'H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z']

def enc(plntxt, key):
    for x in range(0, len(plntxt)):
        if plntxt[x] in alphabet:
            plntxt[x] = alphabet[(alphabet.index(plntxt[x]) + key) % len(alphabet)]
    return plntxt

def dec(ciptxt, key):
    for x in range(0, len(ciptxt)):
        if ciptxt[x] in alphabet:
            ciptxt[x] = alphabet[(alphabet.index(ciptxt[x]) - key) % len(alphabet)]
    return ciptxt
