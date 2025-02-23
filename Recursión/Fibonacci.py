def fibonacci(n, a=0, b=1):
    if n <= 0:
        return []
    elif n == 1:
        return [a]
    else:
        return [a] + fibonacci(n - 1, b, a + b)

if __name__ == "__main__":
    n = 15
    print(fibonacci(n))
