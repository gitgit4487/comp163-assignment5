print("=== Challenge 2: Prime Number Checker ===")
num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not prime (must be greater than 1)")
else:
    print(f"Testing divisors from 2 to {num - 1}...")
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not prime (divisible by {i})")
            break
    else:
        print(f"{num} is prime!")
