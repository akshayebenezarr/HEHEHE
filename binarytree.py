class maram:
    def __init__(self, key, left, right):
        self.key = key
        self.left.key = left
        self.right.key = right


n1 = maram(2, 3, 5)
print(n1.key, n1.left, n1.right)


def parsetree(n1):
    tup = (n1.left, n1.key, n1.right)
    n1.left = parsetree(n1.left.key)
    n1.right = parsetree(n1.right.key)

    if n1.left is None:
        tup=(None, n1.key, n1.right)
        n1.right = parsetree(n1.right.key)
    elif n1.right is None:
        tup=(n1.left, n1.key, None)
        n1.left = parsetree(n1.left.key)
    else:
        tup=(None, n1.key, None)



parsetree(n1)
print(tuple)