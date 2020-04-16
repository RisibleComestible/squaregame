"""Square Game by u/RisibleComestible. Run from the command line: python squaregame.py 30
if you want the moves limit to be 30. The object is to make the randomly generated
active square contain the same numbers as the target square within the moves limit.
You select one element each move and may add or subtract the value of adjacent elements.
Press "q" to quit."""

import curses
import random
import sys
screen = curses.initscr()
curses.cbreak()
curses.noecho()
screen.keypad(1)


def mainloop():
    moves = int(sys.argv[1])
    try:
        target_string = []
        active_string = []
        for i in range(9):
            target_string.append(str(random.randint(0, 9)))
            active_string.append(str(random.randint(0, 9)))

        screen.vline(2, 12, curses.ACS_VLINE, 10)
        screen.vline(2, 22, curses.ACS_VLINE, 10)
        screen.hline(4, 2, curses.ACS_HLINE, 30)
        screen.hline(8, 2, curses.ACS_HLINE, 30)

        screen.vline(2, 52, curses.ACS_VLINE, 10)
        screen.vline(2, 62, curses.ACS_VLINE, 10)
        screen.hline(4, 42, curses.ACS_HLINE, 30)
        screen.hline(8, 42, curses.ACS_HLINE, 30)

        screen.addstr(2, 7, target_string[0])
        screen.addstr(2, 17, target_string[1])
        screen.addstr(2, 27, target_string[2])
        screen.addstr(6, 7, target_string[3])
        screen.addstr(6, 17, target_string[4])
        screen.addstr(6, 27, target_string[5])
        screen.addstr(10, 7, target_string[6])
        screen.addstr(10, 17, target_string[7])
        screen.addstr(10, 27, target_string[8])
        screen.addstr(2, 47, active_string[0])
        screen.addstr(2, 57, active_string[1])
        screen.addstr(2, 67, active_string[2])
        screen.addstr(6, 47, active_string[3])
        screen.addstr(6, 57, active_string[4])
        screen.addstr(6, 67, active_string[5])
        screen.addstr(10, 47, active_string[6])
        screen.addstr(10, 57, active_string[7])
        screen.addstr(10, 67, active_string[8])

        screen.addstr(13, 15, "Target")
        screen.addstr(13, 55, "Active")
        screen.addstr(16, 29, "Remaining moves: " + str(moves))

        screen.addstr(20, 15, "Choose an element of the active square, 1 to 9:")
        screen.refresh()
        key = 'X'

        while key != ord('q'):
            screen.addstr(20, 15, "Choose an element of the active square, 1 to 9:")
            key = screen.getch()
            screen.addch(20,63,key)
            if key in (ord('1'),ord('2'),ord('3'),ord('4'),ord('5'),ord('6'),ord('7'),ord('8'),ord('9')):
                screen.addstr(20, 15, '                                                     ')
                screen.refresh()
                screen.addstr(20, 15, "Choose an adjacent element:")
                first_key = key
                element_value = active_string[int(chr(key))-1]
                key = screen.getch()
                if (first_key == ord('1') and key in (ord('2'), ord('4'))) or (first_key == ord('2') and
                key in (ord('1'), ord('3'), ord('5'))) or (first_key == ord('3') and
                key in (ord('2'), ord('6'))) or (first_key == ord('4') and
                key in (ord('1'), ord('5'), ord('7'))) or (first_key == ord('5') and
                key in (ord('2'), ord('4'), ord('6'), ord('8'))) or (first_key == ord('6') and
                key in (ord('3'), ord('5'), ord('9'))) or (first_key == ord('7') and
                key in (ord('4'), ord('8'))) or (first_key == ord('8') and
                key in (ord('5'), ord('7'), ord('9'))) or (first_key == ord('9') and
                key in (ord('6'), ord('8'))):
                    adjacent_element_value = active_string[int(chr(key))-1]
                    screen.addstr(20, 15, '                                                     ')
                    screen.refresh()
                    screen.addstr(20, 15, "Add or subtract (a or s):")
                    key = screen.getch()
                    if key == ord('a'):
                        new_element = int(element_value) + int(adjacent_element_value)
                        active_string[int(chr(first_key))-1] = str(new_element) + '  '
                        if int(chr(first_key))-1 == 0:
                            screen.addstr(2, 47, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 1:
                            screen.addstr(2, 57, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 2:
                            screen.addstr(2, 67, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 3:
                            screen.addstr(6, 47, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 4:
                            screen.addstr(6, 57, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 5:
                            screen.addstr(6, 67, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 6:
                            screen.addstr(10, 47, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 7:
                            screen.addstr(10, 57, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 8:
                            screen.addstr(10, 67, active_string[int(chr(first_key))-1])
                        moves -= 1
                    if key == ord('s'):
                        new_element = int(element_value) - int(adjacent_element_value)
                        active_string[int(chr(first_key))-1] = str(new_element) + '  '
                        if int(chr(first_key))-1 == 0:
                            screen.addstr(2, 47, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 1:
                            screen.addstr(2, 57, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 2:
                            screen.addstr(2, 67, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 3:
                            screen.addstr(6, 47, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 4:
                            screen.addstr(6, 57, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 5:
                            screen.addstr(6, 67, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 6:
                            screen.addstr(10, 47, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 7:
                            screen.addstr(10, 57, active_string[int(chr(first_key))-1])
                        if int(chr(first_key))-1 == 8:
                            screen.addstr(10, 67, active_string[int(chr(first_key))-1])
                        moves -= 1

            screen.refresh()
            screen.addstr(20, 15, '                                                        ')
            screen.refresh()
            flag = 0
            for i in range(9):
                if int(active_string[i]) != int(target_string[i]):
                    flag = 1
            if flag == 0:
                screen.addstr(24, 29, "Victory! Well done.")
            screen.refresh()
            if moves == 0 and flag == 1:
                screen.addstr(24, 29, "Defeat! You are out of moves.")
                screen.refresh()
            screen.addstr(16, 29, "Remaining moves: " + str(moves) + '  ')
            screen.refresh()

    finally:
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()


mainloop()