a=input("Enter the name  of the student:")
python=int(input("python:"))
java=int(input("java:"))
php=int(input("php:"))
oracle=int(input("oracle:"))
seo=int(input("seo:"))
total=python+java+php+oracle+seo
print(total)
avg=total/5
print(avg)
if(avg>35 and avg<55):
    print("third class")
elif(avg>55 and avg<75):
    print("your second class")
elif(avg>=75 and avg<99):
    print("your first class")
else:
    print("your fail")
