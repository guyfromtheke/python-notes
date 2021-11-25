my_file = open('xmen.txt', 'w+') #opens the file for writing. 
my_file.write('Beast\n')
my_file.write('phoenix\n')

#writing multiple lines, use writelines.


my_file.writelines([ 
    'cyclops\n'
    'Bishop\n'
    'Nightcrawler\n'
])

my_file.close() # all the content gets written to the file and closes the file handle. 


# to read from the file. 


my_file = open('xmen.txt' , 'r')
print(my_file.read())

my_file.close()






