import time #this library is used for lagging some of the output in order to create a more user-friendly console experience. I don't intend to do the same thing on the website...this is just because console is sometimes difficult to read!
fileName="marvel-wikia-data.csv" #traceback to the file to access the information!

class CharacterEntry: #This class retrieves the information of the user's chosen character and returns properly parsed information fields that are accessible individually!
  def __init__(self, line : str):
#take a line of the file and parse it into information fields
    line=line.strip()
    data=line.split(",")
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

 
class TheIndex: #This is the big daddy of the program. The methods in this class do most of the "heavy lifting" associated with building the index and allowing the user to interact with that index of characters.
  def __init__(self, fileName : str): #initializer method that opens the file, creates an empty dictionary, and creates an empty list. Sets index to 0 so tracking lines where characters appear in the file is easier!
    char_names = open(fileName)
    self.charmap={}
    self.chars=[]
    index=0
    for line in char_names:  #Takes each line in the file 
      charData=CharacterEntry(line) #Takes the parsed data from CharacterEntry
      self.chars.append(charData) #Adds that data to the list of characters.
      fullname=charData.char #Gathers the "full name" from the parsed data
      names=fullname.lower().split(" ") #divides each of the names by space (ie. "Peter Parker" becomes "Peter" and "Parker"; two separate names)
      for name in names: 
          if name in self.charmap: #if the name is found, add its location (index) to the index
            self.charmap[name].append(index)
          else:
            self.charmap[name]=[index] #if the name is not found, save its location
      index+=1  #this line is done, so add 1 to move to the next line
    return
  def getResults(self,user_entry): #returns the sorted index of characters that match the entry
    return self.charmap.get(user_entry) 

        
def main(): #this function takes the methods used above and outputs it in a clean, efficient manner.
  full_charmap=TheIndex(fileName) #call the big daddy function (the one that makes the index)
  run_prgrm = "yes" #allows for user descretion on whether or not to continue searching again, set to "yes" to start
  while run_prgrm != "no": #read above
    user_entry=input("Please enter the name of a character to search the database: ").lower() #User inputs a name,which is then lowered to match names in index since they are also lowered for consistency (since it's case-sensitive)
    print("Looking up matches for the name","'"+user_entry+"'"+". . .\n")
    time.sleep(1.5)  #Since there are potentially lots of lines of output, I want the user to see what their input was so they are able to more clearly follow the program as it moves through the search.
    l=full_charmap.getResults(user_entry) #call the charmap method to get the results for the user's entry
    if l == None: #just in case there aren't any matching entries, run through this if statement to prompt the user for a name that is found in the entries
      print("No entries matching the name"+" '"+user_entry+"'","were found.\n")
      run_prgrm=input("Enter any key to search the database again or type 'no' to quit: ")
    else: #this is pretty self-explanatory. Takes user's input and prints the lines where that input matches entries in the index.
      print("The name","'"+user_entry+"'", "is found on the following lines: \n")
      for e in l:
        print(e, full_charmap.chars[e].char)
        time.sleep(.25)
      pick_char=int(input("Enter the line of the character whose data you wish to view: ")) #prompts the user to input the line # that they wish to view the information for
      print("Retrieving data . . . \n\n If fields are left blank, data for that character attribute is unknown.\n")
      time.sleep(1.50)
      for i in l: #Match up the user's # selection (index number) and print out the data associated with that character.
        if i == pick_char:
          print("Character ID and Name: ")
          print(i,full_charmap.chars[e].char)
          time.sleep(.5)
          print("Character URL: ")
          print(full_charmap.chars[e].urlslug)
          time.sleep(.5)
          print("Character identity: ")
          print(full_charmap.chars[e].identify)
          time.sleep(.5)
          print("Character alignment: ")        
          print(full_charmap.chars[e].alignment)
          time.sleep(.5)
          print("Character eye color: ")       
          print(full_charmap.chars[e].eyecolor)
          time.sleep(.5)
          print("Character hair color: ")
          print(full_charmap.chars[e].hair)
          time.sleep(.5)
          print("Character sex: ")
          print(full_charmap.chars[e].sex)
          time.sleep(.5)
          print("Character gsm: ")
          print(full_charmap.chars[e].gsm)
          time.sleep(.5)
          print("Character living status: ")
          print(full_charmap.chars[e].alive)
          time.sleep(.5)
          print("Number of appearances: ")
          print(full_charmap.chars[e].appearances)
          time.sleep(.5)
          print("First appearance: ")
          print(full_charmap.chars[e].first_appear)
          time.sleep(.5)
          print("Year created: ")
          print(full_charmap.chars[e].year)
          print("\n")
          run_prgrm=input("Enter any key to search the database again, or type 'no' to quit: ")


main()
  