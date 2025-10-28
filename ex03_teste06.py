N, M, f = map(int, input().split())

A = []

for _ in range(N):
    linha = list(map(int, input().split()))
    A.append(linha)

B = [[0 for _ in range(M // f)] for _ in range(N // f)]

for i in range(0, N, f):
    for j in range(0, M, f):
        max_valor = 0
        for x in range(i, i + f):
            for y in range(j, j + f):
                if A[x][y] > max_valor:
                    max_valor = A[x][y]
        B[i // f][j // f] = max_valor

for linha in B:
    print(*linha)
