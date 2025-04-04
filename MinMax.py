arr=[
    [5,6,7],
    [8,9,0],
    [4,5,6]
]

min=arr[0][0]
max=arr[0][0]

for row in arr:
    for num in row:
        if num < min:
            min=num

        if num > max :
            max=num
print(max) 
print(min)
