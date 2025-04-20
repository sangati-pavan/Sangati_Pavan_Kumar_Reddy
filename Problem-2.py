def generate_odd_series(n) :
    return [2*i + 1 for i in range(n)]

n = int(input()) # Input: 4
print(generate_odd_series(n))  # Output: [1, 3, 5, 7]
