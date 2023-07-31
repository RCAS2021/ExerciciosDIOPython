month = int(input())

months_dict = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]

if (month>0 and month<=12):
    print (months_dict[month-1])
else:
    print("ERRO")