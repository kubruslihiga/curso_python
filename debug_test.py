import pdb


def soma(x, y):
    z = x + y
    pdb.set_trace()
    if x > 10:
        breakpoint()
    print("debugger")
    return z


soma(112, 4)
