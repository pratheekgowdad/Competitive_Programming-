"""
Problem
Alex, a sophomore got inspired to do mathematics after watching a movie "The Man who knew Infinity". One day, he was studying mathematics in the library and in one of the books he discovered a way to perform multiplication of numbers in a new fashion by using digits of a number. He found that method interesting and decided to formulate an algorithm for the same method. Alex finds it difficult to implement and he asks for your help.

Given a number N. Let the first digit of the number be X. P1 is the number formed using first X digits of the given number in the sequence. Let the digit after Xth digit is Y. P2 is another number formed using Y digits starting from (X + 1)th position in sequence and so on. If the number of digits to be used to form a number are more than the remaining digits, then simply form the number using digits till the last digit. Product of (P1 * P2 * P3 ... * Pi) is known as magic product. Help Alex to find the magic product.

Input Format:
The first line of the input contains an integer T denoting the number of test cases. Each test case contains a number N followed by values of A and B respectively.

Output Format:
For each test case, output the magic product modulo 10A + B.

Constraints:

T ∈ [1, 105]
N ∈ [1, 10100]
A ∈ [1, 9]
B ∈ [0, 100]
NOTE: Any digit in the given number N will not be equal to 0.

Sample Input:
3
46542368
1 5
35935
2 9
54321
1 3

Sample output:
1
30
7
"""




try:
    for _ in range(int(input().strip())):  # Read the number of test cases
        s = input().strip()               # Read the number as a string
        u = len(s)
        a, b = map(int, input().strip().split())  # Read A and B
        x = 0
        r = []

        while u > x:
            t = int(s[0])                 # Get the first digit
            k = s[:t]                     # Get the first t digits
            s = s[t:]                     # Remove these t digits from the string
            x += t                        # Update the position counter

            r.append(int(k))              # Append the number to the list

            if len(s) == 0:               # Break if the string is empty
                break

        v = 1
        for j in r:                       # Calculate the product
            v *= j

        print(v % (10**a + b))            # Print the result modulo (10^a + b)
except Exception as e:
    print(f"An error occurred: {e}")
