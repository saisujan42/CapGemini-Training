print(len([1, 2, 3]))

combinedList = [1, 2, 3] + [4, 5, 6]
print(combinedList)

sameValueList = ['abc'] * 4
print(sameValueList)

print(str([1, 2]) + "34")

print([1, 2] + list("34"))

print(3 in (1, 2, 3))

for x in [1, 2, 3]:
    print(x, end = ' ')
print()

res = [c * 4 for c in 'SPAM']
print(res)