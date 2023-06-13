import itertools

if __name__ == '__main__':
    arr = ['A', 'B', 'C']
    nPr = itertools.permutations(arr, 2)
    print(list(nPr))