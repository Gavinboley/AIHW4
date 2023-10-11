# Minimax Algorithm for Four-in-a-Row Game
Nina Rubanovich, Jade Neeley, Gavin Boley 

Implementation:

Minimax algorithm to play a two-player, four-in-a-row game, a variation of tic-tac-toe: two players, X and O, take turns marking the spaces in a 5×6 grid. The player who succeeds in placing 4 of their marks consecutively in a horizontal, vertical, or diagonal row wins the game. A player may place a piece at any empty space next to an existing piece horizontally, vertically, or diagonally on the board. Ties are broken in increasing order of column number first (smaller column number has higher priority) and then increasing order of row number (smaller row number has higher priority). The two AI players follow the same heuristic function, and start at different positions.

Heuristic used:

h(n) = 200*[number of two-side-open-3-in-a-row for me]
– 80*[number of two-side-open-3-in-a-row for opponent]
+ 150*[number of one-side-open-3-in-a-row for me]
– 40*[number of one-side-open-3-in-a-row for opponent]
+ 20*[number of two-side-open-2-in-a-row for me]
– 15*[number of two-side-open-2-in-a-row for opponent]
+ 5*[number of one-side-open-2-in-a-row for me]
– 2*[number of one-side-open-2-in-a-row for opponent]

Example Game(Player: Position - # of nodes generated - CPU time(sec)):

X: [3,5] - 34 nodes - 1 sec
O: [4,5] - 84 nodes - 3 sec
…
