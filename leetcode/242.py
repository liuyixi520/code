# 有效的字母异位词
# 思路：用一个字典用来统计字符出现的次数
# 遍历第一个字符串时，这个字符串的字数增加
# 遍历第二个字符串时，这个字符串的字数减少
# 最后遍历这个字典，如果字典中所有的元素值都为0，那么就是异位词
# 否则不是异位词

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        # 统计第一个字符串的字数
        for i in s:
            # d.get(i, 0) 这个是为了防止字典中没有这个键值对，就用0代替
            d[i] = d.get(i, 0) + 1
        # 统计第二个字符串的字数
        for i in t:
            d[i] = d.get(i, 0) - 1
        # 遍历字典，如果字典中所有的元素值都为0，那么就是异位词
        for i in d:
            if d[i] != 0:
                return False
        return True