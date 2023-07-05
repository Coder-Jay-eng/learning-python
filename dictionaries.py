# dictionaries are special structures that allow us to store data in key value pairs.

monthConversions = {
    # "Key": "Value"
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Dec"])

# OR

print(monthConversions.get("Luv", "Not a valid key"))
