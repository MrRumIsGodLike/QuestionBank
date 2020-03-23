class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        # 1.暴力
        # res = list(S)
        # for p in range(length):
        #     if res[p] == ' ':
        #         res[p] = '%20'
        # return ''.join(res[:length])
        # 2.精简
        # return '%20'.join(S[:length].split(' '))
        # 3.极精简
        return S[:length].replace(' ','%20')