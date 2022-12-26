class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        levelStart = 1
        while(levelStart*2 <= label):
            levelStart = levelStart*2
        while(label != 1):
            temp = levelStart+(((levelStart*2)-1)-label)
            label = math.floor(temp/2)
            levelStart = levelStart/2
            ans.append(label)
        return ans[::-1]
