# 1110번_더하기 사이클

## 0 < N < 99의 정수, 사이클 길이 출력
## 26으로 시작한다면 2+6 = 8, 새로운 수 68
## 68은 다시 6+8=14, 새로운 수 84
## 84는 다시 8+4=12, 새로운 수 42
## 42는 다시 4+2=6, 새로운 수 26
## 위 예는 4번 만에 원래 수로 돌아옴. 사이클 길이 4


N = int(input())

num = N #초기 변수 설정, N값을 바꿔줘야 while문이 무한루프를 돌지 않음
cycle_len = 0 #사이클 초기 길이 0

while True :
    cycle = N//10 + N%10 #26에서 2+6부분.
    new_num = (N%10)*10 + cycle%10 #26에서 6이 60, 2+8은 8로 68만들기
    
    cycle_len += 1 #사이클 길이 1씩 추가

    N = new_num #N값 새로운 숫자로 바꿔줘야 while문 반복 시 첫 줄에서 바뀐 값으로 재실행됨

    if new_num == num : #초기에 설정한 N값과, 새로운 값 비교
        break

print(cycle_len)