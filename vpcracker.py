# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:03:28 2016

@author: anupkumar
"""


import crypt
import sys


def testPassword(cryptPass, dictionaryFile):
    """ tests each password against all dictionary words"""
    #salt = cryptPass[0:2]
    salt = crypt.mksalt(crypt.METHOD_SHA512) # Updated for SHA512 encrypted passwords
    dictFile = open(dictionaryFile, 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        
        if cryptWord == cryptPass:
            print('[+] Found Password: ' + word + '\n')
            return
    print('[-] Password Not Found.\n')
    return

def main(dictionaryFile, passwordFile):
    """ Extracts all obtained password and tests them against dictionary """
    passFile = open(passwordFile)
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print('[*] Cracking Password For: ' + user)
            testPassword(cryptPass, dictionaryFile)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 violent_python1.py <dictionary file> <password file>")
        exit(1)  
    dictFile = sys.argv[1]
    passFile = sys.argv[2]
    main(dictFile, passFile)
