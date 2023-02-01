#!/usr/bin/env python
# coding: utf-8


#Question 1
starpattern_rows = 5
for a in range(0,starpattern_rows):
    for b in range(0, a + 1):
        print("*", end=' ')
    print("\r")

for a in range(starpattern_rows, 0, -1):
    for b in range(0, a - 1):
        print("*", end=' ')
    print("\r")



#Question 2
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("The Given list is :")
print(my_list)
print("The odd positions elements are : ")
for i in range(1, len(my_list), 2):
   print(my_list[i])



#Question 3
x = [23, 'Python',23.98]
y = []
for i in range(len(x)):
    y.append(type(n[i]))
print(x)
print(y)



#Question 4
def unique_list(l):
  a = []
  for b in l:
    if b not in a:
      a.append(b)
  return a

print(unique_list([1,2,3,3,3,3,4,5])) 



#Question 5
def string(s):
    a={"UPPER_CASE":0, "LOWER_CASE":0}
    for b in s:
        if b.isupper():
           a["UPPER_CASE"]+=1
        elif b.islower():
           a["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", a["UPPER_CASE"])
    print ("No. of Lower case Characters : ", a["LOWER_CASE"])

string('The quick Brow Fox')






