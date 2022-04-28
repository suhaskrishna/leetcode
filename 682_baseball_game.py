class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        li = 0
        
        for op in ops:
            if op.lstrip("-").isnumeric():
                if li == len(res):    
                    res.append(int(op))
                else:
                    res[li] = int(op)
                li += 1
            elif op == "+":
                if li == len(res):    
                    res.append(res[li-1] + res[li-2])
                else:
                    res[li] = res[li-1] + res[li-2]
                li += 1
            elif op == "D":
                if li == len(res):    
                    res.append(res[li-1]*2)
                else:
                    res[li] = res[li-1]*2
                li += 1
            else:
                res[li-1] = 0
                li -= 1
        
        return sum(res)

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        
        for op in ops:
            if op == "C":
                res.pop()
            elif op == "D":
                res.append(res[-1]*2)
            elif op == "+":
                res.append(res[-1] + res[-2])
            else:
                res.append(int(op))
        
        return sum(res)