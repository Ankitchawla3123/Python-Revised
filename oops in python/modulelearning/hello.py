import new
new.newatt=3

print(new.newatt)
new.__dict__["hey"]=213
print(new.hey)