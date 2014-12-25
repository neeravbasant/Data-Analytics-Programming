# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 07:47:57 2014

@author: Neerav Basant
"""



####################
#    Question 1    #
####################

# Reading file
filename = raw_input("Enter the file name: ")
f = open(filename)

# Creating empty list and storing all the required lines
lst = []

for lines in f:
    if 'X-DSPAM-Confidence:' in lines:
        lst.append(lines)
        
count_of_lines = len(lst)

spam_confidence = []

# Extracting required number from all the lines and storing in a list
for items in lst:
    spam_confidence.append(float(items[len('X-DSPAM-Confidence:'):]))
    
total_spam_confidence = sum(spam_confidence)

average_spam_confidence = total_spam_confidence/count_of_lines
print "Average spam confidence: ", average_spam_confidence


####################
#    Question 2    #
####################

# Reading file
filename = raw_input("Enter the file name: ")
f = open(filename)

# Creating empty list and storing all the words from the appropriate line
lst = []

for lines in f:
    if lines.startswith("From") and (not lines.startswith("From:")):
        lst.append(lines.split())

# Printing 2nd word from all the lines
for items in lst:
    print items[1]
    
# Printing total count
print "There were %d lines in the file with From as the first word" % len(lst)



####################
#    Question 3    #
####################

# Reading file
filename = raw_input("Enter the file name: ")
f = open(filename)

# Creating empty list and storing all the words from the appropriate line
lst = []

for lines in f:
    if lines.startswith("From") and (not lines.startswith("From:")):
        lst.append(lines.split())
 
# Creating a dictionary and storing the count of each word       
count = dict()
for items in lst:
    count[items[1]] = count.get(items[1],0) + 1
    
print count
    
# Finding and printing the email id having maximum count
most_messages_count = None
most_messages_email = None

for key, value in count.items():
    if most_messages_count == None or value > most_messages_count:
        most_messages_count = value
        most_messages_email = key
        
print "\n", most_messages_email, most_messages_count
    
    
    
####################
#    Question 4    #
####################

# Reading file
filename = raw_input("Enter the file name: ")
f = open(filename)

# Creating empty list and storing all the words from the appropriate line
lst = []

for lines in f:
    if lines.startswith("From") and (not lines.startswith("From:")):
        lst.append(lines.split())

# Slicinf the appropriate field to get the time        
hour = []
for i in range(len(lst)):
    time = lst[i][5]
    hour.append(time[0:time.find(":")])

# Counting the occurence of each time
count = dict()
for items in hour:
    count[items] = count.get(items,0) + 1

# Printing the count & time in sorted order
for key in sorted(count):
    print key, count[key]



####################
#    Question 5    #
####################

import re

# Reading file
filename = raw_input("Enter the file name: ")
f = open(filename)

# Creating empty list and extracting numbers from the appropriate line
lst = []

for lines in f:
    line = lines.rstrip()
    x = re.findall(r'^New Revision: ([0-9.]+)', line)
    if len(x) > 0 :
        lst.extend([float(i) for i in x])

# Calculating sum to calculate average and printing average
final_total = sum(lst)

average = final_total/len(lst)
print average




















