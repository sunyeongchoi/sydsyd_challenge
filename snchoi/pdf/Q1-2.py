# 2차원 사진  배열을 좌우 반전 시킨다.
def reversalPhoto(photoAry, height, width): # 2차원 사진 배열, 사진 배열의 행 개수, 사진 배열의 열 개수
    retAry = [] # 좌우 반전된 2차원 사진 배열
    ###########   여기부터 코딩 (1) ---------------->




    ###########   <-------------- 여기까지 코딩 (1)
    return retAry


# 2차원 사진  배열을 2배 확대 시킨다.
def zoomScale(photoAry, height, width): #2차원 사진 배열, 사진 배열의 행 개수, 사진 배열의 열 개수
    retAry = [] # 2배 확대된 2차원 사진 배열
    ###########   여기부터 코딩 (2) ---------------->




    ###########   <-------------- 여기까지 코딩 (2)

    return retAry

# 2차원 사진 배열을 왼쪽으로 90도 회전시킨다.
def rotatePhoto(photoAry, height, width): # 2차원 사진 배열, 사진 배열의 행 개수, 사진 배열의 열 개수
    retAry = [] # 왼쪽으로 90도 회전된 2차원 사진 배열
    ###########   여기부터 코딩 (3) ---------------->




    ###########   <-------------- 여기까지 코딩 (3)

    return retAry


# 2차원 사진 배열에 테두리를 추가한다.
def drawEdge(photoAry, height, width): # 2차원 사진 배열, 사진 배열의 행 개수, 사진 배열의 열 개수
    retAry = [] # 테두리가 추가된 2차원 사진 배열
    ###########   여기부터 코딩 (4) ---------------->




    ###########   <-------------- 여기까지 코딩 (4)

    return retAry


## 전역 변수 선언 부분
inputPhotoAry =[] # 입력 배열(2차원) 
outputPhotoAry = [] # 출력 배열(2차원)
rowNum, colNum=0, 0 # 배열의 크기. 

def main() :
        global inputPhotoAry, outputPhotoAry, rowNum, colNum

        loadData() # 2차원 이미지 읽어오기

        ## 원본 출력
        print(' ----- (0) 원본 사진 -----')
        printData(inputPhotoAry, rowNum, colNum)
        
        ## 좌우 반전
        outputPhotoAry = reversalPhoto(inputPhotoAry, rowNum, colNum)
        print(' ----- (1) 좌우 반전된 사진 -----')
        printData(outputPhotoAry, rowNum, colNum)
        inputPhotoAry = outputPhotoAry[:] #  출력배열 --> 입력 배열
        
        ## 2배 확대
        outputPhotoAry = zoomScale(inputPhotoAry, rowNum, colNum)
        print(' ----- (2) 2배 확대된 사진 -----')
        rowNum *= 2; # 행 2배 
        colNum *= 2;  # 열 2배
        printData(outputPhotoAry, rowNum, colNum)
        inputPhotoAry = outputPhotoAry[:] #  출력배열 --> 입력 배열

        ## 왼쪽 90도 회전
        outputPhotoAry = rotatePhoto(inputPhotoAry, rowNum, colNum)
        print(' ----- (3) 90도 회전된 사진 -----')
        rowNum, colNum = colNum, rowNum # 행, 열을 교체
        printData(outputPhotoAry, rowNum, colNum)
        inputPhotoAry = outputPhotoAry[:] #  출력배열 --> 입력 배열
        
        ## 테두리가 추가된 사진.
        outputPhotoAry = drawEdge(inputPhotoAry, rowNum, colNum)
        print(' ----- (4) 테두리가 추가된 사진 -----')
        printData(outputPhotoAry, rowNum+2, colNum+2)
        
## 함수 선언 부분
def  loadData() : # 데이터 불러오기
    global inputPhotoAry, outputPhotoAry, rowNum, colNum

    ###########
    # 제공 데이터 세트 1 
    # 4x2 사진 데이터. 
    ###########
    rowNum , colNum = 4, 2 # 행 및 열의 개수
    inputPhotoAry = \
    [
        ['C', 'D' ],
        ['K', 'P' ],
        ['A', 'R' ],
        ['P', 'Q' ]
    ]


def printData(photo, x, y) :
    global inputPhotoAry, outputPhotoAry, rowNum, colNum
    
    for i in range(0, x) :
        for k in range(0, y) :
                try :
                        print("%c " % photo[i][k], end='')
                except :
                        pass
        print()
    print()

## 메인 함수 호출 ##
if __name__ == "__main__" :
    main()

