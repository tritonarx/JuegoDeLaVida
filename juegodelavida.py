def JuegoDeLaVida():
	import time

	cm,fm,ptp=42,42,1600


	tiempo=0.025

	m0=[[0 for x in range(cm)] for y in range(fm)]
	m1=[[0 for x in range(cm)] for y in range(fm)]
	m2=[[0 for x in range(cm)] for y in range(fm)]


	#carga datos en forma x,y\r\r\n
	#datos.txt,honeythieves.txt,pinwheel.txt,quadrupleburloaferimeter2.txt

	def load_data():
		datos=open('/media/thor/AC11-7B29/quadrupleburloaferimeter2.txt','r')
		for line in datos:
			line=line.strip()
			line=line.split(',')

			if int(line[0])<cm and int(line[1])<fm:
				m1[int(line[0])][int(line[1])]=1

		datos.close()	

	def print_load_data():
		b=''
		for x in range(1,cm-1,1):
			s=0
			for y in range(1,fm-1,1):
				if m1[x][y]==1:
					b+= 'm1['+str(x)+']['+str(y)+'] '
					s=1
			if s==1:
				b+='\r\r\n'
		print b


	def ciclo_de_vida():

		for x in range(1,cm-1,1):
			for y in range(1,fm-1,1):
				#Numero de  Vecinos para cierto punto xy	? ? ?
				#											? X ?
				#											? ? ?
				nvecinos=m1[x+1][y]+m1[x-1][y]+m1[x][y+1]+m1[x+1][y+1]+m1[x-1][y+1]+m1[x][y-1]+m1[x+1][y-1]+m1[x-1][y-1]

				if m1[x][y]==0 and nvecinos==3: #Muerto-->Revive?
					m2[x][y]=1

				if m1[x][y]==1:	#Vivo-->Muere?

					if nvecinos<=1:
						m2[x][y]=0
					if nvecinos==2 or nvecinos==3:
						m2[x][y]=1
					if nvecinos>=4:
						m2[x][y]=0

	def vida():
		i=0
		op=0
		ops=0
		while True:

			ciclo_de_vida() 

			time.sleep(tiempo)	
			op=0
			ops=0
			a='N ciclo ['+str(i)+']\r\r\n'	

			for x in range(1,cm*2-2,1):
				a+='_'

			a+='\r\r\n'
			for x in range(1,cm-1,1):
				a+='|'
				for y in range(1,fm-1,1):
					# Compara punto a punto si cambio la matriz
					if m1[x][y]==m2[x][y]:
						op=op+1
					if m0[x][y]==m2[x][y]:
						ops=ops+1

					m0[x][y]=m1[x][y]
					m1[x][y]=m2[x][y]
					# Visualiza los resultados en un string
					if m1[x][y]==1:
						a+='&)'
					if m1[x][y]==0:
						a+='  '
					
				a+='|\r\r\n'
			for x in range(1,cm*2-2,1):
				a+='_'
			a+='\r\r\n----'+' N '+str(i-1)+' ---> N '+str(i)+'  Cambios = '+str(ptp-op)+' -----\r\r\n'
			if ptp==op:
				
				a+= '--------------FIN------------------'+str(ptp-op)
				# Verifica que al aplicar las reglas
				# cambie, en caso contrario termina el proceso
				break
			if ptp==ops:
				a=''
				print '-------FIN----BUCLE OSCILANTE------'+str(ptp-ops)
				break

			print a
			i=i+1

	#############################################################
	#															#
	#############################################################

	load_data()
	print_load_data()
	vida()
	print_load_data()



JuegoDeLaVida()