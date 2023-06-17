T = int(input())

f0 = [1, 0]
f1 = [0, 1]

for i in range(39):
    rst0 = f0[i] + f0[i+1]
    f0.append(rst0)
    rst1 = f1[i] + f1[i+1]
    f1.append(rst1)


for tc in range(T):
    n = int(input())

    print(f0[n], f1[n])
