N = int(input())
for i in range(N):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except(ZeroDivisionError, ValueError) as e:
        print('Error Code:', e)
    