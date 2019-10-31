rea = 'awdawdwadwad:\x41:\x52:w123:13123123;12salt3123'
b = [x for x  in range(32)]
from sys import exit
import unicodedata
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
      self.inputfile = kwargs['inputfile']
      self.outputfile = kwargs['outputfile'] #str
      self.on_cocaine = kwargs['on_cocaine'] #bool
      self.salt = kwargs['salt'] #strings
      self.shift = kwargs['shift'] #int
      self.decrypt = kwargs['decrypt'] #bool
      self.params = kwargs #assign an attribute again just for the heck of it
    #lazy method to pass on a dict
    except Exception as e:
      print(e)
      print('Parameters: inputfile(str), outputfile(str), on_cocaine(bool), salt(str), shift(int)')
      exit()
  #a = CCC(inputfile='testinput.txt', outputfile='awd', on_cocaine=False, salt='awdawd', shift=1)
  #CLASS PRIVATE FUNCTIONS :>

  def __test_read_from_input__(self):
    print('='*32)
    with open('awd.txt', 'rb+') as f:
      for line in f:
        data = (list(line.decode('utf-8').rstrip()))
        ascii_to_data = [ord(x) for x in data]
        #print(ascii_to_data)
    """
    f = open('awd.txt', 'rb+')
    print( f.read().decode('utf-8'))
    f.close()
    """
  def cypher(self):
    file_output = open(self.outputfile,'wb+')
    with open(self.inputfile,'rb+' ) as f: 
      for line in f: 
        #data = list( line.rstrip() )
        data = (list(line.decode('utf-8').rstrip()))
        
        orig_ascii_data = [x for x in data] 
        pass  
        shifted_ascii_data = [self.ascii_data_shifter(x, self.shift) for x in orig_ascii_data]
        shifted_string_data = ''.join([self.converter(x, ascii_to_str=True) for x in shifted_ascii_data])
        #print(data, end="") #separate to be safe when writing bytes
        #print(' ===> ', end='')
        #print(list(shifted_string_data))
        file_output.write(shifted_string_data.encode('utf-8') + '\n'.encode('utf-8')) 
        #do not use format since it makes everything into string and it won't work well for you
        #file_output.write("{}\n".format(shifted_string_data.encode()))

  def shifter(self, list_data):
    """
    This is a risky process but it'll work
    """
    try:
      list_data = [self.converter(x, char_to_ascii=True) for x in list_data]
      list_data = [self.ascii_data_shifter(x, 3) for x in list_data]
    except: #if it's ascii, then put it back to str
      list_data = [self.converter(x, char_to_ascii=False) for x in list_data]
      list_data = [self.ascii_data_shifter(x, 3) for x in list_data]
    

    return list_data


  def ascii_data_shifter(self, ascii_val, shift): #unused
    #put a limit 1114111 
    """
    if (ascii_val + shift) > 1114111:
      ascii_val = (ascii_val + shift ) - 1114111
    """
    #reading from bytes so you don't need to use ord('letter')
    #but if it's unicode, it sees it as bytes

    try:
      ascii_val = ord(ascii_val) #converts to ascii numbers if possible
    except:
      pass

    if (ascii_val + shift) >= 55175 and (ascii_val + shift) <= 57312: 
      #it errors between 55175 and 57312 because of some reason, jsut look it up :> okay?
      print('The outcome ascii val should not be between 55175 or 57312.')
      print('Current ascii_val {}'.format(str(ascii_val + shift)))
      exit()
    if (ascii_val + shift) > 1114111: #mas dako sa limit
      return (ascii_val + shift) - 1114111 #minusan mo ka limit kag ang bilin muna ang result #110 - 100 = 10
    if (ascii_val + shift) < 0: #kung negative
      return (ascii_val + shift) + 1114111 #
    
    return (ascii_val + shift) #if no problem arises, return #uncomfy method

    #( n + shift) + limit
    """try: 
      return (shift + ascii_val)
    except Exception as e: 
      print(e, 'error on ascii_data_shifter')
      return (shift + ord(ascii_val) )"""
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

    if char_to_ascii == False and ascii_to_str == False or char_to_ascii==True and ascii_to_str == True:
      print('One choice must be true and one must be false: char_to_ascii or ascii_to_str')
      exit()

    if char_to_ascii == True:
      return(__str_to_ascii__(char))

    if ascii_to_str == True:
      return(__ascii_to_str__(char))



if __name__ == "__main__":
  #a = CCC(inputfile='awd.txt', outputfile='testTTTT.txt', on_cocaine=False, salt='awdawd', shift=, decrypt=True)
  pass
  #a.__test_read_from_input__()



links_that_helped = """
idk which links helped me solve the program but JFTHOI I'm pasting everything here

https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty

https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters

https://stackoverflow.com/questions/934160/write-to-utf-8-file-in-python

https://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined

https://stackoverflow.com/questions/19591458/python-reading-from-a-file-and-saving-to-utf-8

https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in

https://stackoverflow.com/questions/15746954/what-is-the-difference-between-rb-and-rb-modes-in-file-objects

https://stackoverflow.com/questions/19897209/troubleshooting-typeerror-ord-expected-string-of-length-1-but-int-found

https://stackoverflow.com/questions/4987327/how-do-i-check-if-a-string-is-unicode-or-ascii

https://stackoverflow.com/questions/147741/character-reading-from-file-in-python


https://web.archive.org/web/20090228203858/http://techxplorer.com/2006/07/18/converting-unicode-to-ascii-using-python

https://stackoverflow.com/questions/43939704/transform-ascii-to-unicode?rq=1

https://stackoverflow.com/questions/28583565/str-object-has-no-attribute-decode-python-3-error

https://stackoverflow.com/questions/491921/unicode-utf-8-reading-and-writing-to-files-in-python

https://stackoverflow.com/questions/33054527/typeerror-a-bytes-like-object-is-required-not-str-when-writing-to-a-file-in

https://stackoverflow.com/questions/46259640/cant-concat-bytes-to-str-converting-to-python3/46281174#46281174

https://docs.python.org/3/howto/unicode.html

https://realpython.com/python-encodings-guide/

https://stackoverflow.com/questions/10971033/backporting-python-3-openencoding-utf-8-to-python-2

https://stackoverflow.com/questions/6048085/writing-unicode-text-to-a-text-file

https://stackoverflow.com/questions/12092527/python-write-bytes-to-file
"""