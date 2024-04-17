def fibonacci_series(n):
    fib_series = [0, 1]  # Initialize the series with first two Fibonacci numbers

    # Generate Fibonacci series up to the nth term
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series


# Input from the user
try:
    num_terms = int(input("Enter the number of terms you want in the Fibonacci series: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        series = fibonacci_series(num_terms)
        print("Fibonacci series up to the", num_terms, "term(s) is:", series)
except ValueError:
    print("Please enter a valid integer.")
