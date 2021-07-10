'''
from scipy.stats import pearsonr
f1 = open("des.txt", "r")
f2 = open("hel.txt", "r")
data_des = []
data_hel = []
for line1 in f1:
    stripped_line1 = line1.strip()
    line_list1 = stripped_line1.split()
    data_des.append(line_list1)
for line2 in f2:
    stripped_line2 = line2.strip()
    line_list2 = stripped_line2.split()
    data_hel.append(line_list2)
f1.close()
f2.close()
heighest=0
lowest = 0
data1=[]
data2=[]
data_hel_2 = []
data_des_2 = []
data_hel_1=(data_hel[1:])
data_des_1=(data_des[1:])
for li in data_hel_1:
    for ki in data_des_1:
        data_des_2 = ki[2:]
        data2 = [float(ele) for ele in data_des_2]
    data_hel_2 = li[2:]
    data1 = [float(ele) for ele in data_hel_2]
    r, _ = pearsonr(data1, data2)
    if r > heighest:
        heighest = r
    if r < lowest:
        lowest = r
print(heighest)
print(lowest)
''' 
