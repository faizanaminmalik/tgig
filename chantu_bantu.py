import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here
T = int(input())
for i in range(0, T):
    N = int(input())
    G = int(input())
    P = input().split()
    Prices = [int(i) for i in P]
    Prices.sort()
    money = 0
    for x in range(0, N):
        money += Prices[x]
    print(money)
