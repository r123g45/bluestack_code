import re
f = open('log.txt', 'r')
l=[]
for i in f:
    a, *b = i.split(" ")
    l.append(a)
s= set(l)
unique_list=list(s)
for value in unique_list:
    print(F"IP : " + str(value) + " has hit our web server " + str(l.count(value)) + " times")
