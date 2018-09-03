	def main():
		import curses
		stdscr = curses.initscr();
		running=True;
		stdscr.addstr("\n Para comenzar ingrese 'b' (Begin) | para finalizar ingrese 'q' (Exit)\n  =>");
		while(running):	
			key = stdscr.getch();
			if (chr(key) == "q"):
				running = False;
			if (chr(key) == "b"):
				curses.noecho(); 
				load_data();
				vida();
				print_load_data()
				key = stdscr.getch();
				running=False;
			else:
				stdscr.addstr("\n Para comenzar ingrese 'b' (Begin) | para finalizar ingrese 'q' (Exit)\n  =>");
		curses.nocbreak();
		stdscr.keypad (0);		curses.endwin();

		curses.echo();
		return 0;
	if (__name__== "__main__"):	
		main();

JuegoDeLaVida()
