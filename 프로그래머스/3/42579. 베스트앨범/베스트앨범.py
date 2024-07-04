# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
# 노래는 고유 번호로 구분

# 노래를 먼저 수록하는 기준
# 속한 노래가 많이 재생된 장르
# 장르 내에서 많이 재생된 노래
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래

def solution(genres, plays):
    answer = []
    # 장르 재생 횟수
    genre_play_cnt = {}
    # 장르에 해당하는 고유번호
    genre_id = {}
    n = len(genres)
    for i in range(n):
        # 고유번호에 해당하는 장르
        if genres[i] in genre_id:
            genre_play_cnt[genres[i]] += plays[i]
            genre_id[genres[i]].append((-plays[i], i))
        else:
            genre_play_cnt[genres[i]] = plays[i]
            genre_id[genres[i]] = [(-plays[i], i)]

    # value 값으로 정렬: 내림차순
    play = sorted(genre_play_cnt.items(), key=lambda x: x[1], reverse=True)

    # 가장 많이 재생된 순으로 탐색
    for genre in play:
        for cnt, music_id in sorted(genre_id[genre[0]])[:2]:
            answer.append(music_id)

    return answer