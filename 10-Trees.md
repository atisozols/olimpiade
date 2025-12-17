# 10 — Koki (Trees): DFS/BFS, BST

## Ko jāzina
- DFS: preorder / inorder / postorder
- BFS: līmeņos
- BST īpašība: kreisais < sakne < labais

## DFS šablons (rekursija)
```py
def dfs(node):
    if not node:
        return
    # preorder: apstrādā node
    dfs(node.left)
    # inorder: apstrādā node
    dfs(node.right)
```

## Uzdevumi
1. Aprēķini koka augstumu.
2. Pārbaudi, vai koks ir simetrisks.
3. Atrodi LCA bināram kokam (grūtāks).

## NeetCode piemēri
- Maximum Depth of Binary Tree
- Invert Binary Tree
