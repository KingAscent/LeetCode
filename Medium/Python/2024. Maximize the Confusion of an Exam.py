class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        fs = 0
        ts = 0
        ansKey = 0
        start = 0
        end = 0

        while end < len(answerKey):
            if answerKey[end] == 'F':
                fs += 1
            else:
                ts += 1
            while k < min(fs, ts):
                if answerKey[start] == 'F':
                    fs -= 1
                else:
                    ts -= 1
                start += 1
            ansKey = max(ansKey, fs + ts)
            end += 1

        return ansKey
