dict1={
"name": 'Subhankar',
"age":'37',
"mobile":9477426909,
"department":"QEA"
}

for x in dict1:
    print(x)

for x in dict1:
    if (dict1.get("mobile").__eq__(9477426807)):
        print("PASS")
        break
    else:
        print("FAIL")
        break
    #test