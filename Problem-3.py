def generate_adjusted_odd_series(n) :
    count = n if n % 2 != 0 else n - 1
    return [2*i + 1 for i in range(count)]

n = int(input()) #Input: 6
print(generate_adjusted_odd_series(n))  # Output: [1, 3, 5, 7, 9]
