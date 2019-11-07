def find_median_five(L):
	start = 0
	end = len(L)-1
	
	while(start<end):
		i = start 
		j = end
		mid = L[(i+j)//2]
		
		while i<j:
			if L[i]>mid or L[i]==mid :
				tmp = L[j]
				L[j] =L[i]
				L[i]=tmp
				j=j-1
			else: i=i+1
		if L[i]>mid: i=i-1
			
		if i>len(L)//2 or i==len(L)//2: end = i
		else: start = i+1
	return L[len(L)//2]

def MoM(L, k): # L의 값 중에서 k번째로 작은 수 리턴
	if len(L) == 1: # no more recursion
		return L[0]
	i = 0
	A, B, M, medians = [], [], [], []
	while i < len(L) and i+4 <= len(L):
		medians.append(find_median_five(L[i: i+5]))
		i = i+5
	if i < len(L) and i+4 > len(L):
		medians.append(find_median_five(L[i:len(L)]))
	
	mom = MoM(medians,len(medians)//2)
	for v in L:
		if v < mom: A.append(v)
		elif v > mom: B.append(v)
		else: M.append(v)
	if len(A)>k or len(A)==k: return MoM(A,k)
	elif len(A)+len(M)<k: return MoM(B,k-len(A)-len(M))
	else: return mom

# n과 k를 입력의 첫 줄에서 읽어들인다
#n개의 수에서 k번째 수 찾기
n,k = input().split()
n = int(n)
k = int(k)
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
L = []
L = input().split()
for i in range(n):
	L[i] = int(L[i])
print(MoM(L, k))