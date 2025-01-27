D1= {}
print("1. Empty Dictionary : ", D1)

D2 = {'spam' : 2, 'eggs' : 3}
print("2. Two Item Dictionary : ", D2)

D3 = {'food' : {'ham' : 1, 'egg' : 2}}
print("3. Nested Dictionary : ", D3)

D4 = dict(name = 'Bob', age = 40)
print("4. Alternative Construction : ", D4)

keylist = ['a', 'b', 'c']
valslist = [1, 2, 3]
D5 = dict(zip(keylist, valslist))
print("5. Zip 2 Lists as Dictionary : ", D5)

print(D2.keys())
print(D2.values())
print(D2.items())

#D2.get(key, default)     # Does not throw error if Key not Found
D2.get('spam', 10)         # Assigns default value to Key
print(D2)

D2.pop('eggs')
print(len(D2))
D2['spam'] = 10

D1.update(D2)            # Merges D1 and D2 into D1
print(D1)