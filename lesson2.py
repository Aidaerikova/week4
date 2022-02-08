if gg == 6:
    from functools import reduse
    a = [i for i in range(1, 101)]
    def dom(x):
        dom = pow(x,2)
        return dom

    def filter1(v):
        if v % 3 == 0 and v % 5 == 0:
            return v

        def summa(m, n):
            return m + n

        b = list(map(dom, a))
        c = list(filter(filter1, b))
        d = reduce(summa, c)
        print(d)

