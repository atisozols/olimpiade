# 99 — Špikerlapa (must-know šabloni)

## Saraksti
- `for i, x in enumerate(a):`
- divi rādītāji: `l=0, r=n-1` vai “slow/fast”

## Sliding window (mainīgs logs)
- paplašini ar `r`
- kamēr nederīgs → bīdi `l`
- `freq` (dict) uztur loga saturu

## Stack
- `append/pop`, `stack[-1]`
- monotonic stack: glabā indeksi/vērtības “augoši” vai “dilstoši”

## Queue (BFS)
- `deque`, `append/popleft`
- `seen` pievieno **uzreiz**, kad ieliec rindā

## Grafi
- adjacency list: `defaultdict(list)`
- DFS/BFS ar `seen`
- komponentes: palaid DFS/BFS no katra neredzētā mezgla

## DP
- definē `dp(i)` vai `dp[r][c]`: **ko tieši tas nozīmē?**
- bāzes gadījumi
- pāreja (no kā veidojas)
- memoizācija ar `lru_cache`
