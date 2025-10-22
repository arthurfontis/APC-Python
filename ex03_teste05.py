def decompressao():
    n = int(input())
    for _ in range(n):
        s = input().strip()
        result = ""
        i = 0
        while i < len(s):
            letter = s[i]
            i += 1
            num = ""
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            result += letter * int(num)
        print(result)

decompressao()