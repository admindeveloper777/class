class Point:
	"docstring for ClassName"
	x=1
	y=1

# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))
# pt=Point()
# Point.x=100
# print(pt.x,pt.y)
# print(pt.__dict__)
# print(id(pt),id(Point),sep="\n")

# pt=Point()
# pt.x=3
# pt.y=10
# print(pt.x,Point.x,sep="\n") 
# print(pt.__dict__)
# print(getattr(pt,"x",True)) class qiymatini qaytaradi
# print(getattr(pt,"d",False))
# print(hasattr(pt,"y")) mavjud class qiymatri mavjud bolsa true bolmasa false qiytaradi
# setattr(pt,"D",'XNJNJQW')

# print(pt.__dict__)


# class Salom:
	# def __init__(self,x=0,y=0): 
		# self.x=x
		# self.y=y
	# def __del__(self):
		# print("ochrildi hammasi"+self.__str__())
	"""docstring for ClassName"""
	# x=1; y=1  init metodi 
	# def __init__(self,x=0,y=0):
		# self.a=x
		# self.c=y





# pr=Salom()
# pr1=Salom(3)
# pr2=Salom(0,6)
# pr3=Salom(3,6)

# print(pr.__dict__, pr1.__dict__, pr3.__dict__, pr2.__dict__, sep="\n")

# class Talaba:
# 	"enfcnwefkjgvbpokerogkprkjgpokropgk"
# 	a=1
# 	b=1
# print(Talaba.__name__)
# dt=Talaba()
# dt.a=int(input("sonni kiriting: "))
# dt.b=int(input("sonni kiriting: "))
# setattr(dt,"z",1200000000)
# print((dt.a+dt.b)/dt.z)
# print(getattr(dt,'a'))
# print(hasattr(dt,"d"))
# del dt.a
# print(dt.a)
# print(isinstance(dt,ClassName))









# class Talaba:
# 	def __init__(self,x=0,y=0):
# 		self._x=x
# 		self._y=y
# 	def __checkValue(x):
# 		if(isinstance(x,int) or isinstance(x,float)):
# 			return True
# 		return False				
# 	def setCoords(self,x,y):
# 		if Talaba.__checkValue(x) and Talaba.__checkValue(y):

# 		 self._x=x
# 		 self._y=y
# 		else:
# 			print("dasturda xatolik")
# 	def getCoords(self):
# 			return self._x+self._y





# pt=Talaba(12,15)
# print(pt.getCoords())
# print(pt)

# class CoordValue:
# 	def __get__(self,instance,owner):
# 		return self.__value

# 	def __set__(self,instance,value):
# 		self.__value=value	


# 	def  __delete__(self,obj):
# 		del self.__value	


# class Point:
# 	coordX=CoordValue()
# 	coordY=CoordValue()
# 	def __init__(self,x=0,y=0):
# 		self.coordX=x
# 		self.coordY=y

	# def __checkValue(x):
	# 	if isinstance(x,int) or isinstance(x,float):
	# 		return True
	# 	return False	
	# @property	
	# def coordX(self):
	# 	return self._x
	# @coordX.setter	
	# def coordX(self,x):
	# 	if Point.__checkValue(x):
	# 		self._x=x
	# 	else:
	# 		raise ValueError("xatolik formati")	
	# @coordX.deleter		
	# def coordX(self):
	# 	print("malumotlar ochrildi")
	# 	del self._x			

	#  coordX=property(__getCoords,__setCoords,__delCoords)	
# pt=Point(1,2)
# pt.coordX=342
# pt.coordY=569556
# print(pt.coordX,pt.coordY)





# class Itdasturchi:
# 	def __init__(self,ismi,yonalish,boshlagan_yoshi,pensiya_vaqti):
# 		self.ismi=ismi
# 		self.yonalish=yonalish
# 		self.boshlagan_yoshi=boshlagan_yoshi
# 		self.pensiya_vaqti=pensiya_vaqti

# 	def __str__(self):
# 		return("Ismi:\t"+self.ismi+"Yonalishi:\t"+self.yonalish+"Boshlagan_yoshi:\t")+self.boshlagan_yoshi+"Pensiya vaqti:\t"+self.pensiya_vaqti

# dasturchilist=[]
# while True:
# 		print("1-dasturchi qoshish\n2-dasturchi royhatni chiqarish\n3-yonalishi boyicha tartiblash\n4-boshlagan vaqti boyicha tartiblash\n5-pensiya vaqti boyicha\nq-quit")

# 		cmd=input()
# 		if cmd=="1":
# 			ismi=input("FISHni kiriting: ")
# 			yonalish=input("yonalishini kiriting: ")
# 			boshlagan_yoshi=input("Boshlagan_yoshini kiriting: ")
# 			pensiya_vaqti=input("Pensiya_vaqti: ")


# 			st=Itdasturchi(ismi,yonalish,boshlagan_yoshi,pensiya_vaqti)
# 			dasturchilist.append(st)

# 		elif cmd=="2":

# 			print("__________________Itdasturchi royhati_____________________")

# 			for st in dasturchilist:
# 				print(st)
# 			print("_______________________________________________")
			

# 		elif cmd=="3":
							
# 			stlist=dasturchilist
# 			stlist.sort(key=lambda x:x.yonalish)


# 			for i in stlist:
# 				print(i)

# 		elif cmd=="4":

# 			stlist=dasturchilist
# 			stlist.sort(key=lambda x:x.boshlagan_yoshi)

# 			for i in stlist:
# 				print(i)

# 		elif cmd=="5":
# 			stlist=dasturchilist
# 			stlist.sort(key=lambda x:x.pensiya_vaqti)


# 			for i in stlist:
# 				print(i)
		

# 		elif cmd=="q":
# 			break






class Student:

	def __init__(self,name,age,bosqichi):
		self.name=name
		self.age=age
		self.bosqichi=bosqichi
	def __str__(self):

		return f"ismi:{self.name}\nyoshi:{self.age}\n kursi{self.bosqichi}"

list=[]
while True:
	print("1-royhatga qoshing\n2-Ismi boyicha royhati\n2.1-ismi boyicha tartiblash\n3-yoshi boyicha tartiblash\n4-kursi boyicha tartiblash\nq-quit")

	cmd=input()
	if cmd=='1':
		
		name=input("FISHni kiriting: ")
		age=input("yoshini kiriting: ")
		bosqichi=input("Kursini kiriting: ")



		st=Student(name,age,bosqichi)
		list.append(st)

	elif cmd=='2':

		print("___________Studentlar royhati_________")

		for st in list:
			print(st)
		print("_____________________________")
	
	elif cmd=='2.1':
		stlist=list
		stlist.sort(key=lambda x:x.name)			

	elif cmd=='3':
		stlist=list
		stlist.sort(key=lambda x:x.age)
		for i in stlist:
			print(i)

	elif cmd =='4':
		stlist=list
		stlist.sort(key=lambda x:x.bosqichi)			
		for i in stlist:
			print(i)

	elif cmd=='q':
		break		