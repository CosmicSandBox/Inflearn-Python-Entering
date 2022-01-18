#chapter05-1
#파이썬 함수 및 중요성
#파이썬 함수식 및 람다(Lambda)

#함수 정의 방법
#def function_name(parameter):
#    code

#예제1
def first_func(w):
    print('Hello,',w)

word = 'Goodboy'

first_func(word)
    
#예제2
def return_func(w1):
    value = 'Hello, ' + str(w1)
    return value

x = return_func('Goodboy2')
print(x)
#내가 원하는 값을 만들고 반환 받아서 이 변수를 호출한 것.

# 예제3(다중반환)

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

###3개를 리턴하기 때문에 받는 쪽도 3개를 받아야 함. 이런 것을 언팩킹이라고 함. 
#3개로 알아서 파이썬이 차곡차곡 풀어서 넣어준다. 

x, y, z = func_mul(10)
print(x, y, z)

#튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3) #이렇게 하나로 묶는걸 패킹이라고 하는 듯. 
                        #이렇게 묶으니 튜플이 됨.

q = func_mul2(20)

print(type(q), q, list(q)) #이렇게 리스트로 캐스팅해서(형변환) 해서 필요한 곳에 사용하면 됨.

#리스트 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func-mul2(30)

print(type(p), p, set(q)) #set은 집합을 의미