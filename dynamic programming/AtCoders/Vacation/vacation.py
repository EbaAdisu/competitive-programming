n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
for r in range(1, n):
    for c in range(3):
        mat[r][c] += max(mat[r-1][:c] + mat[r-1][c+1:])
print(max(mat[-1]))
