#generate the first 50 fibonacci sequence 
fibonacci_seq = []
a, b = 0, 1
for _ in range(50):
    fibonacci_seq.append(a)
    a, b = b, a + b

print(fibonacci_seq)

#sum the first fibonacci sequence
sum_fibonacci = sum(fibonacci_seq)
print(f"The sum of the first fibonacci sequence is: {sum_fibonacci}")
