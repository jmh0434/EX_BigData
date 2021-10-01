# 필요한 라이브러리를 import
import numpy as np
import time
from numpy.random import rand

# 행, 열의 크기
N = 150

# 행렬을 초기화
matA = np.array(rand(N, N))
matB = np.array(rand(N, N))
matC = np.array([[0] * N for _ in range(N)])

# 파이썬의 리스트를 사용하여 계산
# 시작 시간을 저장
start = time.time()

# for 문을 사용하여 행렬 곱셈 실행
for i in range(N):
    for j in range(N):
        for k in range(N):
            matC[i][j] = matA[i][k] * matB[k][j]

print("파이썬 기능만으로 계산한 결과: %.2f[sec]" % float(time.time() - start))

# Numpy를 사용하여 계산
# 시작 시간 저장
start = time.time()

# Numpy를 사용하여 행렬 곱셈 실행
matC = np.dot(matA, matB)

# 소수점 이하 두 자리까지 표시되므로 Numpy는 0.00[sec]으로 표시
print("NumPy를 사용하여 계산한 결과: %.2f[sec]" % float(time.time() - start))