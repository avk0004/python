class Problems:
    def __init__(self,target,Nums):
        self.N = Nums
        self.t = target

    def TwoSum(self):
        D = 0
        Li = {}
        for i,num in enumerate (self.N):
            D = self.t - num
            if D in Li:
                return[Li[D],i]
            Li[num] =i
                
if __name__ == "__main__":
    
    Nums = [5,10,15,30]
    t = 45
    X= Problems(t,Nums)
    Dummy = X.TwoSum()
    print(Dummy)
        

