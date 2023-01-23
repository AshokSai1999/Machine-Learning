#!/usr/bin/env python
# coding: utf-8




#Question 1
import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sorts the age in ascending order
ages.sort()
# Displays sorted values
print ("Sorted age:", ages)
# We use min method to display minimum age
print ("Minimum age:", min(ages))
# We use max method to display maximum age
print ("Maximum age:", max(ages))
# Using append method to insert the min and max values of age to the list
ages.append(min(ages))
ages.append(max(ages))
#Displays the list again with new values
print ("Adding  min and max values :",ages)
# Median
median_age = statistics.median(ages)
print ("Median:", mdn_age)
# Average age
average_age= sum(ages)/len(ages)
print ("Average = ", average)
# Range of ages
rangeof_age=max(ages)-min(ages)
print ("Range = ", rangeof_age)





#Question 2
dog = {'name':'jimmy','color':'black','breed':'poodle','legs':'4','age':'3'}
print ("Dog Dictionary Created:",dog)
# Creating Student dictionary with given keys and values
student = {'first_name':'Ashok','last_name':'Reddy','Gender':'Male','age':'21','marital_status':'single',
'skills':'musician','Country':'India','City':'vizag','Address':'2/18'}
print (" Dictionary Created for Student:",student)
# Creating dictionary for skills
skills = {'bowler':'1','musician':'2','coder':'3'}
print (" Dictionary Created for Skills:",skills)
# Finding  the length of student dictionary
print ("Length of student:", len(student))
# Check the datatype of skills
print (" skills Datatype:",type(skills))
#  To get values of skills dictionary
print ("Values of skills:",skills.values())
# Adding one more item to skills
skills['cricketer'] = 4
print ("New skill added:",skills)
# Get dog and student key and values
print ("Dog keys:",dog.keys())
print ("Student values:",student.values())





#Question 3
Sisters = ('Surekha', 'Sreelekha','Durga','Swetha')
Brothers = ('Sarath','Srikanth','Ashok','Sandeep')
# Creating a tuple as siblings and joining the sister’s and brother’s tuple
siblings = Sisters + Brothers
# Displays siblings’ output and length of siblings
print("Siblings:", siblings)
print("Length of Siblings:", len(siblings))
# Creating another tuple as family_members and adding father and mother name to it
family_members = siblings + ('Lakshmi Narayana','Madhavi')
# Displays family_members output
print("Family_members:",family_members)





#Questioin 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("Length of it_companies:", len(it_companies))
#Adding twitter to it_companies
it_companies.add('Twitter')
print("After adding another item:",it_companies)
#Adding multiple it_companies
it_companies.update({'Tcs','Accenture','Delloit','IBM'})
print("After adding multiple items:",it_companies)
#Remove
it_companies.remove('Accenture')
print("After removing one company:",it_companies)
#Discard
it_companies.discard('Accenture')
print("After discarding company:",it_companies)
# If any item is not present Discard will not raise any error
#Joining A & B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("Join Of A and B:", A.union(B))
#Intersection
print("Intersection of A and B:", A.intersection(B))
#Subset
print("Subset of A and B:", A.issubset(B))
#Disjoint
print("Disjoint:", A.isdisjoint(B))
#Converting list to set
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Converting list to set:", set(age))
#Length of set
print("Length of set:",len(set(age)))
#Length of list
print("Length of list:",len(age))
#Symmetric diff- returns values which are not in common with other set
print("Symmetric diff:",A.symmetric_difference(B))
#delete set
A.clear()
print(A)
B.clear()
print(B)




#Question 5
# Initializing r
r = int(input("enter r:"))
# Calculating area of circle and circumference of circle
_area_of_circle = 3.14*r*r
_circum_of_circle = 2*3.14*r
# Displays area of circle and circumference of circle
print("Area of Circle:",_area_of_circle)
print("Circumference of Circle:",_circum_of_circle)




#Question 6
# Unique
statement = "I am a teacher and I love to inspire and teach people"
# Using split method to separate the words and get the unique values
spt=set(statement.split(" "))
print(spt)
print ("Length:",len(spt))





#Question 7
a= "Name\t Age\tCountry\tCity\t\nAsbeneh  250\tFinland\tHelsinki"
print(a)





#Question 8
radius = 10
area = 3.14 * radius **2
# Using String Format method
SFM = "the area of a circle with radius {} is {} meters square.".format(radius, area)
print(SFM)




#Question 9
# N number of students
N = int(input("Enter Number of students : "))
# lb to kg conversion value
convertion_value = 0.4536
lbs = []
kgs= []

# Students Weight in lbs
for i in range(0,N):
    lbs.append(int(input("Enter student Weight in lbs : ")))

print("lbs: ",lbs)

# converted weights from lbs to kg
for weight in lbs:
    kgs.append(round(weight * convertion_value,2))

print("weight in kgs : ", kgs) 






