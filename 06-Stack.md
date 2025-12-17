# 06 — Steks (Stack)

## Ideja
LIFO: pēdējais iekšā → pirmais ārā. Python: parasti `list` ar `append/pop`.

## Šabloni
```py
stack = []
stack.append(x)
top = stack[-1]
stack.pop()
```

## Kur to lieto
- iekavas (valid parentheses)
- “monotonic stack” (nākamais lielākais/mazākais)
- DFS imitācija

## Uzdevumi
1. Pārbaudi, vai iekavu virkne ir korekta: `()[]{}`.
2. Aprēķini “Next Greater Element” katram masīva elementam.
3. Vienkāršs kalkulators ar `+` un `*` (parsera izaicinājums).

## NeetCode piemēri
- Valid Parentheses
- Daily Temperatures
