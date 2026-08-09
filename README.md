# 🚇 Optimal Route Finder — Metro-Network-Analysis (Hyderabad Metro)

A Dijkstra's-algorithm shortest path finder for the Hyderabad Metro network. Given any two stations, it computes the minimum **distance** (meters) or **travel time** (minutes) across 56 stations on 3 interconnected lines, and returns the full route.

**🔗 Live demo:** [metro-network-analysis.vercel.app](https://metro-network-analysis.vercel.app/)

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Dijkstra's%20Algorithm-4B5563?style=flat-square" alt="Dijkstra's Algorithm">
  <img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white" alt="Vercel">
  <img src="https://img.shields.io/badge/MIT%20License-yellow?style=flat-square" alt="MIT License">
</p>

---

## Features

- Shortest distance or shortest time between any two stations
- Full route reconstruction — every stop along the way, not just the total
- Covers all 3 lines (Red, Blue, Green) with correct interchange handling
- Graceful handling of invalid station names

## Tech Stack

- **Python 3** — standard library only (`heapq`, `dataclasses`, `typing`)
- **HTML / CSS / JavaScript** — vanilla frontend, no frameworks, runs entirely client-side
- **Vercel** — static hosting for the web app

## How It Works

The metro network is modeled as a weighted, undirected graph: each station is a node, and each connection is an edge carrying both a time and a distance weight. A single generalized Dijkstra implementation finds the shortest path — the weight to optimize (time vs. distance) is passed in as a parameter — and a parent-pointer trace reconstructs the full route.

## Running It

**Web app:** just open the [live demo](https://metro-network-analysis.vercel.app/) — no setup needed. Or open `index.html` locally in any browser.

**Python CLI:**
```bash
python3 metro.py
```
```
Press 1 to show the Station Names
Press 2 to find minimum distance to reach source to destination
Press 3 to find minimum time to reach source to destination
```

| Input | Result |
|---|---|
| `1` | Lists all 56 station names |
| `2` | Prompts for source + destination → shortest distance + route |
| `3` | Prompts for source + destination → shortest time + route |

**Example:**
```
2
Miyapur
LB_Nagar

28500 meters
Route: Miyapur -> JNTU_College -> KPHP_Colony -> ... -> LB_Nagar
```

> Station names are case-sensitive and use underscores — e.g. `LB_Nagar`, `Lakdi-Ka-Pul`, `HITEC_City`. Run option `1` if you're unsure of the exact spelling.

---

<p align="center">
  Made with ❤️ by <strong>Sai Kumar</strong><br>
  DSA enthusiast · BTech IT student
</p>
