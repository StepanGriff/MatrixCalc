class MatrixMath:
    a=[[]]
    b=[[]]
    def __init__ (self, x:list[list[int]], y:list[list[int]]):
        self.a = x
        self.b = y

    def add(self):
        assert (len(self.a) == len(self.b) and len(self.a[0]) == len(self.b[0])), "Matrices are not the same size"
        res = [[]]
        it = 0        
        for num, num2 in zip(self.a, self.b):
            for val, val2 in zip(num, num2):
                sum = val + val2
                res[it].append(sum)
            it+= 1
            if it < len(self.a):
                res.append([])
        return(res)
    
    def subtract(self):
        assert (len(self.a) == len(self.b) and len(self.a[0]) == len(self.b[0])), "Matrices are not the same size"
        res = [[]]
        it = 0        
        for num, num2 in zip(self.a, self.b):
            for val, val2 in zip(num, num2):
                sum = val - val2
                res[it].append(sum)
            it+= 1
            if it < len(self.a):
                res.append([])
        return(res)

    def multiplication(self):
        assert len(self.a) == len(self.b[0]), "Matrices are not the proper size"
        res = [[0 for x in range(len(self.a))] for y in range(len(self.b[0]))]
        it = 0
        for i in range(len(self.a)):
            for j in range(len(self.b[0])):
                for k in range(len(self.b)):
                    res[i][j] += self.a[i][k] * self.b[k][j]
        return(res)
    
    def determinant(self, x):
        assert len(x) == len(x[0]), "Matrix is not square"
        det=0
        alt = 1
        if len(x) == 2:
            det = (x[0][0]*x[1][1] - x[1][0]*x[0][1])
            return (det)
        else:
            for num in range(len(x)):
                if num % 2 == 0:
                    alt = 1
                else:
                    alt = -1 
                det += (alt*x[0][num])*self.determinant(self.shrinkMatrix(x, 0, num))
            return (det)

    def shrinkMatrix(self, x, y:int , z:int):
        clone = self.cloneMatrix(x)
        clone.remove
        clone.pop(y)
        for num in range(len(clone)):
            clone[num].pop(z)
        return clone
    
    def matrixOfMinors(self, x):
        assert len(x) == len(x[0]), "Matrix is not square"
        mom = [[0 for val in range(len(x))] for val2 in range(len(x))]
        for num in range(len(x)):
            for num2 in range(len(x)):
                mom [num][num2] = self.determinant(self.shrinkMatrix(x,num,num2))
        return mom

    def matrixOfCofactors(self, x):
        moc = [[0 for val in range(len(x))] for val2 in range(len(x))]
        for num in range(len(x)):
            for num2 in range(len(x)):
                moc [num][num2] = x[num][num2]*((-1)**(num+num2))
        return moc
    
    def transposeMatrix(self, x):
        tm = [[0 for val in range(len(x[0]))] for val2 in range(len(x))]
        for num in range(len(x)):
            for num2 in range(len(x)):
                tm [num][num2] = x[num2][num]
        return tm

    def cloneMatrix(self, x):
        clone= [[0 for val in range(len(x))] for val2 in range(len(x))]
        for num in range(len(x)):
            for num2 in range(len(x[0])):
                clone[num][num2] = x[num][num2]
        return clone

    def division(self):
        self.b = self.invert(self.b)
        return(self.multiplication())

    def invert(self, y: list[list[int]]): 
        assert (len(y) == len(y[0])), "Matrices are not the same size"
        ind = [[0 for x in range(len(self.a))] for y in range(len(self.b[0]))]
        inv = [[0 for x in range(len(self.a))] for y in range(len(self.b[0]))]
        it=0
        for it in range(len(y)):
            ind[it][it] = 1
            it+=1
        return(inv)

    def scalarMultiplication(self):
        return x
    
    
            

x = MatrixMath([[1,2],[3,4]],[[5,6],[7,8]])
#print (x.add())
#print (x.subtract())
#print (x.multiplication())
#print (x.division())
z = [[1,2,3], [5,6,7],[9,10,11]]
print(x.transposeMatrix(z))
#print(x.matrixOfMinors(z,1))