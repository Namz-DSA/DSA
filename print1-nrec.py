def intnumbers(N):
    if N == 0:
        return 
    intnumbers(N-1)
    print(N)


intnumbers(5)