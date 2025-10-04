print("=== Challenge 1: Collatz Conjecture ===\n")

# Get starting number from user
current_number = int(input("Enter starting number: "))

# Initialize step counter
step_count = 0

# Print initial number
print("\nSequence:", current_number, end=" ")

# Generate Collatz sequence
while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = 3 * current_number + 1
    print(current_number, end=" ")
    step_count += 1

# Output number of steps
print(f"\n\nSteps: {step_count}")

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
        print(f"{num} is prime")

print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

# Print header row
print("    ", end="")  # Top-left corner padding
for i in range(1, 11):
    print(f"{i:4}", end="")
print()  # New line

# Print separator
print("    " + "----" * 10)

# Print table rows
for row in range(1, 11):
    print(f"{row:2} |", end="")  # Row label
    for col in range(1, 11):
        print(f"{row * col:4}", end="")
    print()  # New line after each row





