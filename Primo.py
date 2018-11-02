#!usr/bin/python3

p = True
n = 0
a = 0
c = 0
num_test = []
log = open("log_Primo.txt", "w")
i = 0

n = input("Qual numero você deseja testar? ")

while(a < int(n)):
	a = a + 1
	z = int(n)/a
	num_test.append(str(a)+" = "+str(z) + '\n')
	if(str(z)[-1] == "0"):
		c = c + 1
if(c == 2):
	print("         +----------------+")
	print("         |     É primo    |")
	print("         +----------------+")
else:
	print("         +--------------------+")
	print("         |     Não é primo    |")
	print("         +--------------------+")
log.writelines(num_test)
log.close
