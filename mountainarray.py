class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        result = False
        if len(arr) >= 3 and len(arr) <= 10**4:
            for x in range (0, len(arr) - 1):
                if arr[x+1] > arr[x]:
                    result = True
                else: 
                    break
            if result: 
                for index in range(x, len(arr)-1):
                    if arr[index+1] < arr[index]:
                        result = True
                    else:
                        result = False
                        break
                        
        return result
                