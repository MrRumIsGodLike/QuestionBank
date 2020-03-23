class Solution:
    def compressString(self, S: str) -> str:
        # 出现1次长度加1 出现2次长度不变 出现2次以上长度减少
        S += '-'
        cnt,res = 1,""
        for i in range(1,len(S)):
            if S[i] == S[i-1]:
                cnt += 1
            else:
                res += (S[i-1] + str(cnt))
                cnt = 1
        return S[:-1] if len(res) >= len(S) - 1 else res
