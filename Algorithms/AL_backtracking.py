# N QUEENS 
def is_available(candidates, col):
    row = len(candidates)
    # 수직 체크 
    if col in candidates:
        return False
    # 대각선 체크 
    for queen_row in range(row):
        if abs(candidates[queen_row] - col) == row - queen_row:
            return False
    return True

def DFS(N, row, candidates, results):
    if row == N:
        results.append(candidates[:])
        return 
    for col in range(N):
        if is_available(candidates, col):
            candidates.append(col)
            DFS(N, row+1, candidates, results)
            candidates.pop()

def n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result

if __name__ == '__main__':
    print(n_queens(1))

