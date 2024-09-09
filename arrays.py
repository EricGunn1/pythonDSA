class Arrays:

    @staticmethod
    def mergeSortedArrays(nums1, nums2):
        nums0 = []
        j = 0
        for num in nums1:
            if j < len(nums2):
                while nums2[j] < num:
                    nums0.append(nums2[j])
                    j += 1
                    if j == len(nums2):
                        break

            nums0.append(num)

        if j < len(nums2):
            for num in nums2[j:]:
                nums0.append(num)

        return nums0

    @staticmethod
    def dedupSortedArray(nums):
        k = 1
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                break
            while num == nums[i + 1]:
                del nums[i + 1]
                if i == len(nums) - 1:
                    break
        return nums

    def bubbleSortArray(self):
        pass

    def removeElement(self):
        pass

    def insertElement(self):
        pass