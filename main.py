def checkIfPangram(sentence):
  # TODO: Write your code here
  if len(set(self.sentence.upper())) == 26:
    return True
  return False

if __name__ == '__main__':
  #Solution solution = Solution()
  print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))