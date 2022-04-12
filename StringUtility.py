class StringUtility:
  
  def __init__(self, string):
    self.string = string
    
  def __str__(self):
    return self.string
  def vowels(self):
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
    if len(self.string) <= 2:
      return ""
    return self.string[:2] + self.string[-2:]
    
  def fixStart(self):  
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
    expected = 0
    for i in self.string:
      expected += int(ord(i))
    return expected
  def cipher(self):
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
  
    