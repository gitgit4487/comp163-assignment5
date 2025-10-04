I chose the loop types that I did in order to pass the test cases, using for and while loops in the correct situatuions also helped me succeed in this trivial assignment.

My solutions worked as follows:
Challenge 1: I was able to complete the collatz conjecture (first time hearing of it)
Challenge 2: The prime numbers were tricky but when I figured it out eventually
Challenge 3: I used the code from word and added to it

Shoutout to ChatGPT, couldn't have done this wihout that clanker.


Challenge 1: Collatz Conjecture - The user inputs starts of by inputting a number. While the number is not 1: If it's even, divide it by 2. If it's odd, multiply by 3 and add 1. Each step is counted and printed as part of the sequence. I used a while loop because the number of iterations isn't known ahead of time — it depends on how the sequence progresses. This was the first time I've ever heard of this.

Challenge 2: Prime Number Checker - The program checks if a given number is prime. If the number is greater than or equal to 1, it's not prime. Otherwise, a for loop tests divisibility from 2 up to (but not including) the number itself. If the number is divisible by any of those values, it's not prime. If no divisors are found, the number is prime. The for loop made it easy to go through a known range of numbers.

Challenge 3: Multiplication Table - This prints a clean, formatted multiplication table from 1 to 10: The outer for loop handles the rows. The inner for loop handles the columns. I used f-strings to keep the output aligned and readable. I had some starter code for this from Word, which I adapted and improved with nested loops.

AI Assistance - HUGE shoutout to my cligga ChatGPT, this cligga helped me understand these challenges, I'm just glad it's over
