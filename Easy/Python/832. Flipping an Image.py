class Solution(object):
    def flipAndInvertImage(self, image):
        for col in image:
            i = 0
            j = len(image) - 1

            while i <= j:
                temp = col[i]
                col[i] = 1 - col[j]
                col[j] = 1 - temp
                i += 1
                j -= 1
        
        return image
