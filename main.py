dia = int(input())
mes = int(input())
if mes == 1:
	if dia > 0 and dia <= 20:
	    print("capricornio")
	elif dia > 20 and dia <= 31:
		print("acuario")
	else:
		print("Dia incorrecto")
elif mes == 2:
	if dia > 0 and dia <= 19:
		print("acuario")
	elif dia > 19 and dia <= 31:
		print("piscis")
	else:
		print("Dia incorrecto")
elif mes == 3:
	if dia > 0 and dia <= 20:
		print("piscis")
	elif dia > 20 and dia <= 31:
		print("aries")
	else:
		print("Dia incorrecto")
elif mes == 4:
	if dia > 0 and dia <= 20:
		print("aries")
	elif dia > 20 and dia <= 31:
		print("Tu signo es Tauro")
	else:
		print("Dia incorrecto")
elif mes == 5:
	if dia > 0 and dia <= 20:
		print("tauro")
	elif dia > 20 and dia <= 31:
		print("geminis")
	else:
		print("Dia incorrecto")
elif mes == 6:
	if dia > 0 and dia <= 2:
		print("geminis")
	elif dia > 21 and dia <= 31:
		print("cancer")
	else:
		print("Dia incorrecto")
elif mes == 7:
	if dia > 0 and dia <= 22:
		print("cancer")
	elif dia > 22 and dia <= 31:
		print("leo")
	else:
		print("Dia incorrecto")
elif mes == 8:
	if dia > 0 and dia <= 23:
		print("leo")
	elif dia > 23 and dia <= 31:
		print("virgo")
	else:
		print("Dia incorrecto")
elif mes == 9:
	if dia > 0 and dia <= 22:
		print("virgo")
	elif dia > 22 and dia <= 31:
		print("libra")
	else:
		print("Dia incorrecto")
elif mes == 10:
	if dia > 0 and dia <= 22:
		print("libra")
	elif dia > 22 and dia <= 31:
		print("escorpio")
	else:
		print("Dia incorrecto")
elif mes == 11:
	if dia > 0 and dia <= 22:
		print("escorpio")
	elif dia > 22 and dia <= 31:
		print("sagitario")
	else:
		print("Dia incorrecto")
elif mes == 12:
	if dia > 0 and dia <= 21:
		print("sagitario")
	elif dia > 21 and dia <= 31:
		print("capricornio")
	else:
		print("Dia incorrecto")
else:
	print("Mes incorrecto")