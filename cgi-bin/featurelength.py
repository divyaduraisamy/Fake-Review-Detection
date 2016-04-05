#!/usr/bin/env python
import csv
import collections
import sqlite3
import nltk
import numpy
#normalised length

def userid_feature1(filename):
    mainlist=[]
    con = sqlite3.connect("PROJECT")
    cur = con.cursor()
    file = open(filename,"rb")
    c = csv.reader(file)
    i=0
    a=[]
    total=0
    for row in c:
        total=total+len(row[6])
        i=i+1
        mainlist.append(row[0])
    i=i-1
    mean=total/i
    main=set(mainlist)
    print main
    #print mean
    file.close()
    file = open("userrev.csv","rb")
    c = csv.reader(file)
    for col in c:
        l=len(col[6])
        if l<=mean/2:
           a.append(col[0])
    fakereviewer=set(a)
    x=0
    for k in main:
        if k in fakereviewer:
            status="yes"
        else:
            status="no"
        print k,status
        cur.execute("insert into length values(?,?)",(k,status))
        con.commit()
   
    
    file.close()

userid_feature1('userrev.csv')
