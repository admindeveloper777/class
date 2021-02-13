# d=0
# n=int(input("qiymat kiriting: "))
# for x in range(1,n):
# 	s=pow(x,2)
# 	print("sonni darajalari qiymati:",s)
# 	d+=s	
# print("sonnlar yegindisi :",d)

# list=["saman","jim","toby","aziz","lobar","qobil"]
# list[2]="omon"
# list.insert(1,"kelly")
# print(list.index("lobar"))


# cordinatas=(2,3),(4,5),(6,7)

# print(type(cordinatas))



# def say(name,age):
# 	print("hello" +  name, "\nyoshingiz" + age+" da")
# say(" shoxruh"," 23")	
# say(" azim"," 61")
# from math import*
# def cube(num):
# 	return (num*num*num*num)/14
# res=cube(20)
# print((res))	

# is_male=True
# if is_male:
# 	print("siz erkakmisiz? yes/no ")
# 	is_male=input("tanleng: ")
# 	if is_male=="yes":
# 		print("ulug siz erkak emassiz togri tanleng !!!!!!!!!")
# 	else:
# 		print("xato")


# def my_max(num1,num2,num3):
# 	if num1!=num2 and num1>=num3:
# 		return num1
# 		# print("birinchi son kotta")
# 	elif num2>=num1 and num2>=num3:
		
# 		return num2
# 		# print("ikkinchi son kotta")
# 	else:
# 		return num3
# 		# print("uchinchi son kotta")
# print(my_max(2,20,2))


# num1=float(input("Enter first number: "))
# op=input("Enter operator: ")
# num2=float(input("Enter second number: "))
# if op=="+":

# 	print(num1+num2)
# elif op=="-":
# 	print(num1-num2)
# elif op=="*":
# 	print(num1*num2)
# elif op=="/":
# 	try:
# 	  s=num1/num2
# 	  print(s)
# 	except:
# 		print("NOLGA BOLIB QOYILDI")
# elif op=="**":
# 	print(num1**num2)


# else:
# 	print("xatolik yuz berdi!!!")		



#415 17 guruh talabalari royxati
talaba = {
	
 " num1 ":" Ahmedov Elbek", 
 " num2 ":" Botirjonov Ismoil",
 " num3 ": "Boboqulov Atham",
 " num4 ":" Isoyev Temur",
 "num5 ": "Yuldashev Kamoliddin",
 "num6 ":"Yuldashev Kamoliddin",
 "num7 ": "Raximov Abdug'ofur",

}
# talaba=input("Talaba nomerini kiriting: ")
# if talaba=="num1":
# 	print(" Ahmedov Elbek")
# elif talaba=="num2":
# 	print(" Botirjonov Ismoil")	
# elif talaba=="num3":
# 	print("Boboqulov Atham")	
# elif talaba=="num4":
# 	print(" Isoyev Temur")	
# elif talaba=="num5":
# 	print("Yuldashev Kamoliddin")	
# elif talaba=="num6":
# 	print("Yuldashev Kamoliddin")	
# elif talaba=="num7":
# 	print("Raximov Abdug'ofur")		
# else:
	# print("Bunday talaba yoq!!!!")



# say="salom"
# all=""
# all_count=0
# all_limit=3
# yutqiz=False
# while say!=all and not(yutqiz):
# 	if all_count<all_limit:

#  	    all = input("sozni kiriting: ")
#  	    all_count += 1 
# 	else:
# 		yutqiz = True
 	
#  	# print("Xatolik yuz berdi boshqaatan kiriting !!!")
# if yutqiz:
# 	print("urinsh yakunlandi Siz yutqazdingiz")
# else:
# 	print("siz yutdingiz!!!!")
#  



# son topish oyini

# yashirin_son="120"
# kirit_son=""
# imkon=0
# limit=5
# yutqiz=False

# while yashirin_son != kirit_son and not(yutqiz):
# 	if imkon<limit:
# 		kirit_son=input("sonni kiriting: ")
# 		# print("topolmadingiz!!!!!!!")
# 		imkon +=1
# 	else:
# 		yutqiz=True

# if yutqiz:
# 	print("imkoninigiz tugadi Siz yutqazdingiz!!!!!")
# else:
# 	# print("topdingiz!!!!!!!")
# 	print("Siz yutdingiz Tabriklaymiz!!!!!!")		

# for soz in "hammaga salom":
	# print(soz[::2])

# try:
# 	anse=10/0
# 	num=int(input("sonni kiriting: "))
# 	print(anse)
# except ZeroDivisionError as err:
# 	print(err)
# except ValueError:
# 	print("xatolik")



# em=open("salyut.txt","w")
# em.write("azizlar salom barchaga ")

# print(em)
# em.close()	

# sd=open("aziz.html","w")
# sd.write("salom barcaga")
# print(sd)
# class Student():
		
# 	def __init__(self,name,major,age):
# 		self.name=name
# 		self.major=major
# 		self.age=age
# 		# s=input("qiymatini kiriting: ")
# 	def func(self):
# 		return str(f"{self.name} \n{self.major} \n{self.age}")
# talaba=Student("aziz","raximov","26")
# talaba2=Student("rustiy","azizov","30")

# print(talaba.func())				


from tkinter import*
class But_print:
	
	def __init__(self):
		self.but=Button(root)	
		self.but["text"]="salom"
		self.but=Label(root)
		self.but.bind("<Button-1>",self.printer)
		self.but.pack()
	def printer(self,event,e):
		e["text"]="salomlar"
		e.grid(row=0,column=0)
		e.pack()
		print(e)
root=Tk()
obj=But_print()
root.mainloop()