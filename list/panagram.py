class Solution:
  def checkIfPangram(self, sentence):
    panagram = False
    for i in range(ord('a'), ord('z')+1):
      if not chr(i) in sentence.lower():
        return False
    return True

s = Solution()
s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")