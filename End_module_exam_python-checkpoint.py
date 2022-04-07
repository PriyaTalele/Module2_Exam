#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Convert given hrs & mins in second
hour=int(input("Enter hrs here: "))
minutes=int(input("Enter minutes here: "))
second=(hour*3600)+(minutes*60)
print(hour,"hours and",minutes,"minutes are total",second,"second.")


# In[ ]:





# In[3]:


#5) Create class maths:
class Math:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Add(self):
        return self.a+self.b
    def Sub(self):
        return self.a-self.b
    def Mul(self):
        return self.a*self.b
    def Div(self):
        return self.a/self.b
    
    


# In[6]:


x=Math(20,10)


# In[7]:


print(x.Add())
print(x.Sub())
print(x.Mul())
print(x.Div())


# In[ ]:





# In[25]:


#9 Accept String & print only alternate
#characters on a string.
#Ex: this i s a _ test

a = input("Enter the string here:")
for i in a[1:len(a):2]:
    print(i,end='')


# In[32]:


#10.Create menu driven code for
#1) Accept 2 numbers
#2) Add
#3) Sub
#4) Mul
#5) Div
while True:
    a=input(print("1)accept 2 number\n2)add\n3)sub\n4)mul\n5)div\n6)Exit"
        if a == '1'
           b=int(input("enter 1st number: "))
           c=int(input("enter 2nd number:"))
        elif a=='2':
            print("addition of",b,'and',c,'is',b+c)
        elif a=='3':
            print("subtraction of",b,'and',c,'is',b-c)     
        elif a=='4':
            print("multiplication of",b,'and',c,'is',b*c)      
        elif a=='5':
            print("division of",b,'and',c,'is',b/c)     
        elif a=='6':
            print("Exit")
            break
                 


# In[33]:


#Q.6) Read file & count numbers of digit
#alphabets & symbols
#(hint one can compare using ‘a’ < digit <
#‘z‘.
a= input("enter a string")
d=l=s=0
for c in a:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        s=s+1
    print("letters",l)
    print("digits",d)
    print("symbols",s)


# In[20]:


#Q.3) Print pattern
for i in range(1,6):
        for j in range(1,i+1):
            print(j%2,end=" ")
        print()


# In[22]:


#8.print pattern
a='13567'
for i in range(0,len(a)):
  print(a[i]*(i+1))


# 
