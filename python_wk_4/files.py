filename= input("Enter the file name: ")
try:
  with open(filename,"r") as employeelist:
    employees=employeelist.read()
    # Modify content // convert to uppercase
    modified_content = employees.upper()
        
        # Define new filename
    new_filename = "modified_" + filename
        
        # Write to new file
    with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        
    print(f"Modified content saved to {new_filename}")
except FileNotFoundError:
  print("This file doesnt exist!!")