class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Approach:
        - Use Tarjan's Algorithm to find all critical connections (bridges) in the network.
        - Perform DFS while keeping track of discovery times and low-link values for each node.
        - If the low-link value of a connected node is greater than the discovery time of the current node, the edge is critical.
        Time Complexity:
        - O(V + E), where V is the number of nodes (n) and E is the number of connections.
        - DFS runs in O(V + E) time, and updating low-link values is constant time.
        Space Complexity:
        - O(V + E) for the adjacency list and additional O(V) space for storing discovery, low-link values, and visited nodes.
        """
        # Step 1: Build the adjacency list
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        # Initialize variables
        discovery = [-1] * n  # Discovery time of each node
        low = [-1] * n  # Lowest discovery time reachable from each node
        critical_edges = []  # To store critical connections
        time = 0  # Timer to track discovery time

        def dfs(node, parent):
            nonlocal time
            # Set discovery and low values to the current time
            discovery[node] = low[node] = time
            time += 1

            # Explore neighbors
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Skip the parent node

                if discovery[neighbor] == -1:  # If the neighbor hasn't been visited
                    dfs(neighbor, node)  # Recur for the neighbor
                    # Update the low value for the current node
                    low[node] = min(low[node], low[neighbor])
                    # Check if the edge is a critical connection
                    if low[neighbor] > discovery[node]:
                        critical_edges.append([node, neighbor])
                else:
                    # Update the low value if the neighbor was already visited
                    low[node] = min(low[node], discovery[neighbor])

        # Step 2: Perform DFS from node 0
        for i in range(n):
            if discovery[i] == -1:  # If the node hasn't been visited
                dfs(i, -1)

        return critical_edges
