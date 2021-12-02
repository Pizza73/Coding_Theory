import numpy as np

def hamming_encode(i):
    G=np.matrix([[1,0,0,0,0,1,1],\
                [0,1,0,0,1,0,1],\
                [0,0,1,0,1,1,0],\
                [0,0,0,1,1,1,1]])

    return np.dot(i, G) % 2

def hamming_decode(j, num):
    print(j)
    if num == 7:
        pass
    else:
        e = np.array([0,0,0,0,0,0,0])
        e[num] = 1
        j = (j + e) % 2
    print(j)
    """
    H=np.matrix([[0,1,1,1,1,0,0],\
                [1,0,1,1,0,1,0],\
                [1,1,0,1,0,0,1]])
    """
    H=np.matrix([[0,0,0,1,1,1,1],\
                [0,1,1,0,0,1,1],\
                [1,0,1,0,1,0,1]])

    return np.dot(j, H.T) % 2


def main():
    G=np.matrix([[1,0,0,0,0,1,1],\
                [0,1,0,0,1,0,1],\
                [0,0,1,0,1,1,0],\
                [0,0,0,1,1,1,1]])

    H=np.matrix([[0,0,0,1,1,1,1],\
                [0,1,1,0,0,1,1],\
                [1,0,1,0,1,0,1]])

    print(np.dot(G, H.T) % 2)
    i = np.array([1,0,0,1])
    encode = hamming_encode(i)
    for i in range(8):
        decode = hamming_decode(encode, i)
        print(decode)
    
if __name__ == '__main__':
    main()
