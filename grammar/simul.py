'''

구현 팁
1. 구현을 최대한 쉽게 하자
2. 개발 관점에서 진짜 안 좋은 코드들일 수 있따
ex) 전역변수, 메모리 3~4배


구현 => 구현, 아이디어, 배경지식

애드혹 : 아이디어 + 구현


여기서 이대로 따라가면서 구현해봐라 : 시뮬레이션 => 구현


'''


'''
1. 전체적인 설계
2. 쉬운 구현 문제를 빠르게 풀 수 있어야 된다.


'''



'''
# 물 복사

삼성 시뮬레이션 문제에서 자주 나오는 컨셉
=> 2차원 평면에서 어떤 객체들이 이동, 소멸, 생성
=> 객체의 위치 등에 대한 정보(속도, 가치, 무게 등!) 어떻게 저장할 거냐

1. 똑같은 2차원 배열을 만들어서, [i][j] 위치에 객체가 있는지?
ex) 없는 곳 다 False, 있는 곳 True // 크기를 넣을 수도 있고
있다면 그 객체에 대한 정보를 그 위치에 저장.

2. 객체의 정보를 단순히 1차원 배열에 나열해서 저장.
[[3, 0], [3, 1], [4, 0], [4, 1]]에 있다.


둘을 모두 들고 있어도 됨. => 경우에 따라서 필요한 거 사용

1 => 2를 만드는 건 어렵지 않다.
2 => 1을 만드는 것도 어렵지 않다.


'''


'''
# 물 복사


주변 값들을 참조해서 내가 바뀌는 문제
=> 원본 배열은 그대로 두고 값이 바뀌는 건 새로운 배열에 적용한 후 원본 배열에 복사
왜냐면 원본 배열 자체에서 바뀌면,
동시에 바뀌어야 하는 다른 값이 바뀐 값에 영향을 받아서 코드가 꼬인다.

바뀌는 과정은 순차적으로 일어날 수 밖에 없기 때문에!!
(동시에 바꾸는 걸 원해도 코드는 순차적으로 짤 수 밖에 없다)


'''

'''

# 미세먼지

쉬프트할 때

미는 게 나오면 밀지 말고 반대쪽에서 당겨 오자

x = arr[8] 맨 마지막 거 저장해놓고
for i in range(7)[::-1]:
  arr[i + 1] = arr[i]

arr[0] = x

0   1   2   3   4   5   6   7   8
a   b   c   d   e   f   g   h   i

i   a   b   c   d   e   f   g   h

'''


'''
# 구슬 탈출 13460

오른쪽, 아래, 왼쪽, 위 네 방향에 대한 처리가 복잡하게 나온다면

1. 아래로 이동하는 것만 구현
2. 맵 전체를 회전


맵을 왼쪽으로 회전하고, 아래로 이동하고, 다시 위로 돌리면
그대로 왼쪽으로 간 것임

0   1   2   3
4   5   6   7
8   9   10  11


8   4   0
9   5   1
10  6   2
11  7   3

arr[0][0] <= arr[n - 1][0]


'''

'''
# 구슬

최적화 아이디어

1. 이전 방향이랑 같은 방향, 혹은 반대 방향은 볼 필요 없다
2. check에서 not r and b만 봤는데, not r or not b도 봐줘야 함
3. 방문처리하면서 BFS // 이거 해주면 시간 무조건 빨라짐

'''