# 08 — Linked List (saistītais saraksts)

> Olimpiādēs retāk prasa implementēt no nulles, bet bieži parādās uzdevumos.

## Pamats
Mezgls: `value` + `next` (dažreiz `prev`).

## Šablons (iterācija)
```py
cur = head
while cur:
    cur = cur.next
```

## Top 3 prasmes
1) apgriezt sarakstu  
2) atrast ciklu (Floyd)  
3) atrast vidu (slow/fast)

## Uzdevumi
1. Apgriez linked list.
2. Atrodi, vai ir cikls.
3. Atrodi vidējo mezglu (slow/fast pointers).

## NeetCode piemēri
- Reverse Linked List
- Linked List Cycle
