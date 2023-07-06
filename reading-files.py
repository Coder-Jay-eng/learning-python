# python read command("r")
employee_file = open("employees.txt", "r")

print(employee_file.readable())  # Returns True if file is readable

# print(employee_file.read())
#  # Returns all contents of the file

# print(employee_file.readline())
# # Returns first line of file.

# print(employee_file.readlines())
# # Returns all lines of file as an array.

# print(employee_file.readlines()[3])
# # Returns specified line in the index of array.


for employee in employee_file.readlines():
    print(employee)
# prints each individual line in the file

employee_file.close()  # closes file
