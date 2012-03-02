lis = range(5)

# you can create an iterator with `iter(iterable)`
it = iter(lis)

# it.next() returns the next value
# and raises StopIteration when you get to the end
while True:
    try:
        print it.next()
    except StopIteration:
        print "done"
        break
