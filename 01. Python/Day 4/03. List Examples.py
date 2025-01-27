L1 = []
print("1. An Empty List : ", L1)

L2 = [0, 1, 2, 3]
print("2. List With Four Items : ", L2)

L3 = ["abc", ["def", "ghi"]]
print("3. A Nested List : ", L3)

L4 = list("spam")
print("4. List Created From String : ", L4)

L5 = list(range(-4, 4))
print("5. List Created From Range : ", L5)

L6 = [10, 20, 30, 40]
print("6. Element At Index 2 : ", L6[2])

L7 = ['x', [10, 20, 30], 'y']
print("7. Accessing Element of Nested List : ", L7[1][2])

L8 = [0, 1, 2, 3, 4, 5]
print("8. Slicing List from 2 to 4 : ", L8[2:5])

L9 = [0, 1, 2, 3, 4]
print("9. Length of List : ", len(L9))

L10 = [10, [100, 200, 300, 400], 50]
print("10A. Accessing Sub-List : ", L10[1])
print("10B. Accessing Element From Sub-List : ", L10[1][3])
print("10C. Slciing Sub-List : ", L10[1][1:3])