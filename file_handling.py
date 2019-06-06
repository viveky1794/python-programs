import os
print("This the program of file handling here we are considering a file name test.txt\n ")

fd = open("test.txt",'r+')

print('file has open now.below wee are going to print the data\n')

print('..........................................')
print('1->',fd.read())
print('..........................................')
print('\n\n\nnow  we are going to read a singel line at a time by readline method')

fd.seek(0,0)

print('..........................................')
print('readline\n->',fd.readline())
print('..........................................')

print('\n\n\n now i will write some thing into file \n')


print('..........................................')
fd.write("it is some extera content into file. ")
print('..........................................')
