class Solution:
    def mergeTwoLists(self,list1, list2):
        i,j = 0,0
        merge=[]
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merge.append(list1[i])
                i+=1
            else:
                merge.append(list2[j])
                j+=1

        while i < len(list1):
            merge.append(list1[i])
            i+=1
        while j < len(list2):
            merge.append(list2[j])
            j+=1
        return merge
           

solution=Solution()
list1 = [1,3,5]
list2 = [2,4,6]
print(solution.mergeTwoLists(list1,list2))
