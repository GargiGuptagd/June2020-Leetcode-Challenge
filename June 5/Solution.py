class Solution:

    def __init__(self, w: List[int]):
        self.arr=[]
        count=0
        for i in w:
            count+=i
            self.arr.append(count)
        self.total=count  

    def pickIndex(self) -> int:
        search_num=self.total*random.random()
        low,high=0,len(self.arr)-1
        while low<high:
            mid=(high+low)//2
            if search_num>self.arr[mid]:
                low=mid+1
            else:
                high=mid
        return low