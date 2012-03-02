def mcpi(nsamples):
    from random import random
    s = 0
    for i in xrange(nsamples):
        x = random()
        y = random()
        if x*x + y*y <= 1:
            s+=1
    return 4.*s/nsamples
    
def multi_mcpi(view, nsamples):
    p = len(view.targets)
    if nsamples % p:
        # ensure even divisibility
        nsamples += p - (nsamples%p)
    
    subsamples = nsamples/p
    
    ar = view.apply_async(mcpi, subsamples)
    return sum(ar)/p