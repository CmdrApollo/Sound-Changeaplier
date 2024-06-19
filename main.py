"""
This is planned to be a Sound-Changeaplier made by Melanie Jones.
"""

import curses
from phoneme_chart import *

print(get_symbol(Place.ALVEOLAR, Manner.NASAL))

def main_menu(stdscr: curses.window):
    user_input = ""

    k = 0

    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while k != ord('Q'):
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        if 0 < k <= 0xff:
            if k == ord('\b'):
                user_input = user_input[:len(user_input) - 1]
            elif k == ord('\n'):
                user_input = ''
            else:
                user_input += chr(k)

        stdscr.border()
        for x in range(width - 2):
            stdscr.addch(height - 3, x + 1, '─')
        for j in range(9):
            for x in range(87):
                stdscr.addch(j * 3 + 2, x + 1, '─')
        for i in range(8):
            for y in range(min(25, height - 4)):
                stdscr.addch(y + 1, i * 11 + 10, "│")

        for p in range(7):
            stdscr.addstr(1, p * 11 + 11, ['Bilabial', 'Alveolar', 'Post-Alv.', 'Palatal', 'Velar', 'Uvular', 'Glottal'][p])
            for m in range(8):
                ch = get_symbol(p + 1, m + 1, False)
                if ch != '*':
                    stdscr.addstr(m * 3 + 3, p * 11 + 11, ch)
                ch = get_symbol(p + 1, m + 1, True)
                if ch != '*':
                    stdscr.addstr(m * 3 + 3, p * 11 + 14, ch)

        stdscr.addstr(height - 2, 1, '>>> ' + user_input)

        stdscr.refresh()

        k = stdscr.getch()

def main():
    curses.wrapper(main_menu)

if __name__ == "__main__":
    main()