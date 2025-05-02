def pbft_consensus(n, f):
    # Returns True if enough nodes agree (3f+1 out of n)
    return n >= (3*f + 1)
