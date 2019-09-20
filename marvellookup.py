import os
from sortedcontainers import SortedDict
fileName="/home/class/SoftDev/marvel/"

class CharacterEntry:
#stores information about a character and compiles it
  def __init__(self, line : str):
#take a line of the file and parse it into information fields
    line=line.strip()
    #print(line)
    data=line.split(",")
    #print(data)
    self.pageid=data[0]
    self.char=data[1]
    self.urlslug=data[2]
    self.identify=data[3]
    self.alignment=data[4]
    self.eyecolor=data[5]
    self.hair=data[6]
    self.sex=data[7]
    self.gsm=data[8]
    self.alive=data[9]
    self.appearances=data[10]
    self.first_appear=data[11]
    self.year=data[12]


class TheIndex:
  def __init__(self, fileName : str):
    char_names = open(fileName)
    self.charmap={}
    self.chars=[]
    index=0
    for line in char_names: 
      charData=CharacterEntry(line)
      self.chars.append(charData)
      
      fullname=charData.char
      names=fullname.lower().split(" ")
      for name in names:
#        if name != "(Earth-616)":
#          if (name==user_entry):
#            print(user_entry,names,index)
          if name in self.charmap:
            self.charmap[name].append(index)
          else:
            self.charmap[name]=[index]
          #print(name,self.charmap[name])
      index+=1
    return
  def getResults(self,user_entry): #returns the sorted index of characters that match the entry
    return self.charmap.get(user_entry) 

        
def main():
  full_charmap=TheIndex(fileName)
  run_prgrm = "yes"
  while run_prgrm != "no":
    user_entry=str(input("Please enter the name of a character to search the database: "))
    print("YOU ENTERED: ",user_entry)
    l=full_charmap.getResults(user_entry)
    print("The name",user_entry, "is found on the following lines: ",l)
    for e in l:
      print(e, full_charmap.chars[e].char)
    pick_char=int(input("Enter the line of the character whose data you wish to view: "))
    print("YOU ENTERED: ", pick_char)
    for i in l:
      if i == pick_char:
        print("Character ID and Name: ")
        print(i,full_charmap.chars[e].char)
        print("\n")
        print("Character URL: ")
        print(full_charmap.chars[e].urlslug)
        print("\n")
        print("Character identity: ")
        print(full_charmap.chars[e].identify)
        print("\n")
        print("Character alignment: ")        
        print(full_charmap.chars[e].alignment)
        print("\n")
        print("Character eye color: ")       
        print(full_charmap.chars[e].eyecolor)
        print("\n")
        print("Character hair color: ")
        print(full_charmap.chars[e].hair)
        print("\n")
        print("Character sex: ")
        print(full_charmap.chars[e].sex)
        print("\n")
        print("Character gsm: ")
        print(full_charmap.chars[e].gsm)
        print("\n")
        print("Character living status: ")
        print(full_charmap.chars[e].alive)
        print("\n")
        print("Number of appearances: ")
        print(full_charmap.chars[e].appearances)
        print("\n")
        print("First appearance: ")
        print(full_charmap.chars[e].first_appear)
        print("\n")
        print("Year created: ")
        print(full_charmap.chars[e].year)
        print("\n")
        run_prgrm=str(input("Enter any key to search the database again, or type 'no' to quit."))


main()
  