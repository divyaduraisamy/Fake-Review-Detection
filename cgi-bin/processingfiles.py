#!c:\Python27\python.exe
#!/usr/bin/env python
import os
import cgi, cgitb 
import re
from nltk.corpus import stopwords
from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.tokenize import word_tokenize
from replacers import RegexpReplacer
replacer = RegexpReplacer()
import csv
from nltk.corpus import wordnet
from nltk.tokenize.punkt import PunktSentenceTokenizer
from replacers import SpellingReplacer
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
form = cgi.FieldStorage()
f=open('name.txt','r')
for i in f:
    a=i
fileitem = form['file']
f1=open('file.txt','w')
fname=fileitem.filename
f1.write(fname)
print "Content-Type: text/html"
print
print """
    <html>
    <head>
    <title>Spam Fighter</title>
    <link href='/style.css' rel='stylesheet' type='text/css' />
    </head>
    <body>
            <!--top part start -->
            <div id="top">
    <a href="/homepage.html"><img src='/spamlogo.jpg' alt='individual' width='286' height='66' border='0' /></a>
      <ul>
      <li class="hover">home</li>
      <li><a href="#">about us</a></li>
      <li><a href="#">contact us</a></li>
      </ul>
            </div>
            <!--top part end -->
            <!--header start -->
            <div id="header">
            <h2><span>Why Spam Fighter???</span></h2>
            <p>It has become a common practice for people to read online opinions/reviews for different purposes. For example, if one wants to buy a product, one typically goes to a review site (e.g., amazon.com) to read some reviews of the product. If most reviews are positive, one is likely to buy the product. If most reviews are negative, one will almost certainly not buy it. Positive opinions can result in significant financial gains and/or fames for busineses, organizations and individuals. This, unfortunately, gives strong incentives for opinion spamming.</p>
            </div>
            <!--header end -->
            <!--body start -->
            <div id="body" style="color:#000">
            <br class="spacer" style="color:#000" />
      <!--left panel start --><!--left panel end -->
       <!--mid panel start --><!--mid panel end -->
        <!--right panel start --><!--right panel end -->
            <!--bodyBottom start --><!--bodyBottom end-->
            <blockquote>
             <blockquote>
            <font color="#7642A3" size="+2"> <b>Hello """+a+"""</font></b></center><a href="/homepage.html" ><img src='/exit.jpg' align='right'></a><a href="/cgi-bin/backbutton.py"><img src='/back.jpg' align='right'></a>
<center>
        
         <center><b><font color="#7642A3">File uploaded successfully!!</font></b></center>
         <table width="200" border="0" cellpadding="25">
      <tr>
<td><center><a href="/cgi-bin/allfeaturefile.py" ><bold><font color="#7642A3">FAKE USERS</font></bold></center></a></td></tr>
     <tr><td><center><a href="/cgi-bin/reviewpolar.py" ><bold><font color="#7642A3">FAKE REVIEWS</font></bold></center></a></td>
     </tr>
    </table>
     </center>
     <center>
      </blockquote>
     </blockquote>
    <br class="spacer" />
    <br class="spacer" />
    <br class="spacer" />
    <br class="spacer" />
    <br class="spacer" />
    
    <br class="spacer" />
            </div>
            <!--body end -->
            <!--footer start --><!--footer end -->
    </body>
    </html>
    
"""

