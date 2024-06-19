"""
This is planned to be a Sound-Changeaplier made by Melanie Jones.
"""

import curses

def main_menu(stdscr: curses.window):
    lines = [[" " for _ in range(0xff)] for _ in range(0xff)]

    k = 0
    cursor_x = cursor_y = 0

    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while k != ord('Q'):
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y += 1
        if k == curses.KEY_UP:
            cursor_y -= 1
        if k == curses.KEY_RIGHT:
            cursor_x += 1
        if k == curses.KEY_LEFT:
            cursor_x -= 1
        
        if 0 < k <= 0xff:
            if k == ord('\b'):
                cursor_x -= 1
                lines[cursor_y][cursor_x] = ' '
            elif k == ord('\n'):
                cursor_x = 0
                cursor_y += 1
            else:
                lines[cursor_y][cursor_x] = chr(k)
                cursor_x += 1

        cursor_x = min(width - 1, max(0, cursor_x))
        cursor_y = min(height - 1, max(0, cursor_y))

        stdscr.move(cursor_y, cursor_x)

        for y in range(min(height - 1, len(lines))):
            if y == cursor_y:
                stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, 0, "".join(lines[y]).replace(chr(0), ''))
            if y == cursor_y:
                stdscr.attroff(curses.color_pair(1))

        stdscr.refresh()

        k = stdscr.getch()

def main():
    curses.wrapper(main_menu)

if __name__ == "__main__":
    main()