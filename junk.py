

def heap_perm(A):
    n = len(A)
    Alist = [el for el in A]
    for hp in _heap_perm_(n, Alist):
        yield hp


def _heap_perm_(n, A):
    if n == 1: yield A
    else:
        for i in range(n-1):
            for hp in _heap_perm_(n-1, A): yield hp
            j = 0 if (n % 2) == 1 else i
            A[j],A[n-1] = A[n-1],A[j]
        for hp in _heap_perm_(n-1, A): yield hp


N = [0, 1, 2]
X = heap_perm(N)
while True:
    try:
        print(X.next())
    except:
        break
