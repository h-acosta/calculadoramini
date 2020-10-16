print("^ LA CALCULADORA ^")
elige = int(input("Que quieres usar: " + "\n SUMA-1" + "\nRESTA-2" + "\nMULTIPLICACION-3 " + "\n"))
if elige == 1:
	primernums = int(input("Introduce el primer numero a sumar: "))
	segunnums = int(input("Indruce el segundo numero a sumar: "))
	resultado = primernums + segunnums
	resultado = str(resultado)
	print("El resultado de la suma es: " + resultado)
elif elige == 2:
	primernumr = int(input("Introduce el primer numero a restar: "))
	segunnumr = int(input("Introduce el segundo numero a restar: "))
	resultado2 = primernumr - segunnumr
	resultado2 = str(resultado2)
	print("El resultado de la resta es: " + resultado2)
elif elige == 3:
	primernumm = int(input("Introduce el primer numero a multiplicar: "))
	segunnumm = int(input("Introduce el segundo numero a multiplicar: "))
	resultado3 = primernumm * segunnumm
	resultado3 = str(resultado3)
	print("El resultado de la multiplicacion es: " + resultado3)
else:
	print("Introdusca un numero valido por favor")