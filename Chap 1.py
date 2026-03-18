minutes = 42
seconds = minutes * 60 + 42 
print (seconds, "seconds")
km = 10
miles = km / 1.61
print (round(miles,2), "miles")
averagepace = seconds / miles
print (round (averagepace,2), "miles per seconds")
print (round (averagepace/60, 2), "miles per minutes")
averagespeed = miles / (seconds /3600)
print (round (averagespeed,2), "miles per hour")
