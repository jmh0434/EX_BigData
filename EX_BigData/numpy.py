import numpy as np

# 난수를 초기화
np.random.seed(0)

# 가로세로 크기를 전달하면 해당 크기의 이미지를 난수로 채워서 생성하는 함수
def make_image(m, n):
    image = np.random.randint(0,6,(m,n))
    return image

# 전달된 행렬의 일부를 변경하는 함수
def change_little(matrix):
    # 전달받은 행렬의 형태(크기)를 취득하여 shape에 대입
    shape = matrix.shape

    # 행렬의 각 성분에 대해 변경 여부를 무작위로 결정한 다음
    # 변경할 때는 0~5 사이의 정수로 임의 교체
    for i in range(shape[0]):
        for j in range(shape[1]):
            if np.random.randint(0, 2) == 1:
                matrix[i][j] = np.random.randint(0, 6, 1)
    return matrix

# 임의의 이미지 생성
image1 = make_image(3, 3)
print(image1)
print()

# 임의의 변경사항 적용
image2 = change_little(np.copy(image1))
print(image2)
print()

# image1과 image2의 차이를 계산하여 image3에 대입
image3 = image2 - image1
print(image3)
print()

# image3의 각 성분을 절댓값으로 한 행렬을 image3에 다시 대입
image3 = np.abs(image3)

print(image3)