
# Pacific Atlantic Water Flow
def pacific_atlantic(matrix):
    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    pacific = set()
    atlantic = set()
    
    def dfs(r, c, visited):
        visited.add((r, c))
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and matrix[nr][nc] >= matrix[r][c]:
                dfs(nr, nc, visited)
    
    for r in range(rows):
        dfs(r, 0, pacific)
        dfs(r, cols-1, atlantic)
    for c in range(cols):
        dfs(0, c, pacific)
        dfs(rows-1, c, atlantic)
    
    return [[r, c] for r, c in pacific & atlantic]

# Backfill update on 2022-01-12 13:09:22
# Authored by backfill-2022.sh
# Backfill update on 2022-01-13 19:08:32
# Authored by backfill-2022.sh
# Backfill update on 2022-01-19 19:46:10
# Authored by backfill-2022.sh
# Backfill update on 2022-01-20 12:50:55
# Authored by backfill-2022.sh
# Backfill update on 2022-01-20 15:29:04
# Authored by backfill-2022.sh
# Backfill update on 2022-01-31 12:31:29
# Authored by backfill-2022.sh
# Backfill update on 2022-01-31 17:51:34
# Authored by backfill-2022.sh
# Backfill update on 2022-02-09 12:49:52
# Authored by backfill-2022.sh
# Backfill update on 2022-02-26 17:36:10
# Authored by backfill-2022.sh
# Backfill update on 2022-02-27 18:21:21
# Authored by backfill-2022.sh
# Backfill update on 2022-02-28 16:19:06
# Authored by backfill-2022.sh
# Backfill update on 2022-02-28 20:50:35
# Authored by backfill-2022.sh
# Backfill update on 2022-03-01 18:54:48
# Authored by backfill-2022.sh
# Backfill update on 2022-03-01 20:21:42
# Authored by backfill-2022.sh
# Backfill update on 2022-03-02 15:44:58
# Authored by backfill-2022.sh
# Backfill update on 2022-03-07 20:40:27
# Authored by backfill-2022.sh
# Backfill update on 2022-03-09 13:58:52
# Authored by backfill-2022.sh
# Backfill update on 2022-03-21 20:07:17
# Authored by backfill-2022.sh
