# 05 — Sliding Window (bīdāmais logs)

## Ideja
Uzturi “logu” `[l..r]` un pārbīdi `l`/`r`, lai izpildītu nosacījumu. Parasti ar `dict` vai skaitītājiem.

## 2 galvenie veidi
1) **Fiksēts logs** (garums K)  
2) **Mainīgs logs** (paplašini ar `r`, sašaurini ar `l`)

## Šablons (mainīgs logs)
```py
l = 0
freq = {}
for r in range(len(s)):
    freq[s[r]] = freq.get(s[r], 0) + 1

    while logs_ir_nederīgs(freq):
        freq[s[l]] -= 1
        if freq[s[l]] == 0:
            del freq[s[l]]
        l += 1

    # šeit logs [l..r] ir derīgs, vari atjaunot atbildi
```

## Uzdevumi
### A. Fiksēts logs
1. Dots saraksts un K. Atrodi maksimuma summu jebkurā garuma K apakšsarakstā.
2. Dota virkne. Atrodi, cik apakšvirkņu garuma K ir ar unikāliem simboliem.

### B. Mainīgs logs
3. Garākā apakšvirkne bez atkārtotiem simboliem.
4. Minimālais logs, kas satur visus nepieciešamos simbolus (grūtāks).

## NeetCode piemēri
- Longest Substring Without Repeating Characters
- Minimum Window Substring
