
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
print("before.....")
print(list)
print(tuple)
print("After.....")
list[2] = 1000     # Valid syntax with list

print(list)
tuple[2] = 1000    # Invalid syntax with tuple
print(tuple)
