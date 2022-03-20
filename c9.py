def main(N:int):
    N = str(N)

    for num in range(0,10):
        add_digi = N + str(num)
        if int(add_digi) % 9 == 0:
            add_digi_rev = add_digi[::-1]
            if add_digi_rev < add_digi:
                return add_digi_rev
            return add_digi
        continue


test_case = input()
for case in range(int(test_case)):
    N = input()
    print(f"Case #{case + 1}: {main(int(N))}" )

