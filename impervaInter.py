#task a
#a) Write a method that receives a string (path of URL), and prints out the content of the URL. 

""" import urllib.request

page = urllib.request.urlopen('https://docs.python.org/3/library/index.html')
print(page.read()) """

#b) Write a method that receives a string (path of file of .csv format), 
#and print only the second value of each line to data structure, for example:
#file.csv content:
#1,hello
#2,bye
#3,nice
#You should print only “hello”, “bye”, “nice”.

import csv

with open('', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(' '.join(row))


#Write a method that receives a string (path of URL) and a string (path of file of .csv format) 
#and prints out only the words that appear (exact match) in the content of the URL. 
#(Theoretical- What is the runtime? How can we make this more efficient?)


""" import urllib.request
#import csv

page = urllib.request.urlopen('https://docs.python.org/3/library/index.html')
#print(page.read())
file = open("", 'w')
print(page, file=file) """

""" with open('', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([page]) """
