n = int(input("Enter the number:"))
sum = 0
series = 2

for i in range(1, n + 1):
    sum += series
    series = series * 10 + 2
    
print("The sum of the series is:", sum)
