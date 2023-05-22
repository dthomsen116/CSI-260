def both_ends():
    s = input("What would you like scrambled?" + '\n')
    slen = len(s)
    sSplit = [*s]
    #print(sSplit)
    if slen <= 2:
        print(s + " should yield " + "''")
    else:
        print (s + " should yield " + sSplit[0] + sSplit[1] + sSplit[-2] + sSplit[-1])
    
  # +++your code here+++
  



import unittest
class TestMethods(unittest.TestCase):

  
  def test_testName2(self):
# Failure message: 
# 'a' should yield ''
    self.assertEqual(both_ends('a'), '')
  def test_testName3(self):
# Failure message: 
# 'xyz' should yield 'xyyz'
    self.assertEqual(both_ends('xyz'), 'xyyz')
  def test_testName(self):
# Failure message: 
# spring should yield spng
    self.assertEqual(both_ends('spring'), 'spng')
  def test_testName1(self):
# Failure message: 
# 'Hello' should yield 'Helo'
    self.assertEqual(both_ends('Hello'), 'Helo')

if __name__ == '__main__':
    unittest.main()

