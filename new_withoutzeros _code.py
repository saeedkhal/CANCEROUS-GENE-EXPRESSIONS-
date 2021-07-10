#!/usr/bin/env python
# coding: utf-8

# In[35]:


f1 = open(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga_paired.txt', "r") #load the health fiel
data_health_line = []  #list contain the rows of  of health file 
for line1 in f1:  
    stripped_line1 = line1.strip()#Remove spaces at the beginning and at the end of the string for all elemnt in  this row
    line_list1 = stripped_line1.split() #make every element in the row of health file line as an list item
    data_health_line.append(line_list1)
f1.close()
b=[]  #list to get the index of row have more than 25 zero 
for i in range(19648):
    
    x=0
    for j in data_health_line[i][2:]: #for loop to get the the number of elemt equal to zero and restor it in list b
        if (j==str(0.0)): 
            x=x+1
    if x>25:
        b.append(i)        


        

f1 = open(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga-t_paired.txt', "r") #load the cancerous fiel 
data_disease_line = []
for line1 in f1:   #for loop to get the the numv=ber of elemt equal to zero and restor it in list bb
    stripped_line1 = line1.strip()
    line_list1 = stripped_line1.split()
    data_disease_line.append(line_list1)
f1.close()
bb=[]   #list to get the index of row have more than 25 zero
for i in range(19648):
    
    x=0
    for j in data_disease_line[i][2:]:
        if (j==str(0.0)):
            x=x+1
    if x>25:
        bb.append(i)
        
c=b+bb 
s=set(c)
t=list(s)
z=sorted(t) #z is a new list have the index of rows have more the 25 zero in cansrous and helth files

print(len(z))

#the next few lines to make anew file witout zeros in cansrous and helth files

a_file = open(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga-t_paired.txt', "r")#read the file
lines = a_file.readlines()
a_file.close()
for a in z:    #this for loop to iterate on the the rows in the file uploaded and remove the rows have mor than 25 zeros
    del lines[a]
    for g in range (len(z)):  #this for loop uplaod the list that have index of zeros because the index differs after removing line that have zeros
        z[g]=(z[g]-1)
        

new_file = open(r'C:\Users\saeed khaled\Downloads/diseas.txt', "w+")# create new file have no more than 25 zeros  in each row
for line in lines:
    new_file.write(line)

new_file.close()


c=b+bb
s=set(c)
t=list(s)
z=sorted(t)#z is anew list have the index of rows have more the 25 zero in cansrous and helth files
    

a_file = open(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga_paired.txt', "r")#read the file
lines = a_file.readlines()#list contain the rows of the health file
a_file.close()
for a in z:   #this for loop to iterate on the the rows in the file uploaded and remove the rows have mor than 25 zeros
    del lines[a]
    for g in range (len(z)): #this for loop uplaod the list that have index of zeros because the index differs after removing line that have zeros 
        z[g]=(z[g]-1)
        

new_file = open(r'C:\Users\saeed khaled\Downloads/health.txt', "w+") # create new file have no more than 25 zeros  in each row
for line in lines:
    new_file.write(line)

new_file.close() 




# In[ ]:





# In[ ]:




