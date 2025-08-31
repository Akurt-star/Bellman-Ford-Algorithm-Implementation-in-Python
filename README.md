# Bellman-Ford Algorithm in Python

This project demonstrates the **Bellman-Ford algorithm** implemented in Python using [NetworkX](https://networkx.org/) for graph representation and [Matplotlib](https://matplotlib.org/) for visualization.  

The Bellman-Ford algorithm is used to compute the shortest paths from a single source node to all other nodes in a weighted directed graph. Unlike Dijkstra’s algorithm, Bellman-Ford can handle **negative weight edges** and detect **negative weight cycles**.

---

## ✨ Features
- Computes shortest path distances from a source node.
- Stores both **distance** and **path** for each node.
- Detects **negative weight cycles** and reports them.
- Stops early if no updates occur in a relaxation round (optimization).
- Visualizes the graph with edge weights using `matplotlib`.

---
# 🔍 Dijkstra’s vs Bellman-Ford Algorithm

Understanding the differences between **Dijkstra’s algorithm** and the **Bellman-Ford algorithm** is important when choosing the right shortest-path method for a problem.  

---

## 1. Negative Weights
- **Dijkstra’s Algorithm**
  - ❌ Does **not work** with negative edge weights.  
  - Assumes once a node’s shortest path is found, it never changes (fails with negative weights).
- **Bellman-Ford Algorithm**
  - ✅ Works with **negative edge weights**.  
  - Can also **detect negative weight cycles**.

---

## 2. Complexity
- **Dijkstra’s Algorithm**
  - With min-priority queue (binary heap):  
    ```
    O((V + E) log V)
    ```
  - Faster in practice for large graphs with non-negative weights. (e.g. Maps in real life, it can be extend as A*)
- **Bellman-Ford Algorithm**
  - Runs in:
    ```
    O(V * E)
    ```
  - Slower, since it relaxes all edges up to |V|-1 times.

---

## 3. Approach
- **Dijkstra’s**
  - **Greedy algorithm.**
  - Picks the “closest” unexplored node at each step, then expands.  
  - Similar to BFS but with weighted edges.
- **Bellman-Ford**
  - **Dynamic programming approach.**
  - Iteratively relaxes all edges, ensuring correctness even with negative weights.

---

## 4. Use Cases
- **Dijkstra’s Algorithm**
  - Works when all edge weights are **non-negative**.
  - Common in routing, GPS, and network optimization.
- **Bellman-Ford Algorithm**
  - Needed when the graph may have **negative edges**.
  - Used in problems like **currency arbitrage detection** (negative cycle = profit loop).

---

## 5. Cycle Handling
- **Dijkstra’s**
  - Cannot detect negative cycles.
- **Bellman-Ford**
  - ✅ Detects negative weight cycles in its final step.

---

## 📊 Quick Comparison Table

| Feature                | Dijkstra’s                | Bellman-Ford              |
|-------------------------|---------------------------|---------------------------|
| Negative weights        | ❌ Not supported          | ✅ Supported               |
| Negative cycle detect   | ❌ No                     | ✅ Yes                     |
| Time complexity         | O((V+E) log V) (with PQ) | O(V * E)                  |
| Algorithm type          | Greedy                   | Dynamic Programming       |
| Typical use case        | Fast routing (GPS, maps) | Graphs with negative edges|

---

## ✅ Summary
- Use **Dijkstra’s** when the graph has **no negative edges** and you need speed.  
- Use **Bellman-Ford** when negative edges are possible or when you need to check for **negative cycles**.  

---

