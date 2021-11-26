import sys
from typing import final   #for easier code handling. 


file_name = 'recipes.txt'

try: 
    my_file = open('recipes.txt' , 'x')
    my_file.write(b'Meatballs\n') #b is for bytes
    my_file.close()
except FileExistsError as err:
    print(f"the {file_name} file already exists")
    sys.exit(1)
except:
    print(f"unable to write to file")
    sys.exit()
else:
    print(f"wrote to {file_name}")
finally:
    print(f"execution completed")

    

