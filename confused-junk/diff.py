for i in range(100):
    n,k = raw_input().split();
    n,k = int(n),int(k)
    z = (k-n)>>12
    print z
