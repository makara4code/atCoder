def numba_compile(numba_config):
    import os, sys
    if sys.argv[-1] == "ONLINE_JUDGE":
        from numba import njit
        from numba.pycc import CC
        cc = CC("my_module")
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature)(func)
            cc.export(func.__name__, signature)(func)
        cc.compile()
        exit()
    elif os.name == "posix":
        exec(f"from my_module import {','.join(func.__name__ for func, _ in numba_config)}")
        for func, _ in numba_config:
            globals()[func.__name__] = vars()[func.__name__]
    else:
        from numba import njit
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature, cache=True)(func)
        print("compiled!", file=sys.stderr)
 
import sys
import numpy as np
 
def solve(H, W, AB):
    A = W+1
    identity = -(1<<62)
    sqrtA = 500
    n_buckets = A // sqrtA + 1
    Data = np.zeros(n_buckets * sqrtA, dtype=np.int64)
    Data[0] = 1<<30
    Bucket_min = np.zeros(n_buckets, dtype=np.int64)
    Lazy = np.full(n_buckets, identity, dtype=np.int64)
 
    def eval_data(k):
        if Lazy[k] != identity:
            l, r = k*sqrtA, (k+1) * sqrtA
            for i in range(l, r):
                Data[i] = i-Lazy[k]
            Lazy[k] = identity
 
    def update(s, t, x):
        for k in range(s//sqrtA, (t-1)//sqrtA+1):
            l, r = k*sqrtA, (k+1)*sqrtA
            if s <= l and r <= t:
                Bucket_min[k] = l-x
                Lazy[k] = x
            else:
                eval_data(k)
                for i in range(max(l,s), min(r,t)):
                    Data[i] = i-x
                Bucket_min[k] = Data[l:r].min()
 
    def get_min(s, t):
        res = 1 << 62
        bl, br = s//sqrtA+1, t//sqrtA
        if bl > br:
            eval_data(br)
            return Data[s:t].min()
        if bl < br:
            res = Bucket_min[bl:br].min()
        ll, rr = bl*sqrtA, br*sqrtA
        if s < ll:
            eval_data(bl-1)
            mi = Data[s:ll].min()
            if res > mi:
                res = mi
        if rr < t:
            eval_data(br)
            mi = Data[rr:t].min()
            if res > mi:
                res = mi
        return res
 
    Ans = np.zeros(H, dtype=np.int64)
    for i in range(H):
        a, b = AB[i]
        update(a, b+1, a-1-get_min(a-1, a))
        ans = get_min(1, W+1)
        Ans[i] = ans+i+1 if ans < 1<<25 else -1
 
    return Ans
 
numba_compile([
    [solve, "i8[:](i8,i8,i8[:,:])"]
])
 
def main():
    H, W = map(int, sys.stdin.buffer.readline().split())
    AB = np.array(sys.stdin.buffer.read().split(), dtype=np.int64).reshape(H, 2)
    Ans = solve(H, W, AB)
    print("\n".join(map(str, Ans.tolist())))
 
main()