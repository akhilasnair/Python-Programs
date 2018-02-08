#airport problem
#given departure and arrival times in seconds
arrivalarray = [900, 940, 950, 1100, 1500, 1800]
departurearray = [910, 1200, 1120, 1130, 1900, 2000]
totalarray = arrivalarray + departurearray
totalarray.sort()
count = 0
gatearray = []
#appending the count of gate opening and closing to gatearray based on arrivals and departures
for time in totalarray:
    if time in arrivalarray:
        count += 1
        gatearray.append(count)
    else:
        count -= 1
        gatearray.append(count)
#getiing only the distinct values from the gatearray
gatearray = set(gatearray)
print(" The Minimum number of gates to be opened is {}".format(max(gatearray)))
