The program use `Complete Search` method through 2 function
1. `best_move(board)`:
       - This function is responsible for determining the best move for the computer player ('O').
       - It evaluates all available spaces on the board and calculates the maximum score for each possible move.
       - The optimal point represents the computer's desire to make a move. It is calculated by recursively simulating all possible future states (moves) in the game and assigning a score to each state.
       - The computer player ('O') aims to maximize his score and should choose the move with the best score.
       - The function returns the row and column index of the best move.

2. `optimal (table, depth, is_maximizing)`:
       - `board` represents the current state of the game.
       - `depth` tracks the depth of the recursion, indicating how many steps forward the algorithm is evaluating.
       - `is_maximizing` is a Boolean value indicating whether the player's (computer) move is maximizing or not. If `True`, the function maximizes the score; if `False`, it minimizes the score (for the opponent, 'X').
       - The function evaluates the current state of the game and returns a score based on the following conditions:
         + If the computer ('O') wins, the score is 1.
         + If player ('X') wins, it returns score -1.
         + If the match is a draw, the result is 0.
       - If the game is not over (no winner and no tie), the function will call itself recursively to evaluate all possible moves by creating a new game state. It alternates between maximizing and minimizing the score at each level of recursion.
       - The algorithm explores the entire game tree (all possible sequences of moves) until the final state (win, lose or draw) is reached or the specified depth limit is reached.
       - The `depth` parameter is important to control the depth of the search and avoid excessive computation in deep game trees.
