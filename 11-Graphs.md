# 11 — Grafi (Graphs): reprezentācija, DFS/BFS

## Reprezentācija (adjacency list)
```py
from collections import defaultdict, deque

g = defaultdict(list)

# mala u -> v
g[u].append(v)

# ja nedirekcionēts:
# g[v].append(u)
```

## DFS/BFS pamata šabloni
```py
# DFS
seen = set()
def dfs(u):
    seen.add(u)
    for v in g[u]:
        if v not in seen:
            dfs(v)

# BFS
q = deque([start])
seen = {start}
while q:
    u = q.popleft()
    for v in g[u]:
        if v not in seen:
            seen.add(v)
            q.append(v)
```

## Uzdevumi
1. Pārbaudi, vai ir ceļš starp A un B.
2. Saskaiti savienotās komponentes.
3. Pārbaudi, vai grafiks ir bipartīts (2 krāsas).

## NeetCode piemēri
- Clone Graph
- Course Schedule
