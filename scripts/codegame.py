import sys, math

n = 5
temps = [9,2,-2,4,5]

#n = 0
#temps = []

comp = 0
#print(temps)

if n > 0:
	comp = int(temps[0])
	#print("Esto es comp=",comp)
	for t in temps:
		diff = abs(t) - abs(comp)
		print("diferencia temperaturas ==>",diff)
		if diff < 0 or (diff == 0 and t > comp):
			print("Esto en t==>",t)
			print("Esto es comp ==>",comp)
			comp = t		
print("Esto es el resultado de comp ==>",comp)			
#print(comp)