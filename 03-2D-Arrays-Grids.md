# 03 — Divdimensiju saraksti (matricas)

## Ko jāzina
- Pareiza izveide:
  - ✅ `grid = [[0]*m for _ in range(n)]`
  - ❌ `grid = [[0]*m]*n` (kopētas rindas)
- Piekļuve: `grid[r][c]`
- Kaimiņi (4 virzieni): augša/leja/pa kreisi/pa labi

## Šabloni
```py
n, m = 3, 4
grid = [[0]*m for _ in range(n)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
for r in range(n):
    for c in range(m):
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m:
                pass
```

## Uzdevumi
1. Ievadi matricu un aprēķini katras rindas summu.
2. Atrodi galvenās diagonāles summu.
3. Dota 0/1 matrica. Saskaiti “saliņas” (savienotas 1-šūnas).

## NeetCode piemēri
- Number of Islands
- Flood Fill
