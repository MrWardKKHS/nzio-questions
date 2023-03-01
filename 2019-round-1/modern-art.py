"""
https://train.nzoi.org.nz/problems/891

You are a famous abstract artist. Your latest work involves throwing paint at a range of canvases. Given the dimensions of your canvas and position and spread of each paint throw, you would like to know how many square centimetres of the final work are of a particular colour.
Input

Read the first line to obtain 3 space separated integers: the height H of the canvas in cm, the width W of the canvas in cm, and the number of paint throws N.

What follows are N lines (N≤50), representing the paint throws in the order they were thrown in. Each line contains 3 integers and a single character, separated by spaces. The first two integers are the x and y coordinates (in cm) for the paint throw (0≤xi<W, 0≤yi<H). The third integer is the spread in cm (explained below). The final character indicates the colour of the paint being thrown.

The last line contains a single character, indicating a colour C.
Output

Print a single integer, the number of square centimetres painted with the colour C in the final artwork. Note that more recently thrown colours might cover previous colours.
Subtasks

    Subtask 1 (75%): Small canvases where 1≤H,W≤100
    Subtask 2 (25%): Large canvases where 1≤H,W≤1,000,000



Spread

Paint always covers the square at the coordinates given. The spread indicates how many squares from the centre square the paint spreads. The overall coverage of a single throw is always a square shape. For example, a spread of 1 at coordinates (2, 1) would cover 9 square centimetres.

Sample Explained

In sample 1, you are given a canvas 5 cm high and 4 cm wide. A purple (p) colour is shown at coordinates (0, 0) with a spread of 0. A cyan (c) colour is also shown at coordinates (3, 2). The final square centimetre coverage of cyan (c) is therefore 6.

    Sample Input 1

    5 4 2
    0 0 0 p
    3 2 1 c
    c

    Sample Output 1

    6
"""
