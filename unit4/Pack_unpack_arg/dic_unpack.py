def unpack_kwargs(a, b, c):

    print("a=",a,"b=", b,"c=", c)

kwargs = {'a': 1, 'b': 2, 'c': 3}
unpack_kwargs(**kwargs)
