
def addEdge(adj, x, y):
    adj[x].append(y)
    adj[y].append(x)

def read_graph_from_file(filename):
    with open(filename, "r") as file:
        N = int(file.readline().strip())
        adj = [[] for _ in range(N + 1)]
        for _ in range(N):
            line = list(map(int, file.readline().split()))
            for i in range(1, len(line)):
                addEdge(adj, line[0], line[i])
        return adj, N   
 
 
def dfs(adj, dp, src, par):
    for child in adj[src]:
        if child != par:
            dfs(adj, dp, child, src)
 
    for child in adj[src]:
        if child != par:
            # not including source in the vertex cover
            dp[src][0] = dp[child][1] + dp[src][0]
 
            # including source in the vertex cover
            dp[src][1] = dp[src][1] + min(dp[child][1], dp[child][0])
 
 
def minSizeVertexCover(adj, N):
    dp = [[0 for j in range(2)] for i in range(N+1)]
    for i in range(1, N+1):
        # 0 denotes not included in vertex cover
        dp[i][0] = 0
 
        # 1 denotes included in vertex cover
        dp[i][1] = 1
 
    dfs(adj, dp, 1, -1)
 
    # printing minimum size vertex cover
    print("Sol dp : ", min(dp[1][0], dp[1][1]))
 

def main(inputfile, vertex):
    filename = inputfile
    adj, N = read_graph_from_file(filename)
    
    minSizeVertexCover(adj, N)

