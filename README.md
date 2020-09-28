# Sudoku-Solver
 
## Purpose 
To solve a Sudoku, a logic-based puzzle, a constraint satisfaction problem. The objective of the puzzle is to place digits within the board so that each row, column, or sub-grid (3x3) contains all the digits from 1-9.

## Algorithm(s) Used
Backtracking algorithm was used in this program to solve a given sudoku board. 

### Background Information
Backtracking is an algorithm that goes through all, or some, of the solutions to a problem and builds candidates to the solution(s) incrementally. When a candidate is determined not to lead to a valid solution, it is abandoned. When a candidate it abandoned, it results in visiting a previous stage and exploring new possibilities from there. When a solution is found, searching terminates.

## Constraints 
Constraints for a candidate includes:
<ul>
 <li>Each row has unique numbers from 1-9 or it has 0 (indicating an empty cell) </li>
 <li>Each column has unique numbers from 1-9 or it has 0 (indicating an empty cell) </li>
 <li>Each sub-grid (3x3) has unique numbers from 1-9 or it has 0 (indicating an empty cell) </li>
</ul>

## Algorithm
<ol>
 <li>Find an empty cell</li>
 <li>Place a number in the cell and validate the candidate</li> 
 <li>If any of the constrains listed above failed, abandon the candidate and repeat step 2 with the next number. Otherwise, check if a solution is found</li>
 <li>If a solution is found, stop searching and print out the results. Otherwise, repeat steps 2-4.</li>
 <li>If all the numbers have been checked and there is no candidate, stop searching and terminate the program.</li>
</ol>

## How to Run the Program
To run the program, you would have to have the latest version of Python. Once the program is opened, fill in the array of arrays representing the sudoku board, sudoku_board located at the top of the program, to match the board you are given (0 means the cell is empty). Once filled, run the program. Your inputted sudoku board will be displayed. If there is a solution, the completed sudoku board will be displayed. Otherwise, a prompt, "No Solutions Exists," will be printed.

## Sample Results
### Sudoku Problem
<img src="/images/sudoku_problem.png"/>
Problem taken from https://www.websudoku.com/?level=3

### Inputting the Sudoku Problem in the Program
<img src="/images/sudoku_input.png"/>

### Output 
<img src="/images/sudoku_answers.png">
