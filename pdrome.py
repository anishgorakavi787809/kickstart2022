import random
def main(quanti,binary):
    if len(binary) != quanti:
        print("Err")
    else:
        arr = []

        for i in binary:
            if i == "?":
                i.replace("?",str(random.randint(0,1)))
            arr.append(i)
        var = ''.join(arr)
        if var[::-1] == var:
            return "IMPOSSIBLE"
        return "POSSIBLE"

test_case = input()
for case in range(int(test_case)):
    quanti = int(input())
    binary = input()
    print(f"Case #{case + 1}: {main(quanti,binary)}" )
