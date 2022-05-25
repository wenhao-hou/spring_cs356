# cs357_Command

Consider a very simple graphic editor that only knows how to draw a square and to perform a few manipulations on the square: to set the square color, to translate the square, and to rotate the square.

Define a class, Command, to represent the above commands. Include "metacommands" such as history (to see previous commands), undo (to undo previous commands) and redo (to repeat the previous command) in your class. Define a class, CommandManager, to control the execution of all these commands. The number of commands that can be seen with "history" and undone with "undo" can be bounded.

Design, code and test a driver that executes a sequence of predetermined commands interleaved by a time interval long enough to perceive the effect of a command in the graphic editor.

Be sure to use docstrings and function annotations.

Write unit tests to test your code.
