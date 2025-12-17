# 01 — Saraksti (List) kā “masīvs”

## Ko jāzina
- Indeksēšana: `a[0]`, `a[-1]`
- Garums: `len(a)`
- Pievienošana: `append`, `extend`
- Dzēšana: `pop`, `remove`
- Iterēšana:
  - `for x in a:`
  - `for i, x in enumerate(a):`

## Mini-šabloni
```py
a = [3, 1, 4]
a.append(10)          # [3,1,4,10]
last = a.pop()        # last=10, a=[3,1,4]

for i, x in enumerate(a):
    print(i, x)

# Slicing (griezumi)
b = a[1:3]            # no 1 līdz 2 (3 nav iekļauts)
```

## Tipiskas kļūdas
- Iziet ārpus robežām (`IndexError`)
- Sajaukt indeksu ar vērtību (īpaši `for x in a`)

## Uzdevumi
### A. Warm-up
1. Ievadi `n`, tad `n` skaitļus. Izdrukā minimumu, maksimumu, summu.
2. Apgriez sarakstu bez `reverse()` (izmanto ciklu).
3. Atrodi otro lielāko elementu (bez `sort()`).

### B. Praktiskā domāšana
4. Pārvieto visus `0` uz beigām, saglabājot citu secību.
5. Atrodi, cik pāru `(i<j)` ir tādi, ka `a[i] > a[j]` (sākumā ar O(n²)).

## NeetCode piemēri
- Two Sum
- Contains Duplicate
