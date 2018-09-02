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
			stdscr.addstr("\n Welcome to Game");
			load_data();
			vida();
			print_load_data()
		else:
			stdscr.addstr("\n Para comenzar ingrese 'b' (Begin) | para finalizar ingrese 'q' (Exit)\n  =>");
	curses.nocbreak();
	stdscr.keypad (0);
	curses.echo();
	curses.endwin();
	return 0;
if (__name__== "__main__"):	
	main();
