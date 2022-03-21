# 赎金信
# 思路：将两个字符串进行遍历，然后统计每个字符出现的次数。形成两个字典，key是字符，value是出现的次数。
# 记第一个字符串的字典为r_dic，第二个字符串的字典为m_dic。
# 遍历r_dic，要每一个key都在m_dic中，且value要小于等于m_dic的value。
# 如果有一个不满足，则返回False。
# 如果遍历完了，返回True。

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_dic = {}
        m_dic = {}
        # 统计ransomNote中每个字符出现的次数,存入字典r_dic
        for i in ransomNote:
            if i in r_dic:
                r_dic[i] += 1
            else:
                r_dic[i] = 1
        # 统计magazine中每个字符出现的次数,存入字典m_dic
        for i in magazine:
            if i in m_dic:
                m_dic[i] += 1
            else:
                m_dic[i] = 1
        # 遍历r_dic，要每一个key都在m_dic中，且value要小于等于m_dic的value。
        for key in r_dic:
            if key not in m_dic or r_dic[key] > m_dic[key]:
                return False
        return True