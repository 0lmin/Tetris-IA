# Structure of files

 For a better maintanability and a better code, the python sources is split between several files.

Here is what structure we plan to use :

# Tetris-IA.py

This is the entry point of a normal user. In this file there is the management of initial input (args + CLI/GUI). Then this script only initiate Player-X class and the Core.

# Player-X.py

files `Player-HUMAN.py`, `Player-DUMB.py`, `Player-RANDOM.py`, `Player-IA_DARWIN.py`, `Player-IA_MCxx.py`, ...

Only contain specific methods about input (key/gamepad by human or emulated by IA), here is a list :
 * lorem
 * ipsum
 * ...

OR (it is not decided) => It could have a part for interaction (input/output handeling), and another part for just the brain/decision code (mostly depend of the size of "input/ouput handeling" module-side).

# Core.py
Core of the game, call display, call player and calculate new position, new tick, new piece ...

# MainMenu.py
It is a file that contain the first page of the application, it only contain a form and return params entered by the user if triggered (do not pass here if use of --NO-GUI).

# GameUI.py
Contain everything to display a game (can be split in 2 surface : board/info).

Should have 2 or 3 instances? (Graphical, CLI, (and No))

# PauseMenu.py ?
Is there a pause menu? (NOT IN MVP)
