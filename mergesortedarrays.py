class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        main=m-1
        second=n-1
        last=m+n-1

        while second >=0:
            if main>=0 and nums1[main]>nums2[second]:
                nums1[last]=nums1[main]
                main-=1
            else:
                nums1[last]=nums2[second]
                second-=1
            last-=1
        


        
