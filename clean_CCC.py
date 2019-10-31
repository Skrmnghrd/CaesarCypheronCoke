from sys import exit
class CCC:
  def __init__(self, **kwargs):
    try:
      self.inputfile = kwargs['inputfile'] #str
      self.outputfile = kwargs['outputfile'] #str
      self.shift = kwargs['shift'] #int
    except Exception as e:
      print(e)
      print('Parameters: inputfile(str), outputfile(str), on_cocaine(bool), salt(str), shift(int)')
      exit()

  def cypher(self):
    file_output = open(self.outputfile,'wb+')
    with open(self.inputfile,'rb+' ) as f: 
      for line in f: 
        data = (list(line.decode('utf-8').rstrip()))
        orig_ascii_data = [x for x in data]   
        shifted_ascii_data = [self.ascii_data_shifter(x, self.shift) for x in orig_ascii_data]
        shifted_string_data = ''.join([self.converter(x, ascii_to_str=True) for x in shifted_ascii_data])
        file_output.write(shifted_string_data.encode('utf-8', 'surrogateescape') + '\n'.encode('utf-8', 'surrogateescape')) 

  def shifter(self, list_data):
    
    try:
      list_data = [self.converter(x, char_to_ascii=True) for x in list_data]
      list_data = [self.ascii_data_shifter(x, 3) for x in list_data]
    except:
      list_data = [self.converter(x, char_to_ascii=False) for x in list_data]
      list_data = [self.ascii_data_shifter(x, 3) for x in list_data]
    
    return list_data

  def ascii_data_shifter(self, ascii_val, shift): 

    try:
      ascii_val = ord(ascii_val)
    except:
      pass

    if (ascii_val + shift) > 1114111: 
      return (ascii_val + shift) - 1114111 
    if (ascii_val + shift) < 0: 
      return (ascii_val + shift) + 1114111 
    return (ascii_val + shift) 

  def converter(self, char, char_to_ascii=False, ascii_to_str=False):

    def __str_to_ascii__(char):
      try:
        return(ord(char))
      except Exception as e:
        print(e)
        exit()

    def __ascii_to_str__(char):
      try:
        return(chr(char))
      except Exception as e:
        print(e)
        exit()

    if char_to_ascii == False and ascii_to_str == False or char_to_ascii==True and ascii_to_str == True:
      print('One choice must be true and one must be false: char_to_ascii or ascii_to_str')
      exit()

    if char_to_ascii == True:
      return(__str_to_ascii__(char))

    if ascii_to_str == True:
      return(__ascii_to_str__(char))

if __name__ == "__main__":
    CypherObject = CCC( inputfile='inputtextfile.txt', outputfile='outputtextfile', shift=-500 )
    CypherObject.cypher()