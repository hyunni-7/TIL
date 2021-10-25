"""" Data

# description
    # num of nodes, num of edges
    # node idx(from), node idx(to), weight

8 10
1 2 51
1 7 87
1 8 42
2 3 39
3 4 46
3 8 27
4 5 35
5 6 7
6 7 18
6 8 65
"""

import sys
import heapq
# from print_2d_arr import print_2d_arr


def Dijkstra(s):
    """
    시작 정점에서 목적 정점까지의 최소 비용(거리) 계산
        * 음의 가중치를 허용 하지 않음
        * 추가 학습
            1. Bellman-Ford algorithm (음의 가중치 허용)
            2. Floyd-Warshall algorithm (모든 정점에 대한 최소 비용(거리) 계산)
    """
    hq = []
    heapq.heappush(hq, (0, s))  # cost, node idx

    costs[s] = 0  # cost initialization

    while hq:
        cost, now = heapq.heappop(hq)

        for ncost, nex in graph[now]:
            # 현재까지의 비용에서 앞으로의 비용을 더했을 때, 이 값이 현재 저장되어 있는 최소 비용보다 크다면, 고려 X
            if costs[nex] <= cost + ncost:
                continue
            # 그렇지 않다면, 해당 비용으로 최소 비용 갱신
            costs[nex] = cost + ncost
            # 탐색 목록에 추가
            heapq.heappush(hq, (costs[nex], nex))


V, E = map(int, sys.stdin.readline().split())
# 인접 리스트(무방향성)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s] += [(w, e)]
    graph[e] += [(w, s)]
# print_2d_arr(graph, V+1)

costs = [0] + [987654321] * V  # 각 지점까지의 최소 비용 저장

s = 2  # 시작점
Dijkstra(s)  # Dijkstra 알고리즘 적용

# 결과
for i in range(1, V+1):
    print(f'the minimum cost from idx {s} to idx {i}: {costs[i]}')
    print('-' * 80)
