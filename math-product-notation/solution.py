def product(f, lo, hi):
    """
    f:  a function taking a single integer and returning a number
    lo: the starting index (inclusive)
    hi: the ending index (inclusive)

    Returns:
        Prod_{i=lo}^{hi} f(i), the product of f(i) for every integer i
        from lo to hi, both ends included. If hi < lo, the product is
        empty (1).
    """
    ans = 1
    
    for i in range(lo,hi+1):
        ans *= f(i)

    return ans
