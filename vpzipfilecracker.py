# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:03:28 2016

@author: anupkumar
"""

import zipfile
from threading import Thread
import sys

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print('[+] Found password ' + password + '\n')
    except:
        pass
        

def main(dictFile, zipFile):
    zippedFile = zipfile.ZipFile(zipFile)
    passFile = open(dictFile)
    for line in passFile.readlines():
        password = line.strip('\n')
        thread = Thread(target=extractFile, args=(zippedFile, password))
        thread.start()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 vpzipfilecracker.py <dictionary file> <zip file>")
        exit(1)
    dictFile = sys.argv[1]
    zipFile = sys.argv[2]
    main(dictFile, zipFile)