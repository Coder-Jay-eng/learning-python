# # python write command("w")
employee_file = open("employees.txt", "w")
print(employee_file.readable())  # Returns False since only writing is allowed
employee_file.close()
