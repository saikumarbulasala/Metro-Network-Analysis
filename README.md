# 🚇 Optimal Route Finder — Hyderabad Metro

A Dijkstra's-algorithm-based shortest path finder for the Hyderabad Metro network. Computes the minimum **distance** or **travel time** between any two stations across 56 stations on 3 interconnected lines, and reconstructs the full route.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Algorithm-Dijkstra-blueviolet?style=for-the-badge" alt="Dijkstra's Algorithm">
  <img src="https://img.shields.io/badge/Data%20Structure-Priority%20Queue-orange?style=for-the-badge" alt="Priority Queue">
  <img src="https://img.shields.io/badge/Stations-56-2FAE66?style=for-the-badge" alt="56 Stations">
  <img src="https://img.shields.io/badge/Live%20Demo-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Live Demo">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License">
</p>

### 🔗 [**Live Demo →**](https://metro-network-analysis.vercel.app/)

Try it right now — pick a source and destination station and see the shortest route rendered on a schematic metro map.

---

## ✨ Features

- 🔎 **Shortest distance** between any two stations, in meters
- ⏱️ **Shortest time** between any two stations, in minutes
- 🧭 **Full route reconstruction** — see every stop along the way, not just the total
- 🚦 Covers all **3 metro lines** (Red, Blue, Green) with correct interchange handling
- ✅ Graceful handling of invalid station names

## 🛠️ Tech Stack

| | |
|---|---|
| <img src="https://img.icons8.com/color/48/python.png" width="28"/> **Language** | Python 3 (standard library only — `heapq`, `dataclasses`, `typing`) |
| <img src="https://img.icons8.com/fluency/48/graph.png" width="28"/> **Algorithm** | Dijkstra's shortest path, generalized over distance/time weights |
| <img src="https://img.icons8.com/fluency/48/data-configuration.png" width="28"/> **Data Structure** | Adjacency list graph + binary heap priority queue |
| <img src="https://img.icons8.com/color/48/html-5--v1.png" width="28"/> **Frontend** | Vanilla HTML/CSS/JavaScript — no frameworks, runs entirely client-side |
| <img src="https://img.icons8.com/color/48/vercel.png" width="28"/> **Deployment** | [Vercel](https://vercel.com) (static hosting) |

## 🌐 Web App

A live, interactive version is deployed at **[metro-network-analysis.vercel.app](https://metro-network-analysis.vercel.app/)** — pick stations from dropdowns, toggle between shortest distance/time, and see the route rendered on a schematic transit map, color-coded by line.

To run it locally instead, just open `index.html` in any browser — no server or build step needed.

## 🚀 Getting Started (Python CLI)

### Prerequisites
Just Python 3 — no external packages required.

```bash
python3 --version   # 3.8+ recommended
```

### Run it

```bash
python3 metro.py
```

You'll see:

```
Press 1 to show the Station Names
Press 2 to find minimum distance to reach source to destination
Press 3 to find minimum time to reach source to destination
```

| Input | What it does |
|---|---|
| `1` | Lists all 56 station names |
| `2` | Prompts for source + destination → shortest **distance** (meters) + full route |
| `3` | Prompts for source + destination → shortest **time** (minutes) + full route |

### Example

```
2
Miyapur
LB_Nagar

28500 meters
Route: Miyapur -> JNTU_College -> KPHP_Colony -> Kukatpally -> ... -> LB_Nagar
```

> ⚠️ **Station names are case-sensitive and use underscores** — e.g. `LB_Nagar`, `Lakdi-Ka-Pul`, `HITEC_City`. Run option `1` first if you're unsure of exact spelling.

## 🧠 How It Works

The metro network is modeled as a weighted, undirected graph — each station is a node, each connection is an edge carrying both a time and a distance weight. A single generalized Dijkstra implementation finds the shortest path, selecting which weight to optimize for via a function parameter, and a parent-pointer trace reconstructs the full route from source to destination.

## 📄 License

MIT — feel free to use, modify, and learn from this project.
