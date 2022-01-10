print(""" Sayı tutma oyunu 
              """)
print("-"*30)
import random
a = random.randint(0,100)
c = int(input("sayı giriniz: "))
if a == c:
	print(a, "dogru sayı girdiniz")
else:
	print("yanliş sayı doğru sayî" , a)
