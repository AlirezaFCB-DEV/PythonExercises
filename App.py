# for n in range(2, 10):
#     for x in range(2, n):
#         # print(f"line 4 {x} {n}")
#         if n % x == 0:
#             print(f"line 6 {n} equals {x} * {n // x}")
#             break

for number in range(2, 20):
    if number % 2 == 0 :
        print(f"Found An Even Number : {number}")
        continue
    print(f"Found An Odd Number : {number}")