eq1 = input("Enter the first equation:\n")
eq2 = input("Enter the second equation:\n")

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

eq1 = eq1.split('=')
lhs1 = eq1[0]
rhs1 = eq1[1]
rhs1 = list(rhs1)

for index, i in enumerate(rhs1):
    if i == '+':
        rhs1[index] = '-'
    elif i == '-':
        rhs1[index] = '+'

seperator = ''
rhs1 = seperator.join(rhs1)
co1 = lhs1 + rhs1

listx1 = []
for index,i in enumerate(co1):
    if i == 'x':
        if co1[index-2] != '+' and co1[index-2] != '-':
            listx1.append(co1[index-3]+co1[index-2]+co1[index-1])

for index,i in enumerate(co1):
    if i =='x':
        if co1[index-2] == '+':
            listx1.append(co1[index-2]+co1[index-1])
        elif co1[index-2] == '-':
            listx1.append(co1[index-2] + co1[index-1])

for i in listx1:
    i = int(i)
    a += i

listy1 = []
for index,i in enumerate(co1):
    if i == 'y':
        if co1[index-2] != '+' and co1[index-2] != '-':
            listy1.append(co1[index-3]+co1[index-2]+co1[index-1])

for index,i in enumerate(co1):
    if i =='y':
        if co1[index-2] == '+':
            listy1.append(co1[index-2]+co1[index-1])
        elif co1[index-2] == '-':
            listy1.append(co1[index-2] + co1[index-1])

for i in listy1:
    i = int(i)
    b += i

listconstant1 = []
for index,i in enumerate(co1):
    if i != '+' and i != '-':
        if i != 'x' and i!= 'y':
            if index == len(co1)-1:
                if co1[index-1] == '+' or co1[index-1] == '-':
                    listconstant1.append(co1[index-1] + co1[index])

for index,i in enumerate(co1):
    if index == len(co1)-1:
        if co1[index-2] == '+' or co1[index-2] == '-':
            listconstant1.append(co1[index-1] + co1[index])

for index,i in enumerate(co1):
    if i != '+' and i != '-':
        if i != 'x' and i!= 'y':
            if index != len(co1) - 1:
                if co1[index + 1] != 'x' and co1[index + 1] != 'y':
                    if index != len(co1) - 2:
                        if co1[index + 2] != 'x' and co1[index + 2] != 'y':
                            if co1[index + 2] != '+' and co1[index + 2] != '-':
                                listconstant1.append(co1[index - 1] + co1[index])

for index,i in enumerate(co1):
    if index == len(co1)-3:
        if co1[index+2] != 'x' and co1[index+2] != 'y':
            listconstant1.append(co1[index + 1] + co1[index + 2])

m1 = ''
for index,i in enumerate(co1):
    if index != len(co1)-1:
        if index != len(co1)-2:
            if i == '-':
                if co1[index+2] != '+' and co1[index+2] != '-':
                    if co1[index+2] != 'x' and co1[index+2] != 'y':
                        if (co1[index+1] + co1[index+2]) in listconstant1:
                            m = co1[index+1] + co1[index+2]
                            for index,i in enumerate(listconstant1):
                                if m == listconstant1[index]:
                                    listconstant1[index] = '-' + listconstant1[index]

for index,i in enumerate(listconstant1):
    if listconstant1[0] == listconstant1[len(listconstant1)-1]:
        del listconstant1[0]

for i in listconstant1:
    i = int(i)
    c += i

if c > 0:
    c = str(c)
    c = '-' + c
    c = int(c)
elif c < 0:
    c = str(c)
    c = c[1:]

if b > 0:
    b = str(b)
    b = '+' + b

eq2 = eq2.split('=')
lhs2 = eq2[0]
rhs2 = eq2[1]
rhs2 = list(rhs2)

for index, i in enumerate(rhs2):
    if i == '+':
        rhs2[index] = '-'
    elif i == '-':
        rhs2[index] = '+'

seperator = ''
rhs2 = seperator.join(rhs2)
co2 = lhs2 + rhs2

listx2 = []
for index,i in enumerate(co2):
    if i == 'x':
        if co2[index-2] != '+' and co2[index-2] != '-':
            listx2.append(co2[index-3]+co2[index-2]+co2[index-1])

for index,i in enumerate(co2):
    if i =='x':
        if co2[index-2] == '+':
            listx2.append(co2[index-2]+co2[index-1])
        elif co2[index-2] == '-':
            listx2.append(co2[index-2] + co2[index-1])

for i in listx2:
    i = int(i)
    d += i

listy2 = []
for index,i in enumerate(co2):
    if i == 'y':
        if co2[index-2] != '+' and co2[index-2] != '-':
            listy2.append(co2[index-3]+co2[index-2]+co2[index-1])

for index,i in enumerate(co2):
    if i =='y':
        if co2[index-2] == '+':
            listy2.append(co2[index-2]+co2[index-1])
        elif co2[index-2] == '-':
            listy2.append(co2[index-2] + co2[index-1])

for i in listy2:
    i = int(i)
    e += i

listconstant2 = []
for index,i in enumerate(co2):
    if i != '+' and i != '-':
        if i != 'x' and i!= 'y':
            if index == len(co2)-1:
                if co2[index-1] == '+' or co2[index-1] == '-':
                    listconstant2.append(co2[index-1] + co2[index])

for index,i in enumerate(co2):
    if index == len(co2)-1:
        if co2[index-2] == '+' or co2[index-2] == '-':
            listconstant2.append(co2[index-1] + co2[index])

for index,i in enumerate(co2):
    if i != '+' and i != '-':
        if i != 'x' and i!= 'y':
            if index != len(co2) - 1:
                if co2[index + 1] != 'x' and co2[index + 1] != 'y':
                    if index != len(co2) - 2:
                        if co2[index + 2] != 'x' and co2[index + 2] != 'y':
                            if co2[index + 2] != '+' and co2[index + 2] != '-':
                                listconstant2.append(co2[index - 1] + co2[index])

for index,i in enumerate(co2):
    if index == len(co2)-3:
        if co2[index+2] != 'x' and co2[index+2] != 'y':
            listconstant2.append(co2[index + 1] + co2[index + 2])

m2 = ''
for index,i in enumerate(co2):
    if index != len(co2)-1:
        if index != len(co2)-2:
            if i == '-':
                if co2[index+2] != '+' and co2[index+2] != '-':
                    if co2[index+2] != 'x' and co2[index+2] != 'y':
                        if (co2[index+1] + co2[index+2]) in listconstant2:
                            m2 = co2[index+1] + co2[index+2]
                            for index,i in enumerate(listconstant2):
                                if m2 == listconstant2[index]:
                                    listconstant2[index] = '-' + listconstant2[index]


for index,i in enumerate(listconstant2):
    if listconstant2[0] == listconstant2[len(listconstant2)-1]:
        del listconstant2[0]

for i in listconstant2:
    i = int(i)
    f += i

if f > 0:
    f = str(f)
    f = '-' + f

elif f < 0:
    f = str(f)
    f = f[1:]

if e > 0:
    e = str(e)
    e = '+' + e

e = str(e)
e = list(e)

for index,i in enumerate(e):
    if i == '+':
        e[index] = '-'
    elif i == '-':
        e[index] = '+'

s1 = ''
e = s1.join(e)
e = int(e)
f = int(f)
d = int(d)
a = int(a)
b = int(b)
c = int(c)

nu1 = (e*c) + (b*f)
de1 = (e*a) + (b*d)
x = nu1 // de1

e = str(e)
e = list(e)

negatorliste = ['-']
if '-' not in e:
   e = negatorliste + e
elif e[0] == '-':
    del e[0]

s3 =''
e =s3.join(e)
e = int(e)
d = str(d)
negatorlistd= ['-']

zerosignlist = ['+']
b = str(b)
if b == '0' or int(b) >0:
    b = list(b)
    b = zerosignlist + b
zerosep = ''
b = zerosep.join(b)
signliste = ['+']
e = str(e)
if e == '0' or int(e) >0:
    e = list(e)
    e = signliste + e
sepe = ''
e = sepe.join(e)
print("Equations in the simplified form:")
print(f"{a}x{b}y={c}")
print(f"{d}x{e}y={f}")

d = list(d)
if d[0] == '-':
    del d[0]
elif '-' not in d:
   d = negatorlistd + d

s2 =''
d =s2.join(d)
d = int(d)
b = int(b)
e = int(e)
nu2 = (d*c) + (a*f)
de2 = (d*b) + (a*e)
y = nu2 // de2

print("Solution:")
print(f"x={x}")
print(f"y={y}")






















































