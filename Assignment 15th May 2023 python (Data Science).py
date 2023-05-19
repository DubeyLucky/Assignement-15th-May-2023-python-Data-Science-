#!/usr/bin/env python
# coding: utf-8

# Q1. How do you comment code in Python? What are the different types of comments?

# In[ ]:


In python we can use # or """""" for comment. There are two types of comment in python. First one # and Second one """""".
If you want to use signle line comment then we use # for ex. #This is comment for single line
and multiple line we use """""" or # for ex. """THis is multiple line comment THis is multiple line comment THis is multiple line comment THis is multiple line comment THis is multiple line comment """


# Q2. What are variables in Python? How do you declare and assign values to variables?

# In[9]:


#A variable is a string of characters and numbers associated with a piece of information. 


# How do you declare and assign values to variables?

# In[17]:


# declare an integer variable
x = 2
y = 4
print(x,y)


# declare a string variable

s = "Lucky"
print(s)

# declare a float variable

f = 4.5
print(f)


# Q3. How do you convert one data type to another in Python?

# In[18]:


x = 4 #integer type data
y = 4.5 #float type data
z = x + y   
print(z)   

#output of z will be 8.5 and it is float


# Q4. How do you write and execute a Python script from the command line?

# You need to open a command line and type the word python followed by the path to your script file like this: python first_script.py Hello World! Then you hit the ENTER button from the keyboard

# Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].

# In[5]:


my_list = [1, 2, 3, 4, 5]



# In[11]:


my_list[1:3]


# Q6. What is a complex number in mathematics, and how is it represented in Python?

# Complex numbers are the numbers that are expressed in the form of a+ib where, a,b are real numbers and 'i' is an imaginary number called “iota”
# 

# In[13]:


a = 3 + 6j
print(type(a))


# Q7. What is the correct way to declare a variable named age and assign the value 25 to it?

# In[3]:


age = 25
print(age)


# Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable
# belong to?

# In[5]:


price = 9.99
print(type(price))


# Q9. Create a variable named name and assign your full name to it as a string. How would you print the
# value of this variable?

# In[6]:


name = input("Enter your full name: ")
print(name)


# Q10. Given the string "Hello, World!", extract the substring "World".

# In[22]:


s = "Hello, World!"
s[6:12]


# Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are
# currently a student or not.

# In[32]:


is_student = int(input("Enter your roll number"))
if is_student == 23:
    print(True)
else:
    print(False)


# In[ ]:




