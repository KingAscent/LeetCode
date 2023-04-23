class Solution(object):
    def decode(self, encoded, first):
        original = [first]

        for i in range(len(encoded)):
            original.append(original[i] ^ encoded[i])

        return original
