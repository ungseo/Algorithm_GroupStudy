import sys

input = sys.stdin.readline

emoji = input().rstrip()

length = len(emoji)
colon = emoji.count(':')
underbar = emoji.count('_')

ans = length + colon + underbar * 5

print(ans)