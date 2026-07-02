# Open a file in python , read it and handle errors

# file_handler = open('C:\\ML\\Project\\sample.txt', 'rt')
# # read the content of the file and return it as a string
#  if file does not exist, it will raise an error but i want to print a message instead of error.
# So, I will use try and except block to handle the error.
# now code changed to try and error to handle the error if file does not exist.
try:
    file_handler = open('C:\\ML\\Project\\sample.txt', 'rt') # name of file changed to sample1.txt
    line_1 = file_handler.readline() # read first line of the file
    line_2 = file_handler.readline() # read second line of the file


    file_handler.close() 
# why do we close the file? Because it is a good practice to close the file after we are done with it. It frees up system resources and ensures that any changes made to the file are saved properly. 

    print(f"Line 1: {line_1}")
    print(f"Line 2: {line_2}")  

except FileNotFoundError:
    print("Error: the file sample1.txt was not found.")
    
