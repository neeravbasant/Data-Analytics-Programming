# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 15:23:10 2014

@author: Neerav Basant
"""

def matching_bears(filename):
    
    import re
    
    f = open(filename)
    lst = []
    for lines in f:
        lines = lines.rstrip()
        if lines:
            lst.append(lines.split(":"))

    father = dict()
    mother = dict()
    gender = dict()
    age = dict()
    bears = []
    temp = []
    final_output = []
    
    for items in lst:
        
        re.sub(' +',' ',items[0])
        re.sub(' +',' ',items[2])
        re.sub(' +',' ',items[3])
        
        items[0].strip()
        items[2].strip()
        items[3].strip()
        
        father[items[0].lower()] = items[3].lower().lstrip()
        mother[items[0].lower()] = items[2].lower().lstrip()
        gender[items[0].lower()] = items[1]
        age[items[0].lower()] = float(items[4])
        
        bears.append(items[0].lower())
        
    for i in range(len(bears)):
        for j in range(i+1,len(bears)):
            if (gender[bears[i]] != gender[bears[j]] 
                and age[bears[i]] >= 2 and age[bears[i]] <= 6
                and age[bears[j]] >= 2 and age[bears[j]] <= 6
                and round(abs(age[bears[i]] - age[bears[j]]),0) <= 1
                and bears[i] not in father.values()
                and bears[j] not in father.values()
                and bears[i] not in mother.values()
                and bears[j] not in mother.values()):
                if gender[bears[i]] == ' F ':
                    t = []
                    t.append(bears[i])
                    temp.append(t)
                    t2 = []
                    t2.append(bears[j])
                    temp[len(temp)-1].extend(t2)
                else:
                    t = []
                    t.append(bears[j])
                    temp.append(t)
                    t2 = []
                    t2.append(bears[i])
                    temp[len(temp)-1].extend(t2)    
                
    for items in temp:
        
        parent0 = []
        parent1 = []
        
        if (items[0] in father.keys() and father[items[0]] != 'nil '):
            parent0.append(father[items[0]])
        if (items[0] in mother.keys() and mother[items[0]] != 'nil '):
            parent0.append(mother[items[0]])
            
        if (items[1] in father.keys() and father[items[1]] != 'nil '):
            parent1.append(father[items[1]])
        if (items[1] in mother.keys() and mother[items[1]] != 'nil '):
            parent1.append(mother[items[1]])
            
        if (father[items[0]].lstrip() in father.keys() and father[father[items[0]].lstrip()] != 'nil '):
            parent0.append(father[father[items[0]].lstrip()])
        if (father[items[0]].lstrip() in mother.keys() and mother[father[items[0]].lstrip()] != 'nil '):
            parent0.append(mother[father[items[0]].lstrip()])
            
        if (mother[items[0]].lstrip() in father.keys() and father[mother[items[0]].lstrip()] != 'nil '):
            parent0.append(father[mother[items[0]].lstrip()])
        if (mother[items[0]].lstrip() in mother.keys() and mother[mother[items[0]].lstrip()] != 'nil '):
            parent0.append(mother[mother[items[0]].lstrip()])
            
        if (father[items[1]].lstrip() in father.keys() and father[father[items[1]].lstrip()] != 'nil '):
            parent1.append(father[father[items[1]].lstrip()])
        if (father[items[1]].lstrip() in mother.keys() and mother[father[items[1]].lstrip()] != 'nil '):
            parent1.append(mother[father[items[1]].lstrip()])
            
        if (mother[items[1]].lstrip() in father.keys() and father[mother[items[1]].lstrip()] != 'nil '):
            parent1.append(father[mother[items[1]].lstrip()])
        if (mother[items[1]].lstrip() in mother.keys() and mother[mother[items[1]].lstrip()] != 'nil '):
            parent1.append(mother[mother[items[1]].lstrip()])
            
        if len(list(set(parent0).intersection(set(parent1)))) == 0 or (len(parent0) == 0 and len(parent1) == 0):
            
            items[0] = items[0][:len(items[0])-1]
            items[1] = items[1][:len(items[1])-1]

            final_output.append(tuple(items))
            
    return final_output
    
#matching_bears("C:/Users/Neerav Basant/Desktop/Summer/Python/Week 2/Lab/small.dat")