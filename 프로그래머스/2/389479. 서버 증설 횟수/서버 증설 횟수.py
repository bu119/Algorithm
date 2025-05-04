from collections import deque

def solution(players, m, k):
    # 서버 증설 횟수 저장
    answer = 0
    # 증설된 서버들의 남은 시간 저장
    servers = deque()
    for player in players:
        # 증설되어야하는 서버 수 (필요한 서버 수 - 중설된 서버 수)
        required_servers = player//m - len(servers)
        # 서버가 추가로 필요하면
        if required_servers > 0:
            # 서버를 필요한 만큼 추가하고
            for i in range(required_servers):
                servers.append(k)
            # 서버 증설 횟수도 추가
            answer += required_servers
        # 서버 시간 감소 시키기
        for _ in range(len(servers)):
            server_time = servers.popleft()
            if server_time > 1:
                servers.append(server_time - 1)
    
    return answer