"""Generate sales report showing total melons each salesperson sold."""

# creates empty dict and sets it to variable salespeople
salespeople = {}

# opens the txt file
f = open('sales-report.txt')
# loops through each line of the file
for line in f:
    # strips the line of trailing characters
    line = line.rstrip()
    # stores salesperson's name, total amount of order, and total melons sold as items in a list
    entries = line.split('|')
    # retrieves first item of list (salesperson's name) and stores it in variable 'salesperson'
    salesperson = entries[0]
    # retrieves third item of list (total melons sold), converts it to an int object and stores it in variable 'melons'
    melons = int(entries[2])
    # stores salesperson name as dict key and melons sold as dict value
    salespeople[salesperson] = salespeople.get(salesperson, 0) + melons
    
# loop over each item in the dict 'salespeople'
for salesperson in salespeople:
    # print how many melons each salesperson sold
    print(f'{salesperson} sold {salespeople[salesperson]} melons')

