# Made by Lord-Giganticus
class error:
  def problem(x:int, y:int, z:str):
    if y == 0:
      print("There was a input error on line",str(x),' of file',str(z)+'.')
    elif y != 0 and y > 0:
      print('There was a error somewhere between line',str(x),'and line',str(y),' of file',str(z)+'.')
    elif y != 0 and y < 0:
      print('y is less than 0! It is set to',str(y),'the starting line is line',str(x),' of file',str(z)+'. Please inform the author that this has occured!')
    input('Press enter to exit.')
    exit()