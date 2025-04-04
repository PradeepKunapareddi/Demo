li=[2,3,5,5,2,6,7,6,5,4,8,9,5,6,4]
freq = {}

for item in set(li):
    freq[item]=li.count(item)
print(freq)