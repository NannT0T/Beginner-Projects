random_list = []

for i in range (5):
    number = int(input(f"Enter random number {i+1}: "))
    random_list.append(number)

odd_number = []
even_number = []
for i in random_list: 
    if i % 2 != 0:
        odd_number.append(i)
    else:
        even_number.append(i)

print(random_list)
print(odd_number)
print(even_number)
     


    
