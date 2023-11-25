# შექმენით random password generator პროგრამა რომელშიც დაგენერირდბა პაროლი, 
# 8 სიმბოლოიანი, სადაც აუცილებლად 2 სიმბოლო იქნება !##%(#)^#, 2 სიმბოლო იქნება აბგქწეკჯასკჯქწე , 
# 4 სიმბოლო იქნება ციფრები 215346347347
# მაგ: !n8391k*


import random
my_arr = []
symbols = ["!", "@", "#", "4", "$", "^", "&", "*", ":", "?"]
chars = ["z", "s", "d", "f", "g", "r", "t", "u", "c", "n"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(4):
     my_arr.append(random.choice(numbers))
for i in range(2):
     my_arr.append(random.choice(symbols))
     my_arr.append(random.choice(chars))

finally_password = ""
for i in range(len(my_arr)):
     current_chars = random.choice(my_arr)
     finally_password += current_chars
     my_arr.remove(current_chars)

print (finally_password)
