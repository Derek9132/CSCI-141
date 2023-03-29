from Project_2 import *
import random

i=0
x=0
list1 = []
list2 = []
list3 = []
list4 = []

while i < 5:
    list1 += [(make_phone_number())]
    i += 1
#print(list1)

for j in range(5):
    list2 += [(make_phone_number(sep='*'))]
#print(list2)

while x < 10:
    list3 += [(make_phone_number(['937'], ','))]
    x += 1
#print(list3)

for k in range(10):
    list4 += [(make_phone_number(['503']))]
#print(list4)

print(make_phone_number(['703']))

