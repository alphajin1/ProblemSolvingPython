from collections import Counter

if __name__ == '__main__':
    result = Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
    print(result, type(result))
    print(result["hi"]) # 3