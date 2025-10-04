print("=== Challenge 1: Collatz Conjecture ===\n")


current_number = int(input("Enter starting number: "))


step_count = 0


print("\nSequence:", current_number, end=" ")


while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = 3 * current_number + 1
    print(current_number, end=" ")
    step_count += 1


print(f"\n\nSteps: {step_count}")
