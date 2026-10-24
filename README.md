
# K-Beam Search

A recursive implementation of beam-style search on an undirected graph,
written as a learning exercise.

> ⚠️ **Note:** This is a *learning implementation*, not textbook k-beam
> search. It prunes per-node rather than maintaining a single global beam
> across a level. See [Limitations](#limitations) below.

---

## What is beam search?

Beam search is a heuristic search algorithm. At each level it expands a
set of candidate nodes (the **beam**), scores all their neighbors, and
keeps only the best **k** as the next beam. This prunes the search space
at the cost of possibly missing the optimal path.

- `k = 1` → greedy (keeps only the single best)
- large `k` → closer to exhaustive search (slower, more memory)

---

## How this implementation works

Recursive, per-node approach:

1. Check the current node against the goal.
2. Look at all neighbors of the current node.
3. Collect their heuristic values.
4. Keep the **k best** heuristic values.
5. Select neighbors whose heuristic is among those k values.
6. If the goal is among the selected neighbors → return the path.
7. Otherwise recurse into each selected neighbor.
8. A shared `visited` set prevents infinite loops on cyclic graphs.

> Note: this picks the top-k **of each node's own neighbors**, not
> across the whole level. That is why it is labelled a learning
> implementation (see Limitations).

---

## Usage

```python
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2],
}

heuristics = {0: 4, 1: 3, 2: 1, 3: 5, 4: 0}   # lower = closer to goal

path = K_BEAM_SEARCH(graph, heuristics, k=2, s=0, goal=4)
print(path)   # [0, 2, 4]
