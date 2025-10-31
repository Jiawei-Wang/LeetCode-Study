class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        
        answer = 0

        for i in range(len(boxTypes)):
            if truckSize > 0:
                take = min(truckSize, boxTypes[i][0])
                answer += take * boxTypes[i][1]
                truckSize -= take
            else:
                break
        
        return answer
