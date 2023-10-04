class Solution(object):
    def licenseKeyFormatting(self, s, k):
        license = ""

        for i in range(len(s) - 1, -1, -1):
            if s[i] != '-':
                if len(license) % (k + 1) == k:
                    license += '-'
                license += s[i]

        return license[::-1].upper()
