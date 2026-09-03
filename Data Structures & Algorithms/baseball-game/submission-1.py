class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record =[]
        j=-1
        sum =0
        for i,op in enumerate(operations):
            
            if op == "C":
                sum-= record[-1]
                record.pop()
                j-=1
            elif op == "+":
                val = record[j-1] + record[j]
                record.append(val)
                j+=1
                sum+= val
            elif op == "D":
                val = record[j] * 2
                record.append(val)
                j+=1
                sum+=val
            
            else:
                record.append(int(op))
                j+=1
                sum +=int(op)
        return sum

        