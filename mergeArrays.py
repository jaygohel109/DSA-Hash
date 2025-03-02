lass Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        num1={}
        for i ,n in enumerate(nums1):
            num1[n[0]]=n[1]
        for i ,n in enumerate(nums2):
            if n[0] in num1:
                num1[n[0]]+=n[1]
            else:
                num1[n[0]]=n[1]
        result = sorted([[k, v] for k, v in num1.items()])
        return result
