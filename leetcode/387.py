# 字符串中第一个不重复的元素
# 统计当前字符在字符串中出现的次数，如果是1就直接返回即可
# 如果扫描完整个字符串都没有找到，就返-1
# 如果整个字符串都已经扫描完成了，都没有找到没有重复的字符，就返回-1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            if s.count(s[i]) == 1:
                return i
        return -1