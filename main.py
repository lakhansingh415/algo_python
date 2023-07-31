import list.add_triplet_to_zero
import list.balanced_array
import list.contains_duplicate
def checkIfPangram(sentence):
  # TODO: Write your code here
  if len(set(sentence.upper())) == 26:
    return True
  return False

if __name__ == '__main__':
  #Solution solution = Solution()
  print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))