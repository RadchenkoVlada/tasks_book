def fib(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    else:
        fib_sequence = [1, 1]
        for _ in range(n - 2):
            fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])
        return fib_sequence


list_fib = [1, 1]

def fibo_recursive(n):
    if n<=0:
        print("Incorrect input")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)



def factorial(n):
    return factorial(n-1) * n

if __name__ == '__main__':
    # n = input("Please input a number:")
    print(fib(50))
    # print(fibo_recursive(50))
    print(factorial(10))

#

