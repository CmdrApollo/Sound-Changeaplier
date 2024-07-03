"""
This is planned to be a Sound-Changeaplier made by Melanie Jones.
"""

import curses
from phoneme_chart import *

print(get_symbol(Place.ALVEOLAR, Manner.NASAL))

place_dict = {
    'l': Place.BILABIAL,
    'a': Place.ALVEOLAR,
    'pa': Place.POST_ALVEOLAR,
    'p': Place.PALATAL,
    'v': Place.VELAR,
    'u': Place.UVULAR,
    'g': Place.GLOTTAL
}

manner_dict = {
    's': Manner.STOP,
    'f': Manner.FRICATIVE,
    'af': Manner.AFFRICATE,
    'n': Manner.NASAL,
    'l': Manner.LATERAL,
    'ta': Manner.TAP,
    'tr': Manner.TRILL,
    'ap': Manner.APPROXIMANT
}

def main_menu(stdscr: curses.window):
    phonemes = []

    user_input = ""

    k = 0

    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def parse(command: str):
        elements = command.lower().strip().split(' ')

        cmd = elements[0]

        match cmd:
            case 'add':
                place = elements[1]
                manner = elements[2]
                voiced = True if elements[3] == '+' else False

                if place == '-':
                    for i in range(7):
                        phonemes.append((i, manner_dict[manner] - 1, voiced))

                elif manner == '-':
                    for i in range(8):
                        phonemes.append((place_dict[place] - 1, i, voiced))
                        
                else:
                    phonemes.append((place_dict[place], manner_dict[manner], voiced))

            case 'rm':
                place = elements[1]
                manner = elements[2]
                voiced = True if elements[3] == '+' else False

                rem = []

                if place == '-':
                    for i in range(7):
                        rem.append((i, manner_dict[manner], voiced))

                elif manner == '-':
                    for i in range(8):
                        rem.append((place_dict[place], i, voiced))
                        
                else:
                    rem.append((place_dict[place], manner_dict[manner], voiced))

                for element in rem:
                    if element in phonemes:
                        phonemes.remove(element)

    while k != ord('Q'):
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        if 0 < k <= 0xff:
            if k == ord('\b'):
                user_input = user_input[:len(user_input) - 1]
            elif k == ord('\n'):
                parse(user_input)
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

        for j in range(8):
            stdscr.addstr(j * 3 + 3, 1, ['Stop', 'Fricative', 'Affricate', 'Nasal', 'Lateral', 'Tap', 'Trill', 'Approx.'][j])
        for p in range(7):
            stdscr.addstr(1, p * 11 + 11, ['Bilabial', 'Alveolar', 'Post-Alv.', 'Palatal', 'Velar', 'Uvular', 'Glottal'][p])
        
        for phoneme in phonemes:
            p = phoneme[0]
            m = phoneme[1]
            v = phoneme[2]

            if not v:
                ch = get_symbol(p, m, v)
                if ch != '*':
                    stdscr.addstr(m * 3 + 3, p * 11 + 11, ch)
            else:
                ch = get_symbol(p, m, v)
                if ch != '*':
                    stdscr.addstr(m * 3 + 3, p * 11 + 14, ch)

        stdscr.addstr(height - 2, 1, '>>> ' + user_input)

        stdscr.refresh()

        k = stdscr.getch()

def main():
    curses.wrapper(main_menu)

if __name__ == "__main__":
    main()