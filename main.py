#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
list1=[]
list2=[]
list3=[]

for i in range (0,nr_letters):
  num=random.randint(0,len(letters)-1)
  
  result1=letters[num]
  list1.append(result1)
  
for i in range(0,nr_symbols) :
  num2=random.randint(0,len(numbers)-1)
  result2=numbers[num2]
  list2.append(result2)

for i in range(0, nr_numbers) :
  num3=random.randint(0,len(symbols)-1) 

  result3=symbols[num3]  
  list3.append(result3)

concant_list= list1+list2+list3
for char in concant_list:
  print(char,end="")
print("\n")  
  


list4=[]
for i in range(0,len(concant_list)):
  choose= random.randint(0,len(concant_list)-1)
  password=concant_list[choose]
  list4.append(password)

for char2 in list4:
  print(char2 , end="")
    







#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&