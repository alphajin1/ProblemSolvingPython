import itertools

if __name__ == '__main__':
    arr = ["a", "b", "c"]
    nCr = itertools.combinations(arr, 2)
    print(list(nCr))