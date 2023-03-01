"""
https://train.nzoi.org.nz/problems/872

There are up to 6 kinds of tea in Edward’s pantry, but partially filled boxes and loose bags are all over the shelves. The types he could have are Ginger (G), Chamomile (C), Earl Grey (E), Peppermint (P), Lemon (L) and Strawberry (S).

He needs to know how many of each type he has, so as he finds a type and a number of them, he calls them out to be input into your program.

After he has cleaned out all his pantry, you enter a D for “Done”. The program will then tell you how many of each type he has. The numbers should be listed for the teas in the same order as above ie: Ginger count first.
Input

The lines will consist of a letter indicating the tea type, followed by a space, followed by an integer Ni to indicate how many of that type have been discovered in the pantry (1≤Ni≤100).

Lines will terminate with the letter D.
Output

You should output a single line with 6 space-separated integers, indicating the number of Ginger, Chamomile, Earl Grey, Peppermint, Lemon and Strawberry teas Edward has.

    Sample Input 1

    C 3
    E 4
    P 9
    L 21
    C 5
    S 4
    E 19
    G 5
    C 7
    P 1
    D

    Sample Output 1

    5 15 23 10 21 4
"""

