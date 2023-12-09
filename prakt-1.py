import sys
import networkx as nx
import matplotlib.pyplot as plt

def find(idx, prev_idx, n, a, dp, G):
    if idx == n:
        return 0

    if dp[idx][prev_idx + 1] != -1:
        return dp[idx][prev_idx + 1]

    notTake = 0 + find(idx + 1, prev_idx, n, a, dp, G)
    take = -sys.maxsize - 1
    if prev_idx == -1 or a[idx] > a[prev_idx]:
        take = 1 + find(idx + 1, idx, n, a, dp, G)

    dp[idx][prev_idx + 1] = max(take, notTake)

    if prev_idx != -1:
        G.add_edge(prev_idx, idx, weight=dp[idx][prev_idx + 1])

    return dp[idx][prev_idx + 1]

def longestSubsequence(n, a):
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    G = nx.DiGraph()
    length = find(0, -1, n, a, dp, G)
    return length, G

# Example usage:
a = [4, 1, 13, 7, 0, 2, 8, 11, 3]
n = len(a)

length, tree = longestSubsequence(n, a)

# Visualization
pos = nx.spring_layout(tree)
labels = nx.get_edge_attributes(tree, 'weight')
nx.draw(tree, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=8, font_color="black", font_weight="bold")
nx.draw_networkx_edge_labels(tree, pos, edge_labels=labels, font_color='red')
plt.title("Recursion Tree for Longest Increasing Subsequence")
plt.show()

print("Length of LIS is", length)
