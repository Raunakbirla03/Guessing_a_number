import random
N = random.randint(1,100)
print(N)
A = {}
i = 0
A[i] = int(input("Enter the Number: "))
if(A[i] >= N-10 and A[i] <= N+10):
    print("WARMI")
else:
    print("COLDI")
while(A[i] != N):
    if(A[i] < N):
        D = (N - A[i])
    else:
        D = (A[i] - N)
    A[i + 1] = int(input("Enter the Number: "))
    if((A[i] < A[i + 1] < (N+D) or (N-D) < A[i + 1] < A[i]) and A[i + 1] != N):
        print("WARMER")
    elif(A[i + 1] != N):
        print("COLDER")
    i += 1
print("You guessed correctly and it took {} guesses".format(len(A)))