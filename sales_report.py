"""Generate sales report showing total melons each salesperson sold."""

# creates empty lists and sets them to variables salespeople and melons_sold
salespeople = []
melons_sold = []

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
    # checks to see if saleperson's name is in the list of salespeople.
    if salesperson in salespeople:
        # if name is in the list, find the index of salesperson in the list and store it in variable 'position'
        position = salespeople.index(salesperson)
        # add the number of melons the salesperson sold at the same index but for list 'melons_sold'.
        melons_sold[position] += melons
    else:
        # if name is not in the list, add their name to the list
        salespeople.append(salesperson)
        # add the number of melons the salesperson sold to the end of the list 'melons_sold'.
        melons_sold.append(melons)

# loop over each item in the list 'salespeople'
for i in range(len(salespeople)):
    # print how many melons each salesperson sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
