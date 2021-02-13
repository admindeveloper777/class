# kubini chiqaryuvchi funksiya]
            # import math
           # a=float(input("sonni kiriting: "))
# b=float(input("sonni kiriting: "))
# c=float(input("sonni kiriting: "))
# d=float(input("sonni kiriting: "))
# f=int(input("sonni kiriting: "))
# def myfunc(a,b,c,d,f):
# 	return f"{a**3},\n{b**3},\n{c**3},\n{d**3},\n{f**3}"
	
# print(myfunc(a,b,c,d,f,),)

       # kvadrati kubi tortinchi darajalarini chiqaruvchi dasturt

# def power(a,b,c):
# 	return a**2,a**3,a**4,b**2,b**3,b**4,c**2,c**3,c**4


	#orta arifmertik
# def son(a,b,c,d):
	# return (a+b)/2,(a+c)/2,(a+d)/2,math.sqrt(a*b),math.sqrt(a*c),math.sqrt(a*d)

# print(son(a,b,c,d))	


# x=lambda Triangle:a
# print("perimetr: ",a*3)
# print("yuzasi: ",(a*a)/2*0.87)







print("Dostlar royhatini tuzamiz!!!!!!!!!!!! ")

ismlar=[]
n=1
while True:
	ism=input(f"{n}-dostingizni qoshing: ")
	ismlar.append(ism)
	takrorlash=input("yana dostingizni qoshaszmi?\n(ha/yoq)\t:")
	n+=1

	if takrorlash !='ha':
		break


print("Dostlar royhati")

for ism in ismlar:
	print(ism.title())	