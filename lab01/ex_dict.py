
d = {
    'foo' : 'foo@naver.com',
    'bar' : 'bar@gmail.com',
    'egg' : 'egg@kakao.com'
}

print(d)

print(d['foo'])

#삭제

del d['foo']
print(d)

#새로운 값 추가
d['foo'] = 'foo@naver.com'
print(d)

#기존값 업데이트
d['foo'] = 'foo@dkt.co.kr'
print(d)

# 사전 안에 리스트도 가능
d['list'] = [1,2,3,4,5]
print(d)

#d.keys() 키값만 리스트로 모아보기. key는 인덱스처럼 쓰인다. 
# 그래서 []사용됨.
print(d.keys())

for key in d.keys():
    print(d[key])

for ky in d:
    print(d[key])

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

# 키 없음을 방지하는 방법
# 'bar' in d.keys():
print(d.get('bar', 'none'))

from collections import defaultdict
dd =defaultdict(int)
print(dd)
#없는 키를 조회하면 int를 가져온다.

dd = defaultdict(list)
print(dd)
print(dd['a']) #'a'를 조회하고 없으면 리스트로 만듦

dd['a'].append('A') #'a'리스트에 A 추가.
print(dd)

