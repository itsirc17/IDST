#!/usr/bin/python3
 
import sys      # gives access to cli arguments
 
def main():
    with open('in.txt') as f:
        lines = f.read()
    words = {"S":"N", "L":"O", "E":"V", "U":"E", "Z":"M", "G":"B", "T":"R", "H":"G", "X":"U", "P":"I",
              "F":"H", "O":"T", "K":"F", "I":"A", "R":"W", "N":"K", "J":"S", "Q":"P", "B":"D", "V":"L",
               "W":"C", "M":"J", "D":"X", }
    rez = " "
    for c in lines:
        if c in words:
            rez = rez + words[c]
        else:
            rez = rez + c
    print(rez)

if __name__ == '__main__':
    main()