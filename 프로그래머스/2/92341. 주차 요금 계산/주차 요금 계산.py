# 출차된 내역이 없습니다. 따라서, 23:59에 출차된 것으로 간주
# 차량별 누적 주차 시간을 계산하여 요금을 일괄로 정산합니다.
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
from math import ceil

def solution(fees, records):
    answer = []
    # fees: 기본 시간(분), 기본 요금(원),	단위 시간(분), 단위 요금(원)
    basicTime, basicFee, unitTime, unitFee = fees
    # inCar = {차량번호: 입차시각(분)}
    inCar = {}
    # totalParkingTime = {차량번호: 누적 주차 시간}
    # 누적 시간 저장
    totalParkingTime = {}
    # 출차 입력 없으면 마지막 시각(23:59)에 출차
    lastTime = 23*60 + 59 
    
    for record in records:
        time, carNum, status = record.split()
        hour, minute = map(int, time.split(':'))
        recordTime = hour*60 + minute

        if status == 'IN':
            # 입차
            # 주차 시작 시간 저장 
            inCar[carNum] = recordTime
            # 누적 주차 시간 저장할 공간 만들기
            if carNum not in totalParkingTime:
                # 기본시간 - 로 저장
                totalParkingTime[carNum] = -basicTime
        else:
            # 출차
            # 주차 시간
            parkingTime = recordTime - inCar[carNum]
            # 누적 시간 있으면 저장
            totalParkingTime[carNum] += parkingTime
            # 00:00 부터 가능하므로 -1로 주차 시작 시간 초기화 (주차 여러번 가능)
            inCar[carNum] = -1

    # 출차된 내역이 없는 차량 시간 누적 및 요금 계산
    for i in sorted(inCar):
        # 출차된 내역이 없는 차량 
        if inCar[i] >= 0:
            # 주차 시간 (기본 시간 제외)
            parkingTime = lastTime - inCar[i]
            # 누적 시간 저장 (기본 시간 제외)
            totalParkingTime[i] += parkingTime
            # 주차 시작 시간 초기화 (주차 여러번 가능)
            inCar[i] = 0
        
        # 출차 요금 계산
        parkingFee = basicFee
        if totalParkingTime[i] > 0:
            # 계산할 전체 주차 추가 요금 (올림)
            parkingFee += ceil(totalParkingTime[i] / unitTime) * unitFee

        answer.append(parkingFee)

    return answer