def main(A,B):
    interest_counter = 0
    for n in range(A,B + 1):
        n = list(str(n))
        
        n = [int(num) for num in n]
        
        products = 1
        sum = 0
        for num in n:
            products *= num
            sum += num
        if products % sum == 0:
            interest_counter += 1
    return interest_counter


test_case = input()

res = []
for case in range(int(test_case)):
    AandB = input()
    A,B = AandB.split()
    print(f"Case #{case + 1}: {main(int(A),int(B))}" )


