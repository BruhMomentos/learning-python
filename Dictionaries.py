
month_conversions = {
     "Jan": "January",
     "Feb": "Febuary",
     "Mar": "March",
     "Apr": "April",
     "May": "May",
     "Jun": "June",
     "Aug": "Aug",
     "Sept": "September",
     "Oct": "Ocotober",
     "Nov": "Novemeber",
     "Dec": "December",

}

input = input("Enter a word")


print(month_conversions["Jan"])
print(month_conversions["Feb"])
print(month_conversions.get('Mar', "Not a Valid Key"))
