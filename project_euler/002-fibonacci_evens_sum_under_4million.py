"""Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be 1, 2, 3, 5, 8,
13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

def fibonacci_to_four_million():
    sequency = [1, 1]         # it starts with two ones for the first sum
    while sum(fibonacci) <= 4000000:
        for number in fibonacci:
            n = sequency[number - 1] + sequency[number]
            n.append(sequency)
    return fibonacci

def sum_evens:
    sequency = fibonacci_to_four_million()
    for number in sequency:
        if number % 2 == 0:
            number.append()
    sum(evens)

# def fib_test():
#     fibonacci = [1, 2]
#     for n in range(40):
#         if n == sum(fibonacci[-1], fibonacci[-2]):
#             fibonacci.append(n)
#     return fibonacci
