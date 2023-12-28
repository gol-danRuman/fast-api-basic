from nepse import NEPSE
init = NEPSE()

#GET ALL REGISTERED BROKERS
# brokers = init.brokers()
# print(brokers)

# isOpen = init.isOpen()
# print(isOpen)

floorsheets = init.floorsheets()

# https://github.com/pyFrappe/nepse