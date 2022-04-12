class StringUtility:
  
  def __init__(self, string):
    """initializes the variable string, takes string as an arguemnt"""
    self.string = string
    
  def __str__(self):
    """ idk """
    return self.string
  def vowels(self):
    """counts how many vowels in string, but returns many if its greater than 5 """
    vow = ["a", "e", "i", "o", "u"]
    count = 0
    for letter in self.string:
      if letter in vow:
        count+=1
    if count < 5:
        return str(count)
    else:
        return "many"
  def bothEnds(self):
    """only returns first+last 2 characters in string if the length is greater than 2 characters"""
    if len(self.string) <= 2:
      return ""
    return self.string[:2] + self.string[-2:]
    
  def fixStart(self):  
    """replaces any letter in string that matches the first letter with star. does not replace first letter. if string is not greater than 1 character, returns original string"""
    expected = ""
    if len(self.string) <= 1:
      return self.string
    first_let=self.string[0]
    expected += first_let
    
    for char in self.string[1:]:
      if char == first_let:
        expected += '*'
      else:
        expected += char
        #expected += self.string[char]
        #expected = expected + self.string[char]
    return expected
    #change expected to word
         
  def asciiSum(self):
    """adds ascii sums of each character in string"""
    expected = 0
    for i in self.string:
      expected += int(ord(i))
    return expected
  def cipher(self):
    """shifts each character in string by the number of characters in string. repeats alphabet if shifted outside of alphabetical ascii values"""
    expected ="" 
    for i in self.string:
      if i == ' ':
        y = ord(i)
      if i.islower():
        y = ord(i) + len(self.string)
        while y > ord('z'):
          y -= 26
      elif i.isupper():
        y = ord(i) + len(self.string)
        while y > ord('Z'):
          y -= 26

      
      expected += chr(y)

      #print(len(self.string))
    
    return expected
  
    