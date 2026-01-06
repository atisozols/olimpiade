# Ideja: input() nolasa VIENU rindu. Ja uzdevumā dati ir vairākās rindās,
# tu vienkārši izsauc input() tik reižu, cik rindas/formāts prasa.
#
# Ja ievade ir liela -> lieto ātro variantu:
# import sys
# input = sys.stdin.readline
# ---------------------------------------------

# ============================================================
# 1) 1. rinda: divi skaitļi n, m
#    2..(m+1) rindas: pa diviem skaitļiem (malas, pāri, utt.)
# Piemērs:
# 5 3
# 1 2
# 2 4
# 4 5
# ============================================================
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

# ============================================================
# 2) 1. rinda: n
#    2. rinda: n skaitļi vienā rindā (masīvs)
# Piemērs:
# 4
# 10 20 30 40
# ============================================================
n = int(input())
arr = list(map(int, input().split()))

# ============================================================
# 3) 1. rinda: n
#    NĀKAMĀS n rindas: pa vienam skaitlim (vai tekstam)
# Piemērs:
# 3
# 7
# 2
# 9
# ============================================================
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# ============================================================
# 4) 1. rinda: n m
#    NĀKAMĀS n rindas: matrica ar m skaitļiem katrā rindā
# Piemērs:
# 2 3
# 1 2 3
# 4 5 6
# ============================================================
n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# ============================================================
# 5) 1. rinda: n
#    NĀKAMĀS n rindas: virknes (teksts)
# Piemērs:
# 3
# abc
# qwerty
# z
# ============================================================
n = int(input())
lines = []
for _ in range(n):
    s = input().strip()   # strip() noņem '\n' un liekās atstarpes
    lines.append(s)

# ============================================================
# 6) "Rindas + mainīgs elementu skaits":
#    1. rinda: q (vaicājumu skaits)
#    NĀKAMĀS q rindas: komanda + parametri (dažreiz 1, dažreiz 2+)
# Piemērs:
# 4
# ADD 5
# ADD 10
# SUM 1 2
# GET 2
# ============================================================
q = int(input())
for _ in range(q):
    parts = input().split()        # sadala pa vārdiem/skaitļiem
    cmd = parts[0]
    if cmd == "ADD":
        x = int(parts[1])
        # apstrādā ADD x
    elif cmd == "SUM":
        l = int(parts[1])
        r = int(parts[2])
        # apstrādā SUM l r
    elif cmd == "GET":
        i = int(parts[1])
        # apstrādā GET i

# ============================================================
# 7) 1. rinda: n
#    NĀKAMĀS n rindas: "a b c ..." bet katrā rindā var būt atšķirīgs garums
# (piem., katras rindas sākumā ir k, tad seko k skaitļi)
# Piemērs:
# 3
# 2 10 20
# 4 1 2 3 4
# 1 999
# ============================================================
n = int(input())
lists = []
for _ in range(n):
    parts = list(map(int, input().split()))
    k = parts[0]
    values = parts[1:]              # pārējie skaitļi
    # (drošības pārbaude, ja vajag) assert len(values) == k
    lists.append(values)

# ============================================================
# 8) "Lasi līdz EOF" (līdz faila beigām) — ja uzdevums nesaka, cik rindas
# Piemērs:
# (nezināms rindu skaits)
# 1 2
# 5 6
# 7 8
# ============================================================
import sys
pairs = []
for line in sys.stdin:              # katra nākamā rinda līdz EOF
    line = line.strip()
    if not line:
        continue
    a, b = map(int, line.split())
    pairs.append((a, b))

# ------------------------------------------------------------
# Piezīme:
# Vienmēr skaties uzdevuma ievades aprakstu:
# - "pirmajā rindā ..." -> viena input()
# - "nākamajās N rindās ..." -> cikls ar N input()
# - "vienā rindā ir n skaitļi" -> list(map(int, input().split()))
# - "līdz faila beigām" -> for line in sys.stdin
# ------------------------------------------------------------
