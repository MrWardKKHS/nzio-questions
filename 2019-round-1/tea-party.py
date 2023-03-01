"""
https://train.nzoi.org.nz/problems/870

A number of old school friends meet regularly for afternoon tea parties at each other's house. They all stock a variety of teas although sometimes they are in low supply of some types. The teas stocked are Ginger (G), Chamomile (C), Earl Grey (E), Peppermint (P), Lemon (L) and Strawberry (S).

Each person has a favourite type of tea. Sometimes a person can't have their favourite because the host hasn't enough in their pantry.

A party is considered a success if nobody misses out on their favourite tea; it is mildly successful if at most 2 miss out, and it is a disaster if more than 2 miss out.

A number of these friends are interested in hosting the next tea party, but as they are old, they won't be replenishing their stocks before then. Your job is to determine how successful the next tea party would be, for each potential host.
Input

The first line will contain two space separated integers, N, the number of people who meet regularly (2≤N≤20,000), and K, the number of potential hosts (1≤K≤N).

Then follows N lines, each containing the first name of a party goer, followed by a space, then a letter indicating their favourite tea, as given above.

Then follows N more lines, each containing the first name of a party goer, followed by six space-separated integers, Gi,Ci,Ei,Pi,Li, and Si in order, representing the stock on hand in their pantry of each tea (0≤Gi,Ci,Ei,Pi,Li,Si≤20,000). The names are not necessarily in the same order as in the preceding N lines.

The last K lines each contain the name of a potential host.
Output

Output K lines, each containing the name of a potential host (in the same order as the last K lines of input), and the word(s) Successful or Mildly Successful or Disaster based on how many preferences for favourite teas would be met. This should be followed by a count of how many disgruntled party goers there would be if the outcome is other than fully successful. (i.e. don't output a 0 count)
Subtasks

    Subtask 1 (40%): 2≤N≤100
    Subtask 2 (60%): 2≤N≤20,000

    Sample Input 1

    5 3
    Mary S
    Robert S
    Ella G
    Cynthia E
    Desmond G
    Cynthia 1 0 1 1 2 0
    Mary 0 2 5 1 3 7
    Robert 1 2 8 0 3 1
    Desmond 15 13 16 17 0 1
    Ella 5 10 8 9 13 6
    Cynthia
    Robert
    Ella

    Sample Output 1

    Cynthia Disaster (3)
    Robert Mildly Successful (2)
    Ella Successful
"""
