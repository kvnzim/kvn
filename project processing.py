def upside_down(im):
    n,m = im.dim()
    im2 = Matrix(n,m)
    for i in range(n):
        for j in range(m):
            im2[n-i-1,j] = im[i,j]
    return im2

# Rest of the question

## Code from the lectures of items, local_operator - DO NOT CHANGE ##

def items(mat):
    '''flatten mat elements into a list'''
    n,m = mat.dim()
    lst = [mat[i,j] for i in range(n) for j in range(m)]
    return lst

def local_operator(A, op, k=1):
  n,m = A.dim()
  res = A.copy()  # brand new copy of A
  for i in range(k,n-k):
    for j in range(k,m-k):
      res[i,j] = op(items(A[i-k:i+k+1,j-k:j+k+1]))
  return res

## end of code from lectures


def segment(im, thrd):
    ''' Binary segmentation of image im by threshold thrd '''
    n,m = im.dim()
    im2 = Matrix(n,m)
    for i in range(n):
        for j in range(m):
            if im[i,j] < thrd:
                im2[i,j] = 0
            else:
                im2[i,j] = 255
    return im2

def dilate(im, k=1):
    return local_operator(im, max, k)


def edges(im, k, thr):
    n,m = im.dim()
    im2 = im.copy()
    im2 = segment(im2, thr)
    dilated_im2 = dilate(im2, k)
    return dila

 #Question 5
    m1 = Matrix(4,4,0)
    m1[0,0] = 20
    m1[1,0] = 60
    m2 = segment(m1,10)
    if m2.rows != [[255, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]:
        print("error in segment()")
    m3 = dilate(m2,1)
    if m3.rows != [[255, 0, 0, 0], [255, 255, 0, 0], [0, 255, 0, 0], [0, 0, 0, 0]]:
        print("error in dilate()")
    m4 = m3 - m2
    if edges(m1,1,10) != m4:
        print("error in edges()")ted_im2 - im2
