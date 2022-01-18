# list sort


'''
< 1. list 본체 정렬 >
reverse : 리스트 거꾸로 뒤집기, desc 정렬 x

>>> a = [1, 10, 5, 7, 6]
>>> a.reverse()
>>> a
[6, 7, 5, 10, 1]



< 2. sort >
기본값 오름차순, reverse = True는 내림차순

>>> a = [1, 10, 5, 7, 6]
>>> a.sort()
>>> a
[1, 5, 6, 7, 10]

>>> a = [1, 10, 5, 7, 6]
>>> a.sort(reverse=True)
>>> a
[10, 7, 6, 5, 1]



< 3. sort의 key 옵션 >
>>> m = '나는 파이썬을 잘하고 싶다'
>>> m = m.split() # 공백 기준
>>> m
['나는', '파이썬을', '잘하고', '싶다']

>>> m.sort(key=len) # 길이 기준
>>> m
['나는', '싶다', '잘하고', '파이썬을']



< 4. list 정렬된 결과 반환 >
정렬된 결과 반환하는 함수 : 본체 변형 x !!
sorted : 순서대로 정렬, 정렬된 리스트 반환

>>> x = [1 ,11, 2, 3]
>>> y = sorted(x)
>>> x
[1, 11, 2, 3]

>>> y
[1, 2, 3, 11] # 따로 변수 생성해서 지정해줘야 함 !!



< 5. reversed >
거꾸로 뒤집기, iterable한 객체 반환
확인 위해 list로 한 번 더 변형 필요!

>>> x = [1 ,11, 2, 3]
>>> y = reversed(x)
>>> x
[1, 11, 2, 3]

>>> y
<list_reverseiterator object at 0x1060c9fd0> # iterable한 객체 반환
>>> list(y) # 리스트로 다시 만들어주기
[3, 2, 11, 1]



--> 이렇게 줄여서 쓰는 것 가능함 <--
x = [1, 11, 2, 3]
y = list(reversed(x))
print(y)



< 6. 정렬 순서 주의 >
상위조건(A)과 하위조건(B)가 있을 때 B -> A 해야 함

정렬 조건
1. 길이가 짧은 것부터 (A)
2. 길이 같으면 사전순 (B)

사전순(B) -> 길이 짧은 것(A) 순으로 sort 사용

'''