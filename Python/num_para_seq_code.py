def foo(v,n):
    if n > 0 :
        return v + foo(v,n-1)
    else:
        return 0