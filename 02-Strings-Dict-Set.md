# 02 — Virknes + skaitīšana ar vārdnīcu (dict) un set

> **dict/set** ir kritiski svarīgs gan sliding window, gan grafiem, gan DP.

## Ko jāzina
- `dict` kā “skaitītājs” (frekvences)
- `set` kā “ātra piederība” (O(1) vidēji)

## Šabloni
```py
from collections import Counter, defaultdict

s = "abca"
cnt = Counter(s)  # {'a':2,'b':1,'c':1}

freq = defaultdict(int)
for ch in s:
    freq[ch] += 1

seen = set()
for ch in s:
    if ch in seen:
        pass
    seen.add(ch)
```

## Uzdevumi
1. Dota virkne. Atrodi pirmo simbolu, kas neatkārtojas.
2. Pārbaudi, vai divas virknes ir anagrammas.
3. Dots saraksts ar skaitļiem. Atrodi elementu, kas parādās visbiežāk.

## NeetCode piemēri
- Valid Anagram
- Group Anagrams
