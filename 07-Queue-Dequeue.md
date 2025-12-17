# 07 — Rinda / Deque (Queue)

## Ideja
FIFO: pirmais iekšā → pirmais ārā. BFS parasti izmanto rindu.

## Šablons (deque)
```py
from collections import deque

q = deque()
q.append(x)      # push back
x = q.popleft()  # pop front
```

## Uzdevumi
1. Simulē klientu rindu: komandas `push x`, `pop`, `front`.
2. BFS pa matricu: no starta šūnas atrod īsāko ceļu līdz mērķim (ar sienām).
3. “Rotting Oranges” tipa uzdevums (viļņi pa līmeņiem).

## NeetCode piemēri
- Binary Tree Level Order Traversal
- Rotting Oranges
