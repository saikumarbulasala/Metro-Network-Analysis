"""
Optimal Route Finder - Hyderabad Metro
A Python port of the Java Dijkstra-based shortest path finder.

Given a source and destination station, finds either the shortest
distance (meters) or shortest time (minutes) route across the
Red, Blue, and Green metro lines, and prints the full route.
"""

import heapq
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional


@dataclass
class Edge:
    """A connection from one station to a neighboring station."""
    neighbor: str
    time: int      # minutes
    distance: int  # meters


METRO_MAP = {
    "Miyapur": [
        Edge("JNTU_College", time=3, distance=1800),
    ],
    "JNTU_College": [
        Edge("Miyapur", time=3, distance=1800),
        Edge("KPHP_Colony", time=3, distance=1400),
    ],
    "KPHP_Colony": [
        Edge("JNTU_College", time=3, distance=1400),
        Edge("Kukatpally", time=3, distance=1500),
    ],
    "Kukatpally": [
        Edge("KPHP_Colony", time=3, distance=1500),
        Edge("Balanagar", time=2, distance=1500),
    ],
    "Balanagar": [
        Edge("Kukatpally", time=2, distance=1500),
        Edge("Moosapet", time=2, distance=600),
    ],
    "Moosapet": [
        Edge("Balanagar", time=2, distance=600),
        Edge("Bharat_Nagar", time=2, distance=1000),
    ],
    "Bharat_Nagar": [
        Edge("Moosapet", time=2, distance=1000),
        Edge("Erragadda", time=2, distance=900),
    ],
    "Erragadda": [
        Edge("Bharat_Nagar", time=2, distance=900),
        Edge("ESI_Hospital", time=2, distance=200),
    ],
    "ESI_Hospital": [
        Edge("Erragadda", time=2, distance=200),
        Edge("SR_Nagar", time=2, distance=1700),
    ],
    "SR_Nagar": [
        Edge("ESI_Hospital", time=2, distance=1700),
        Edge("Ameerpet", time=2, distance=700),
    ],
    "Ameerpet": [
        Edge("SR_Nagar", time=2, distance=700),
        Edge("Begumpet", time=2, distance=1600),
        Edge("Madhura_Nagar", time=2, distance=700),
        Edge("Panjagutta", time=3, distance=1300),
    ],
    "Panjagutta": [
        Edge("Ameerpet", time=3, distance=1300),
        Edge("Irrum_Manzil", time=2, distance=1000),
    ],
    "Irrum_Manzil": [
        Edge("Panjagutta", time=2, distance=1000),
        Edge("Khairatabad", time=3, distance=1200),
    ],
    "Khairatabad": [
        Edge("Irrum_Manzil", time=3, distance=1200),
        Edge("Lakdi-Ka-Pul", time=2, distance=1200),
    ],
    "Lakdi-Ka-Pul": [
        Edge("Khairatabad", time=2, distance=1200),
        Edge("Assembly", time=2, distance=1100),
    ],
    "Assembly": [
        Edge("Lakdi-Ka-Pul", time=2, distance=1100),
        Edge("Nampally", time=2, distance=700),
    ],
    "Nampally": [
        Edge("Assembly", time=2, distance=700),
        Edge("Gandhi_Bhavan", time=2, distance=800),
    ],
    "Gandhi_Bhavan": [
        Edge("Nampally", time=2, distance=800),
        Edge("Osmania_Medical_College", time=2, distance=800),
    ],
    "Osmania_Medical_College": [
        Edge("Gandhi_Bhavan", time=2, distance=800),
        Edge("MG_Bus_Station", time=2, distance=900),
    ],
    "MG_Bus_Station": [
        Edge("Osmania_Medical_College", time=2, distance=900),
        Edge("Sulthan_Bazaar", time=3, distance=2100),
        Edge("Malakpet", time=2, distance=800),
    ],
    "Malakpet": [
        Edge("MG_Bus_Station", time=2, distance=800),
        Edge("New_Market", time=2, distance=1200),
    ],
    "New_Market": [
        Edge("Malakpet", time=2, distance=1200),
        Edge("Musarambagh", time=2, distance=1000),
    ],
    "Musarambagh": [
        Edge("New_Market", time=2, distance=1000),
        Edge("Dilsukhnagar", time=3, distance=1500),
    ],
    "Dilsukhnagar": [
        Edge("Musarambagh", time=3, distance=1500),
        Edge("Chaitanyapuri", time=2, distance=1100),
    ],
    "Chaitanyapuri": [
        Edge("Dilsukhnagar", time=2, distance=1100),
        Edge("Victoria_Memorial", time=2, distance=1200),
    ],
    "Victoria_Memorial": [
        Edge("Chaitanyapuri", time=2, distance=1200),
        Edge("LB_Nagar", time=2, distance=1400),
    ],
    "LB_Nagar": [
        Edge("Victoria_Memorial", time=2, distance=1400),
    ],
    "Raidurg": [
        Edge("HITEC_City", time=2, distance=1500),
    ],
    "HITEC_City": [
        Edge("Raidurg", time=2, distance=1500),
        Edge("Durgam_Cheruvu", time=2, distance=900),
    ],
    "Durgam_Cheruvu": [
        Edge("HITEC_City", time=2, distance=900),
        Edge("Madhapur", time=3, distance=1600),
    ],
    "Madhapur": [
        Edge("Durgam_Cheruvu", time=3, distance=1600),
        Edge("Peddamma_Gudi", time=2, distance=1200),
    ],
    "Peddamma_Gudi": [
        Edge("Madhapur", time=2, distance=1200),
        Edge("Jubilee_Hills_Check_Post", time=2, distance=700),
    ],
    "Jubilee_Hills_Check_Post": [
        Edge("Peddamma_Gudi", time=2, distance=700),
        Edge("Road_No_5_Jubilee_Hills", time=3, distance=1400),
    ],
    "Road_No_5_Jubilee_Hills": [
        Edge("Jubilee_Hills_Check_Post", time=3, distance=1400),
        Edge("Yusufguda", time=2, distance=900),
    ],
    "Yusufguda": [
        Edge("Road_No_5_Jubilee_Hills", time=2, distance=900),
        Edge("Madhura_Nagar", time=3, distance=1500),
    ],
    "Madhura_Nagar": [
        Edge("Yusufguda", time=3, distance=1500),
        Edge("Ameerpet", time=2, distance=700),
    ],
    "Begumpet": [
        Edge("Ameerpet", time=2, distance=1600),
        Edge("Prakash_Nagar", time=2, distance=1400),
    ],
    "Prakash_Nagar": [
        Edge("Begumpet", time=2, distance=1400),
        Edge("Rasoolpura", time=2, distance=1100),
    ],
    "Rasoolpura": [
        Edge("Prakash_Nagar", time=2, distance=1100),
        Edge("Paradise", time=2, distance=1100),
    ],
    "Paradise": [
        Edge("Rasoolpura", time=2, distance=1100),
        Edge("Parade_Ground", time=2, distance=1200),
    ],
    "Parade_Ground": [
        Edge("Paradise", time=2, distance=1200),
        Edge("Secundherabad_West", time=2, distance=1000),
        Edge("Secundherabad_East", time=3, distance=1500),
    ],
    "Secundherabad_East": [
        Edge("Parade_Ground", time=3, distance=1500),
        Edge("Mettuguda", time=3, distance=1900),
    ],
    "Mettuguda": [
        Edge("Secundherabad_East", time=3, distance=1900),
        Edge("Tarnaka", time=2, distance=1300),
    ],
    "Tarnaka": [
        Edge("Mettuguda", time=2, distance=1300),
        Edge("Habsiguda", time=3, distance=1600),
    ],
    "Habsiguda": [
        Edge("Tarnaka", time=3, distance=1600),
        Edge("NGRI", time=2, distance=800),
    ],
    "NGRI": [
        Edge("Habsiguda", time=2, distance=800),
        Edge("Stadium", time=2, distance=1200),
    ],
    "Stadium": [
        Edge("NGRI", time=2, distance=1200),
        Edge("Uppal", time=2, distance=1100),
    ],
    "Uppal": [
        Edge("Stadium", time=2, distance=1100),
        Edge("Nagole", time=2, distance=1000),
    ],
    "Nagole": [
        Edge("Uppal", time=2, distance=1000),
    ],
    "Secundherabad_West": [
        Edge("Parade_Ground", time=2, distance=1000),
        Edge("Gandhi_Hospital", time=2, distance=1000),
    ],
    "Gandhi_Hospital": [
        Edge("Secundherabad_West", time=2, distance=1000),
        Edge("Musheerabad", time=2, distance=1500),
    ],
    "Musheerabad": [
        Edge("Gandhi_Hospital", time=2, distance=1500),
        Edge("RTC_X_Roads", time=2, distance=1300),
    ],
    "RTC_X_Roads": [
        Edge("Musheerabad", time=2, distance=1300),
        Edge("Chikkadpally", time=3, distance=1900),
    ],
    "Chikkadpally": [
        Edge("RTC_X_Roads", time=3, distance=1900),
        Edge("Narayanaguda", time=1, distance=900),
    ],
    "Narayanaguda": [
        Edge("Chikkadpally", time=1, distance=900),
        Edge("Sulthan_Bazaar", time=2, distance=1400),
    ],
    "Sulthan_Bazaar": [
        Edge("Narayanaguda", time=2, distance=1400),
        Edge("MG_Bus_Station", time=3, distance=2100),
    ],
}

def dijkstra(
    source: str,
    metro_map: Dict[str, List[Edge]],
    weight_of,
) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    """
    Generic Dijkstra's shortest path.

    weight_of is a function (Edge -> int) that selects which field to
    optimize for - lambda e: e.distance for shortest distance, or
    lambda e: e.time for shortest time - so we don't need two separate
    copies of this algorithm.

    Returns (dist, parent):
      dist   - shortest cost from source to every reachable station
      parent - predecessor of each station on its shortest path, used
               to reconstruct the route
    """
    dist = {station: float("inf") for station in metro_map}
    parent: Dict[str, Optional[str]] = {station: None for station in metro_map}
    dist[source] = 0

    # (cost, station) min-heap
    pq = [(0, source)]

    while pq:
        cost, current = heapq.heappop(pq)
        if cost > dist[current]:
            continue  # stale entry, skip

        for edge in metro_map[current]:
            new_cost = cost + weight_of(edge)
            if new_cost < dist[edge.neighbor]:
                dist[edge.neighbor] = new_cost
                parent[edge.neighbor] = current
                heapq.heappush(pq, (new_cost, edge.neighbor))

    return dist, parent


def build_route(source: str, destination: str, parent: Dict[str, Optional[str]]) -> Optional[List[str]]:
    """Reconstructs the station-by-station route using the parent map."""
    if source == destination:
        return [source]

    route = []
    at: Optional[str] = destination
    while at is not None:
        route.append(at)
        if at == source:
            break
        at = parent[at]

    if not route or route[-1] != source:
        return None  # no path found

    route.reverse()
    return route


def shortest_distance(source: str, destination: str, metro_map: Dict[str, List[Edge]]) -> None:
    dist, parent = dijkstra(source, metro_map, weight_of=lambda e: e.distance)
    print(f"{dist[destination]} meters")
    route = build_route(source, destination, parent)
    print("Route: " + " -> ".join(route) if route else "No route found.")


def shortest_time(source: str, destination: str, metro_map: Dict[str, List[Edge]]) -> None:
    dist, parent = dijkstra(source, metro_map, weight_of=lambda e: e.time)
    print(f"{dist[destination]} minutes")
    route = build_route(source, destination, parent)
    print("Route: " + " -> ".join(route) if route else "No route found.")


def print_stations(metro_map: Dict[str, List[Edge]]) -> None:
    for station in metro_map:
        print(station)


def main() -> None:
    print("Press 1 to show the Station Names")
    print("Press 2 to find minimum distance to reach source to destination")
    print("Press 3 to find minimum time to reach source to destination")
    choice = input().strip()

    if choice == "1":
        print_stations(METRO_MAP)
    elif choice in ("2", "3"):
        source = input().strip()
        destination = input().strip()
        if source not in METRO_MAP or destination not in METRO_MAP:
            print("Enter Valid Stations")
            return
        if choice == "2":
            shortest_distance(source, destination, METRO_MAP)
        else:
            shortest_time(source, destination, METRO_MAP)
    else:
        print("Enter Valid Choice")


if __name__ == "__main__":
    main()
