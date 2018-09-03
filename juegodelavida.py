import curses

from random import randint
cm,fm,ptp=27,27,625

tiempo=0.025

m0=[[0 for x in range(cm)] for y in range(fm)]
m1=[[0 for x in range(cm)] for y in range(fm)]
m2=[[0 for x in range(cm)] for y in range(fm)]
def load_data():
	#carga datos en forma x,y\r\r\n
	#datos.txt,honeythieves.txt,pinwheel.txt,quadrupleburloaferimeter2.txt
	datos=open('/media/thor/AC11-7B29/sim/pinwheel.txt','r')
	for line in datos:
		line=line.strip()
		line=line.split(',')
		if int(line[0])<cm and int(line[1])<fm:
			m1[int(line[0])][int(line[1])]=1

	datos.close()
def print_load_data():
	b=''
	z=0
	for x in range(1,cm-1,1):
		s=0
		z=0
		for y in range(1,fm-1,1):
			if m1[x][y]==1:
				b+= 'm1['+str(x)+']['+str(y)+'] '
				#win.addstr(x,0,b )
				s=1
				z=z+10
		if s==1:
			win.addstr(28+z, 1+x,b ) 
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

curses.initscr()
win = curses.newwin(108,108, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)
load_data()
print_load_data()

key = ' '  

i=0
op=0
ops=0
key=22
while key != 27 and key != 81 and key != 113:
	win.border(0)
	prevKey = key                                                  # Previous key pressed
	event = win.getch()
	key = key if event == -1 else event
	if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
		key = -1                                                   # one (Pause/Resume)
		while key != ord(' '):
			key = win.getch()
		key = prevKey
		continue

	if key not in [66,98,81,113, 27]:     # If an invalid key is pressed
		key = prevKey
#ver	stdscr.addstr("\n Welcome to JuegoDeLaVida")

	ciclo_de_vida() 
	op=0
	ops=0
	#a='N ciclo ['+str(i)+']\r\r\n'	
	for x in range(1,cm-1,1):
#		a+='|'
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
				win.addstr(x,y*2,'&)')
			if m1[x][y]==0:
				win.addstr(x,y*2,'  ')
	#a+='\r\r\n----'+' N '+str(i-1)+' ---> N '+str(i)+'  Cambios = '+str(ptp-op)+' -----\r\r\n'
	if ptp==op:
		win.addstr(cm,0, '--------------FIN------------------'+str(ptp-op))
				# Verifica que al aplicar las reglas
				# cambie, en caso contrario termina el proceso
		
	if ptp==ops:
		a=''
		#print '-------FIN----BUCLE OSCILANTE------'+str(ptp-ops)
	i=i+1

curses.nocbreak()

curses.echo()
curses.endwin()
