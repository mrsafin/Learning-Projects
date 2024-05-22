# Cash

## Description

The "Cash" challenge is a program that simulates giving change in the most efficient way possible. Suppose you work at a store, and a customer gives you $1.00 (100 cents) for candy that costs $0.50 (50 cents). You need to pay them their change, which is the amount leftover after paying for the candy. To minimize the number of coins dispensed, the program uses a greedy algorithm to calculate the minimum number of coins needed for any given amount of change in cents.

## How It Works

When making change, the goal is to minimize the number of coins given to the customer. The program prompts the user for an amount of change owed (an integer greater than or equal to 0). It then calculates the minimum number of coins required to make that amount of change using quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢).

### Example

Change owed: 70

4

In this example, the user inputs 70, and the program outputs 4, indicating that 2 quarters, 2 dimes are needed.

## Greedy Algorithm

A greedy algorithm always takes the best immediate, or local, solution to find an answer. This approach is used here to minimize the number of coins:

1. Start with the largest coin denomination (quarters).
2. Use as many of those coins as possible without exceeding the amount owed.
3. Move to the next largest denomination (dimes) and repeat.
4. Continue until the smallest denomination (pennies) is used.

This method ensures the fewest coins are given as change.

## Implementation

The program is implemented in a file called `cash.c` and follows these steps:

1. Prompt the user for an integer amount of change owed.
2. Validate that the input is an integer greater than or equal to 0. Re-prompt if necessary.
3. Calculate the number of quarters, dimes, nickels, and pennies needed.
4. Print the total number of coins.

## Files

- `cash.c`: The main program file containing the implementation.

## How to Compile and Run

1. Open a terminal and navigate to the `cash` folder.
2. Compile the program using `gcc`:
   gcc -o cash cash.c
3. Run the program:
   ./cash
