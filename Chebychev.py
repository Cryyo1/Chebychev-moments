import numpy as np
from math import factorial


## !important:this function to calculate chebychev moment of order p and repetition q are applied to a 2D grayscaled image
## !important:if u want more precise results applying this moments on contour of the shape in the image using canny or .......



'''
 * The function Scaled_Chebyshev return the value of scaled chebychev polynome applied to x
 * @param:
    x:point to calculate on chebychev polynome
    p:ordder of moment
    N:width(height) of the image
 * @returns the value of scaled chebychev polynome applied to x
'''

def Scaled_Chebychev(x,p,N):
    if(p==0):
        return 1
    if (p==1):
        T=(2*x+1-N)/N
        return T
    T=((2*p-1)*Scaled_Chebyshev(x,1,N)*Scaled_Chebyshev(x,p-1,N)-(p-1)*(1-((p-1)**2/N**2))
       *Scaled_Chebyshev(x,p-2,N))/p
    return T

  
'''
 * The function squared_norm return the value of  chebychev polynome of an order
 * @param:
    p:order of moment
    N:width(height) of the image
 * @returns the value of chebychev polynome
'''
def squared_norm(p,N):
    result=N
    for i in range(1,p+1):
        result= result * (1-(i**2/N**2))
    result=result/(2*p+1)
    return result

'''
 * The function chebyshev_moment return the value of chebychev moment with the order p and repetition q
 * @param:
    src:the source image that contains the shape
    p:order of moment
    q:repetition of moment
 * @returns the value of chebychev moment 
'''

def chebyshev_moment(src,p,q):
    if len(src.shape) == 3:
        print('the input image src should be in gray')
        return
    H, W = src.shape
    if H > W:
        src = src[int((H - W) / 2): int((H + W) / 2), :]
    elif H < W:
        src = src[:, int((W - H) / 2): int((H + W) / 2)]

    N = src.shape[0]
    T=0
    for x in range(N):
        for y in range(N):
            if src[x][y]!=0 :
                T=T+Scaled_Chebyshev(x,p,N)*Scaled_Chebyshev(y,q,N)*src[x][y]
        
    return T/(squared_norm(p,N)*squared_norm(q,N))


