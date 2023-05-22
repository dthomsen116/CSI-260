def remove_adjacent(any_list):
    shortenedlist = []
    
    for x in any_list:
        if x not in shortenedlist:
            shortenedlist.append(x)
    return(shortenedlist)
            




import unittest
class UnitTests(unittest.TestCase):

  def test_removeadjacent3(self):
# Failure message: 
# [] -> []
    self.assertEquals(remove_adjacent([]), [])
  def test_remove_adjacent1(self):
# Failure message: 
# [1, 2, 2, 3] -> [1, 2, 3]
    self.assertEquals(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  def test_removeadjacent2(self):
# Failure message: 
# [2, 2, 3, 3, 3] -> [2, 3]
    self.assertEquals(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])

if __name__ == '__main__':
  unittest.main()
