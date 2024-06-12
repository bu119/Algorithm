def solution(m, musicinfos):
    # 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개
    # 각 음은 1분에 1개씩 재생
    # 음악 길이 < 재생된 시간: 처음부터 반복해서 재생
    # 음악 길이 > 재생된 시간: 처음부터 재생 시간만큼만 재생
    # 조건이 일치하는 음악 중 재생된 시간이 제일 긴 음악 제목을 반환
    # 재생된 시간도 같을 경우, 먼저 입력된 음악 제목 반환
    # 조건이 일치하는 음악이 없을 때, “(None)” 반환
    
    # 기억한 멜로디를 담은 문자열 m은 음 1개 이상 1439개 이하
    # musicinfos: 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열
    # 음악의 시작 시각과 끝난 시각은 24시간 HH:MM 형식
    m = m.replace('A#','a')
    m = m.replace('B#','b')
    m = m.replace('C#','c')
    m = m.replace('D#','d')
    m = m.replace('F#','f')
    m = m.replace('G#','g')
    
    answer = {'title': '(None)', 'maxplaytime': 0}
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        
        music = music.replace('A#','a')
        music = music.replace('B#','b')
        music = music.replace('C#','c')
        music = music.replace('D#','d')
        music = music.replace('F#','f')
        music = music.replace('G#','g')
        
        # 음악 전체 길이 (#포함)
        n = len(music)
        # 총 재생 시간
        starthour, startMinute = map(int, start.split(':'))
        endhour, endMinute = map(int, end.split(':'))
        playtime = (endhour-starthour) * 60 + (endMinute-startMinute)
        # 음악 길이 < 재생된 시간: 처음부터 반복해서 재생
        # 음악 길이 > 재생된 시간: 처음부터 재생 시간만큼만 재생
        # 조건이 일치하는 음악 중 재생된 시간이 제일 긴 음악 제목을 반환
        playmusic = (playtime // n) * music
        playmusic += music[:(playtime % n)]
        
        if m in playmusic and answer['maxplaytime'] < playtime:
            answer['maxplaytime'] = playtime
            answer['title'] = title
            
    return answer['title']