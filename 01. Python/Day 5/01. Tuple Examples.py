T1 = ()
print("1. Empty Tuple : ", T1)

T2 = (0, )
print("2. Single Element Tuple : ", T2)

T3 = (0, 'Ni', 1.2, 3)
print("3. Four-Item Tuple : ", T3)

T4 = 0, 'Ni', 1.2, 3
print("4. Another Four-Item Tuple : ")

T5 = ('abc', ('def', 'ghi'))
print("5. Nested Tuple : ", T5)

T6 = tuple('spam')
print("6. Tuple of Items In An Iterable : ", T6)

print("7. Accessing Using Index of Tuple : ", T3[2])

print("8. Accessing Using Index of Nested Tuple : ", T5[1][1])

print("9. Tuple Slicing : ", T3[0:2])

print("10. Length of Tuple : ", len(T4))