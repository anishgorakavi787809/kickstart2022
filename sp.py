import time

start = time.time()

def main(I,P):

    for x in I:
        if P.find(x) == -1:
           return "IMPOSSIBLE" 
    if len(P) >= len(I):
        return len(P) - len(I)
    
    return "IMPOSSIBLE"

test_case = input()

res = []
for case in range(int(test_case)):
    I = input()
    P = input()
    print(f"Case #{case + 1}: {main(I,P)}" )

print(time.time() - start)

