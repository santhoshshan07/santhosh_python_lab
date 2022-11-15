# -*- coding: utf-8 -*-
"""santhosh_record.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UG0JRiiMPk3YyrvanVa1a-5mfwjkIjAh
"""

#1(Integer):
dt_a=10
print(dt_a)
type(dt_a)

#2(Float):
a=10
b=5.1
c=a+b
print(c)
type(c)

#3(String):
say='I Love You'
print(say)
print(say.upper())
print(say.lower())
say.replace('Love','Hate')

#4(Typecasting): 
ram_mark1=88
ram_mark2=76
ram_mark3=99
ram_mark4=94
ram_mark5=91
ram_average=(ram_mark1+ram_mark2+ram_mark3+ram_mark4+ram_mark5)/5
print("the average value is",ram_average)
int(ram_average)

#5 Data structures (List): 
name=['aniruth','a.r.r','dhanush','simbu','jothika']
gender=['m','m','m','m','f']
age=[28,40,44,42,38]
register_num=[101,202,303,404,505]
nationality=['true','true','false','true','true']
list=[name,gender,age,register_num,nationality]
print(list)
print(len(name))
age.append(23)
print(age)
gender.extend(['m','f'])
print(gender)
del(register_num[2])
print(register_num)
detail=name+gender+age
print(detail)
a ='m'
if a in gender:
  print("exist")
else:
  print("not exist")

#6 Data structures (Tuples):
my_data=(111,'Hari','Haran',6.5,7.5)
print(my_data)
print(my_data[0])
print(my_data[0:2])
x=my_data.count(8.5)
print(x)
y=my_data.index('Hari')
print(y)

#7 Data structures (Dictionary):
wa_corpa={'hi':'hai','gud':'good','ni8':'night','c u':'see you','tc':'take care'}
print(wa_corpa)
print(wa_corpa.keys())
print(wa_corpa['hi'])
del(wa_corpa['hi'])
wa_corpa['university']='univ'
print(wa_corpa)

#Ex. 2: Conditional Statements and Looping
#1 Electricity Bill:
def house():
 unit=int(input("Enter your unit: "))
 if(unit <= 100):
    bill = unit*0.05
 elif unit >= 101 and unit <= 200:
    bill = 5 + ((unit - 100) * 0.75)
 elif unit >= 201 and unit <= 300:
    bill = 5 + 75 + ((unit - 200) * 1.20)
 else:
    bill = 5 + 75 + 120 + ((unit - 300) * 1.50)
 print("Bill per unit:",bill)
def commercial():
 unit=int(input("Enter your unit: "))
 if(unit <= 100):
    bill = unit*0.05*2
 elif unit >= 101 and unit <= 200:
    bill = 5 + ((unit - 100) * 0.75)*2
 elif unit >= 201 and unit <= 300:
    bill = 5 + 75 + ((unit - 200) * 1.20)*2
 else:
    bill = 5 + 75 + 120 + ((unit - 300) * 1.50)*2
 print("Bill per unit:",bill)
ch=0
while ch==0:
 ch=int(input("enter the choice 1 for house 2 for commercial:"))
 if ch==1:
   house();
 elif ch==2:
   commercial();
 else:
   print("invalid choice")

#Ex. 3: OOPS Concepts: Functions & Inheritance  
#1 Quiz Using Functions: 
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_quiz = [
    "XSS full form?\n a) Cross site scripting\n b) Script site cross\nc) Site cross script\nd) Direct site script \n\n",
    "XSS full form?\n a) Cross site scripting\n b) Script site cross\nc) Site cross script\nd) Direct site script \n\n",
    "XSS full form?\n a) Cross site scripting\n b) Script site cross\nc) Site cross script\nd) Direct site script \n\n",
    "XSS full form?\n a) Cross site scripting\n b) Script site cross\nc) Site cross script\nd) Direct site script \n\n",
    "XSS full form?\n a) Cross site scripting\n b) Script site cross\nc) Site cross script\nd) Direct site script \n\n",
    
]

questions = [
     Question(question_quiz[0], "a"),
     Question(question_quiz[1], "a"),
     Question(question_quiz[1], "a"),
     Question(question_quiz[1], "a"),
     Question(question_quiz[1], "a"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("score:", score)

run_quiz(questions)

#Ex. 3:
#2 Calculate the Gross Salary and Net Salary of an employee for following allowance & deduction Using Inheritance.
class Employee:
 def getEmployee(self):
   self.salary = int(input("Enter Employees Basic Salary: "))
   return(self.salary)
class Perks(Employee):
    def calcPerks(self):
        bs=self.getEmployee()
        self.da=bs*0.20
        self.hra=bs*0.1
        self.ta=bs*0.075
        self.emi=bs*0.02
        self.pf=bs*0.12
        self.gs=bs+self.da+self.hra+self.ta
        self.ns=self.gs-self.pf-self.emi
        print("Net Salary:",self.ns)
        print("Gross Salary:",self.gs)
empSalary = Perks()
empSalary.calcPerks()

#Ex4 Data Manipulation Using Pandas
import pandas as pd
#1 Create a dataframe
df = pd.DataFrame({
'RollNo':[1,2,3,4,5,6],
'Name':['Anitha','Brindha','Chithra','Divya','Elakiya','Fathima'],
'Father_Name':['Arun','Bala','Cathu karupu','Dinesh','Eruman','Fareek'],
'year':[2007,2006,2005,2004,2003,2002],
'status':['Daughter','Daughter','Daughter','Daughter','Daughter','Daughter']
})
df['age']=2022-df['year']
df['Father_age']=2*df['age']
df['father_status']=df['Father_age'].apply(lambda x: 'retired' if x>58 else 'not retired')
df['gender']=df['status'].apply(lambda x: 'M' if x =='Son' else 'F')
display(df)

#2 Select columns with specific data types
columns = df.select_dtypes(include=['int'])
print(columns,'\n')

#3 Slicing the dataframe
print(df.loc[0:5,'Father_Name':'year'],'\n')

#4 Select specific values in the column
print(df.iloc[1:2, 1:2],'\n')

#5 Group by Age
print(df.groupby(['age','status']).groups)

#6 Map with dataframe 
df['MARRIED']=df['age'].map(lambda x: 'YES' if x>22 else 'NO')
print(df['MARRIED'])

#7 Rename the column name
df.rename(columns = {'MARRIED':'MARRIED_STATUS'}, inplace = True)
df

#8 Drop columns & rows in the dataframe
df.drop(df.index[1:3], inplace=True)
df.drop(['RollNo'], axis=1,inplace=True)
print(df)

#9 Write/Read as CSV file 
df.to_csv('/content/santhosh_record.csv',index=False)
csv_df = pd.read_csv('/content/santhosh_record.csv')
display(csv_df)

#9 Write/Read as CSV file 
df.to_csv('/content/santhosh_record.csv',index=False)
csv_df = pd.read_csv('/content/santhosh_record.csv')
display(csv_df)

#Ex6. Modular Programming: Scrap news from Hacker News
!pip install pygooglenews

from google.colab import files
uploaded = files.upload()

import news as n
df1=n.scrap_news("hacker news")
display(df1)

!pip install pygooglenews

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
wordcloud = WordCloud(background_color="blue",width=1600, height=800).generate(' '.join(df1['title'].tolist()))
plt.figure( figsize=(12,10), facecolor='k')
plt.imshow(wordcloud)

!pip install scapy

#Ex7.Banner Grabbing Scapy
import socket
import requests
from scapy.all import sniff
#getting ip of domain
hostname = input("Enter the website url (full)")
ip= socket.gethostbyname(hostname)
print(hostname,"\n",ip)
#Banner grabbing
def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(s.recv(1024))
port = str(input("Please enter the port: "))
banner(ip, port)
print(hostname)
#check if vulnerable
domain = "https://www."+hostname
headers= requests.get(domain).headers

if 'X-Frame-Options' in headers:
    print(domain," non - vulnerable")
else:
    print(domain, " vulnerable")

!pip install scapy

pip install pynput

