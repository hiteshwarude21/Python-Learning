s = {12,23,343,3553,23,4534,5,34,4,"hitesh"}

print(s,type(s))

s.add(566)
print(s,type(s))

s.remove(3553)
s.remove(4534)  # this remove only removes 1 element at time
print(s,type(s))

s.remove(343)
print(s,type(s))

s.remove("hitesh")
s.add("Raj")
print(s,type(s))

