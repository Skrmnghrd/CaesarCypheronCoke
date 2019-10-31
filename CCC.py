rea = 'awdawdwadwad:\x41:\x52:w123:13123123;12salt3123'
b = [x for x  in range(32)]
from sys import exit
class CCC:
  """
  Caesar Cypher on Cocaine
  A program that could basically apply the caesar cypher
  to any text as long as you're able to type them in the CLI
  for example:
  бяо, тгч 2 счрнэя тн1$ 
  0x52,0x56
  11112312312312
  \\x01\\x01\\x01\\x01\\x01\\x010  
  """

  def __init__(self, **kwargs):
    #let's correct the user input at __init__ if he didn't provide all the requirements
    #tell him what he needs to print out
    try:
      #self.inputfile = kwargs['inputfile'] #str
      self.inputfile = 'testinput.txt'
      self.outputfile = kwargs['outputfile'] #str
      self.on_cocaine = kwargs['on_cocaine'] #bool
      self.salt = kwargs['salt'] #strings
      self.shift = kwargs['shift'] #int
      
      self.params = kwargs #assign an attribute again just for the heck of it
    #lazy method to pass on a dict
    except Exception as e:
      print(e)
      print('Parameters: inputfile(str), outputfile(str), on_cocaine(bool), salt(str), shift(int)')
      exit()
  #a = CCC(inputfile='testinput.txt', outputfile='awd', on_cocaine=False, salt='awdawd', shift=1)
  #CLASS PRIVATE FUNCTIONS :>

  def cypher(self):
    #file_output = open(self.outputfile,'a+')
    file_output = open(self.outputfile,'w+')


    with open(self.inputfile) as f:
      #https://stackoverflow.com/questions/6475328/how-can-i-read-large-text-files-in-python-line-by-line-without-loading-it-into
      
      for line in f: #5gb worth of text file? no problem
        #f returns <_io.TextIOWrapper name='testinput.txt' mode='r' encoding='UTF-8'> so you read it
        #https://stackoverflow.com/questions/43438303/how-to-read-print-the-io-textiowrapper-data
        data = list( line.rstrip() ) #string => string => [s,t,r,i,n,g]
        print('=================')
        #rstrip kills the new line just to be safe since read already don't mind \ n
        orig_ascii_data = [self.converter(x, char_to_ascii=True) for x in data]
        shifted_ascii_data = [self.ascii_data_shifter(x, 4) for x in orig_ascii_data]
        shifted_string_data = ''.join([self.converter(x, ascii_to_str=True) for x in shifted_ascii_data])

        print(shifted_ascii_data)
        file_output.write("{}\n".format(shifted_string_data))



        
        
        #[x.rstrip().split() for x in f.readlines()] #taken from assign 3
        #do_smthwith line in f 
      #line = f.readline() #this method is faster for smaller files
      
  def ascii_data_shifter(self, ascii_val, shift):
    #put a limit 1114111 
    """
    if (ascii_val + shift) > 1114111:
      ascii_val = (ascii_val + shift ) - 1114111
    """
    bbb = ascii_val + shift
    return (ascii_val + shift)
    #1114111 MAX NUMBER FOR chr(1114111) anything above resets to zero or below
    #self.shift

  def converter(self, char, char_to_ascii=False, ascii_to_str=False):
    #ghetto private functions :>
    #https://stackoverflow.com/questions/1547145/defining-private-module-functions-in-python
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
      
    """
    One of these values need to be true: 
    char_to_ascii
    ascii_to_str
    would throw an error if false ofcourse
    """
    if char_to_ascii == False and ascii_to_str == False or char_to_ascii==True and ascii_to_str == True:
      print('One choice must be true and one must be false: char_to_ascii or ascii_to_str')
      exit()

    if char_to_ascii == True:
      return(__str_to_ascii__(char))

    if ascii_to_str == True:
      return(__ascii_to_str__(char))



if __name__ == "__main__":
  a = CCC(inputfile='testinput.txt', outputfile='awd', on_cocaine=False, salt='awdawd', shift=1)
  a.cypher()
  print(';')