# 04 — Two Pointers (divi rādītāji)

## Ideja
Divi indeksi (piem., `l`, `r`) kustas pa sarakstu/virkni, bieži lai iegūtu O(n).

## Tipiski pielietojumi
- sakārtotam masīvam
- pāru meklēšanai
- “saspiešanai” (remove duplicates)

## Šablons
```py
l, r = 0, len(a)-1
while l < r:
    if a[l] + a[r] < target:
        l += 1
    elif a[l] + a[r] > target:
        r -= 1
    else:
        break
```

## Uzdevumi
1. Dots sakārtots saraksts. Atrodi, vai eksistē pāris ar summu `X`.
2. Noņem dublikātus sakārtotā sarakstā “in-place” un atgriez jauno garumu.
3. Dota virkne. Pārbaudi, vai tā ir palindroms (ignorējot atstarpes/pieturzīmes).

## NeetCode piemēri
- Valid Palindrome
- Two Sum II (Input Array Is Sorted)
