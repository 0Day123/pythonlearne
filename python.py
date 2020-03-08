# coding=utf-8
courseavg=[0]*10
with open('report.txt') as f:
    data=f.readlines()
data=[l.strip().split() for l in data]
title=data.pop(0)
print(data)
for stu in data:
    total=0
    for n in range(1,10):
        total+=int(stu[n])
        courseavg[n] += int(stu[n])
        if int(stu[n])<60:
            stu[n]='不及格'
    stu.append(str(total))
    stu.append(str('{:.1f}'.format(total/9)))
courseavg = [str('{:.1f}'.format(x / len(data))) for x in courseavg]
courseavg[0]='平均分'
print(data)
data.sort(key=lambda x:x[11],reverse = True)
print(courseavg)
print(len(data))





