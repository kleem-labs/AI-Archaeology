"""A position-wise two-layer feed-forward network."""
def affine(matrix, vector, bias):
    return [sum(w*x for w,x in zip(row,vector))+b for row,b in zip(matrix,bias)]
def relu(vector): return [max(0.0,x) for x in vector]
def ffn(x,w1,b1,w2,b2): return affine(w2,relu(affine(w1,x,b1)),b2)
if __name__ == "__main__":
    x=[1.0,-2.0]
    w1=[[1,1],[1,-1],[-1,0]]; b1=[0,0,0]
    w2=[[1,.5,0],[0,1,1]]; b2=[0,0]
    print("hidden:", relu(affine(w1,x,b1)))
    print("output:", ffn(x,w1,b1,w2,b2))
