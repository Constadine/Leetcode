edges = [[1, 18], [18, 2], [3, 18], [18, 4], [18, 5], [6, 18], [18, 7], [18, 8], [
    18, 9], [18, 10], [18, 11], [12, 18], [18, 13], [18, 14], [15, 18], [16, 18], [17, 18]]

cnt = 0
for i in range(1, len(edges) + 2):
    for j in range(len(edges)):
        if i in edges[j]:
            cnt += 1
            if cnt == len(edges):
                print(i)
        else:
            cnt = 0
