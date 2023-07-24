import sys

input = sys.stdin.readline

n = int(input())

dist = list(map(int,input().split()))
fuel = list(map(int,input().split()))
fuel_cost = fuel[0]
cost = 0


for i in range(n-1):
    cost += fuel_cost * dist[i]
    if fuel_cost > fuel[i+1]:
        fuel_cost = fuel[i+1]
        
print(cost)