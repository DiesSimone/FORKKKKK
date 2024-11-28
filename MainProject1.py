from operator import truediv

print("ciao mondo!")
x = 10
print(x)

stringa = "Kebab"
print(stringa)

print(f"hello {stringa}")

is_Student = True

if x ==1:
    print("is a student")
else:
    print("is not a student")

#data type

print(type(x))

gpa = 10.5

print(type(gpa))

gpa = (int(gpa))

print(type(gpa))

name = input("what is your name? : ")

age = input("what is your age? : ")
age =int(age)+1
print(f"your name is {name} and your are {age} years old")



#triangle area calculator

base = input("inserisci la base : ")
altezza = input("inserisci l'altezza : ")

area = (int(base)*int(altezza))/2

print(f"area = {area}")

#secondo metodo
base1 = float(input("inserisci la base : "))
altezza1 = float(input("inserisci l'altezza : "))

area1 = (base1*altezza1)/2

print(f"area = {area1}")