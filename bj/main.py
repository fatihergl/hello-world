import time
import os
print((10*'-')+"BlackJack"+(10*'-'))
time.sleep(1)

balance = 100
print("your balance is{balance}$")
time.sleep(1)

os.system('cls||clear')
table = []
table.append(20*'_')
for i in range(1,12):
    temp_string = ''
    temp_string += ('|')
    temp_string += (18*' ')
    temp_string += ('|')
    table.append(temp_string)
table.append(20*'_')
    
for i in table:
    print(i)