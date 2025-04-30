#read from the file 
f=open("Subhankar.txt","r")
text=f.read()
print(text,type(text))
if (text.__contains__("Subhankar")):
    print("PASS")
else:
    print("FAIL")
f.close()