"""
Task :
Raghu is a shoe shop owner. His shop has X number of shoes. He has a list containing the size of each shoe he has in his shop. There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size. Your task is to compute how much money Raghu earned.

Input Format :
The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.

Output Format :
Print the amount of money earned by Raghu.

Sample Input :
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output :
200
"""
from collections import Counter

num_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
num_customers = int(input())

cost = 0
for _ in range(num_customers):
    size, price = map(int, input().split())
    if shoe_sizes[size]:
        cost += price
        shoe_sizes[size] -= 1

print(cost)