import time, random

def prefixSum1(X, n):
	# code for prefixSum1
	A = [0]*n
	for i in range(n):
		for j in range(i+1):
			A[i]=A[i]+X[j]


		
	
	
def prefixSum2(X, n):
	# code for prefixSum2
	A = [0]*n
	A[0] = X[0]
	for i  in range(1,n):
		A[i] = A[i-1]+X[i]


	
random.seed()		# random 함수 초기화
n = int(input())
X=[]				# n 입력받음
for i in range(0,n):
	X.append(random.randint(-999,999))
	print(X[i])
# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
before = time.clock()
prefixSum1(X,n)# prefixSum1 호출
after = time.clock()
result1 = after-before

before = time.clock()
prefixSum2(X,n)# prefixSum2 호출
after = time.clock()
result2 = after-before

print(result1,result2)# 두 함수의 수행시간 출력