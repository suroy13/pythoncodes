#problem is create a dictionary with the following keys and values of Hindi word and its meaning in English
# 1. गाड़ी - Car
# 2. घर - House
# 3. किताब - Book
# 4. स्कूल - School
# 5. बगीचा - Garden

Hindi_to_English = { "car": "गाड़ी","house"  : "घर","book": "किताब","school": "स्कूल","garden": "बगीचा" }

# hindiword=input("Enter the Hindi word: ")
# print("The meaning of Hindi word is: ",Hindi_to_English.get(hindiword))
# for i in Hindi_to_English.items():
#     print(i)car
#------------------------------

#problem to take 5 numbers are input and print unique numbers
# numberset=set()
# n=int(input("Enter the number of elements 1: "))
# numberset.add(n)
# n=int(input("Enter the number of elements 2: "))
# numberset.add(n)
# n=int(input("Enter the number of elements 3: "))
# numberset.add(n)
# n=int(input("Enter the number of elements 4: "))
# numberset.add(n)
# n=int(input("Enter the number of elements 5: "))
# numberset.add(n)
# print(numberset)
#------------------------------
#problem to take int and string in set

globalset=set()
numberfirst=int(input("Enter the number: "))
globalset.add(numberfirst)
Stringelement=input("Enter the string: ")
globalset.add(Stringelement)
print(globalset)