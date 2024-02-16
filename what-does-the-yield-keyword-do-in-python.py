def squares (n):
  for i in range (n):
    yield i * i

gen = squares (5) # create a generator object
print (next (gen)) # print the first value
print (next (gen)) # print the second value
for x in gen: # loop over the remaining values
  print (x)

