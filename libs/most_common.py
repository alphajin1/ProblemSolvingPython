import collections

if __name__ == '__main__':
    a = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5]

    print(collections.Counter(a).most_common(3))
    # [(5, 4), (4, 3), (3, 2)]