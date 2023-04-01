class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        
        prefix = ''
        for i, wrd in enumerate(strs[0]):
            for sub in strs[1:]:
                if i >= len(sub) or wrd != sub[i]:
                    return prefix
            prefix += wrd
        
        return prefix
