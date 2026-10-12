def matrix_chain_order(p, n):
    m = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = (m[i][k] + m[k + 1][j]
                        + p[i - 1] * p[k] * p[j])

                if cost < m[i][j]:
                    m[i][j] = cost

    return m[1][n - 1]

p = list(map(int, input("Enter dimensions: ").split()))
n = len(p)

result = matrix_chain_order(p, n)

print("Minimum number of scalar multiplications:", result)
