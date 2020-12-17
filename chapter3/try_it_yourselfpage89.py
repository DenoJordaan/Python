guestlist = ['dad','mom','Gran','joeps']
print(guestlist)
message1 = f'i would like to invite you to dinner {guestlist}.'
print(message1)
popped_guestlist1 = guestlist.pop(-1)
popped_guestlist2 = guestlist.pop(0)
print(popped_guestlist1)
print(popped_guestlist2)
message2 = f'i would like to invite you to dinnner {guestlist[1].title()}.'
print(message2)
message3 = f'i would like to invite you to dinnner {guestlist[0].title()}.'
print(message3)
guestlist.insert(0,'juan')
print(guestlist)
guestlist.insert(3,'Don')
print(guestlist)
guestlist.insert(2,'jimmy')
print(guestlist)
del guestlist[2]
print(guestlist)
del guestlist[0]
print(guestlist)
del guestlist[1]
print(guestlist)
del guestlist[1]
print(guestlist)
del guestlist[0]
print(guestlist)