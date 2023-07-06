# # python write command("w")
employee_file = open("employee1.txt", "w")
print(
    employee_file.write("\nGeorge - Security Guard")
)  # Creates new file and updates / overwrites everything in the file

employee_file.close()
