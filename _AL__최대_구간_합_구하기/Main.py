import sys
MIN = -sys.maxsize-1
def max_sum(A, left, right):
	# A[left], ..., A[right-1] 중 최대 구간 합 리턴
	if left == right:
		return A[left]
	mid = (left+right)//2
	le = max_sum(A,left,mid)
	ri  = max_sum(A,mid+1,right)
	
	tmp = 0
	left_part=MIN
	for i in range(mid,left-1,-1):
		tmp +=A[i]
		left_part = max(left_part,tmp)
	
	tmp = 0
	right_part=MIN
	for i in range(mid+1,right+1):
		tmp +=A[i]
		right_part = max(right_part,tmp)
	
	return max(le,ri,left_part+right_part)
		
A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)