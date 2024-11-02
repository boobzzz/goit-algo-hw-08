import heapq


def get_min_cost(cables):
    heapq.heapify(cables)
    total_cost = 0
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        combined = first + second
        total_cost += combined

        heapq.heappush(cables, combined)

    return total_cost


cables = [4, 3, 2, 6]
min_cost = get_min_cost(cables)
print(f"Мінімальні витрати на з'єднання кабелів: {min_cost}")
