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
        matrix =list[list[int]]
        if len(x) ==2:
            det = (x[0][0]*x[1][1] - x[1][0]*x[0][1])
            return (det)
        else:
            for num in range(len(x)):
                if num %2 == 0:
                    alt = 1
                else:
                    alt =-1 
                det += (alt*x[0][num])*det(self.matrixOfMinors(x, num))
            return (det)


    def matrixOfMinors(self, x, y:int):
        minor = list[list[int]]
        x.remove
        x.pop(0)
        for num in range(len(x)):
            x[num].pop(y)
        minor = x
        return minor

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
z = [[0,1,2],[3,4,5],[6,7,8]]
print(x.determinant(z))
#print(x.matrixOfMinors(z,1))