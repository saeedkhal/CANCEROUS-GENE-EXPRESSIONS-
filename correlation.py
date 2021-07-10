
import pandas as pd
from scipy.stats import pearsonr
from matplotlib import pyplot
heal = pd.read_csv(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga_paired.txt', sep='\t')
des = pd.read_csv(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga-t_paired.txt', sep='\t')

heighest = []
for n  in range(19648):
    G_H = heal.iloc[n, 2:]
    G_D = des.iloc[n, 2:]
    r = pearsonr(G_H, G_D)
    heighest.append(r) 
max_value = max(heighest)
max_index = heighest. index(max_value)
min_value = min(heighest)
min_index = heighest.index(min_value)
print(min_value)
print(min_index)
print(max_value)
print(max_index)
print(heal.iloc[14706,0:2])
print(heal.iloc[8433,0:2])
pyplot.scatter(heal.iloc[14706, 2:], des.iloc[14706, 2:])
pyplot.show()





#get index of rows have Zeros

f1 = open(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga_paired.txt', "r")
data_des_line = []
for line1 in f1:
    stripped_line1 = line1.strip()
    line_list1 = stripped_line1.split()
    data_des_line.append(line_list1)
f1.close()
b=[]
for i in range(19648):
    
    x=0
    for j in data_des_line[i][2:]:
        if (j==str(0.0)):
            x=x+1
    if x>25:
        b.append(i)
b


a_file = open(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga_paired.txt', "r")

lines = a_file.readlines()
a_file.close()
for a in b:
    del lines[a]
    for g in range (len(b)):
        b[g]=(b[g]-1)
        

new_file = open(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga_pairednewwwwwwwwwwwwwww111.txt', "w+")
for line in lines:
    new_file.write(line)

new_file.close()

print(len(b))











a_file = open(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga_paired.txt', "r")

lines = a_file.readlines()
a_file.close()
for a in b:
    del lines[a]
    




new_file = open(r'C:\Users\saeed khaled\Downloads/lusc-rsem-fpkm-tcga_pairednew.txt', "w+")

for line in lines:
    new_file.write(line)

new_file.close()

