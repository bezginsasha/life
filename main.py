import curses
import time

stdscr = curses.initscr()
win_width = curses.COLS
win_height = curses.LINES

stdscr.addstr(0,0,'$')
stdscr.addstr(1,1,'$')
stdscr.addstr(2,2,'$')
stdscr.refresh()
time.sleep(2)

stdscr.addstr(0,0,'%')
stdscr.addstr(1,1,'%')
stdscr.addstr(2,2,'%')
stdscr.refresh()
time.sleep(2)