# opening file output.txt in append mode even if file does not exist it will create a new file.

fh = open('output.txt', 'at')

# updating data in line1

input1 = input("Enter text to write to the file : ")
line1 = fh.write(input1)
print(f"Data successfully written to {fh.name}.")

# appending data in line 2 
line2 = input("Enter additional text to append : ")
fh.write(f"\n{line2}")

print("Data successfully appended.")
fh.close()

# to print both the lines now again open the file in rt mode

fh1 = open('output.txt', 'rt')
print(f"Final content of {fh.name} : ")
for line in fh1:
    print(line, end='')
fh1.close()
    