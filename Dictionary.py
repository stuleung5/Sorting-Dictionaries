# Your names: 
# Bryan Leung
# Allen Gao
#
#
# no other modules allowed
import random, time, sys, string

class Dictionary:
    #### To complete
    """######Preliminaries + App2 ######"""
    def __init__(self, name = "N/A"): 

        self.__words = [] #private instance list for all my files
        self.__name = name #private name for all my files e.g. french_sorted.txt
        random.seed(8) #randomized seed for future random words and/or lists
        try:
            if name == "N/A": #Added possibility
                True #Always works
            else:
                f = open(name, "r") #Files I used exist since I can read it.
                f.close() # Every file that's open should be closed
        except:
            print("File " + name + ' does not exist!') 
            sys.exit(0) #Exit using sys import
        
        # For each existing file in the project, I open in read mode. Then, for each line, I add it to my list and remove '\n' as well
        # as split with commas. Finally, I close every file I open.
        f = open(name,'r')
        for line in f:
            self.__words += [line.rstrip('\n').split(',')]
        f.close()
        

    # Get methods help call private instance variables
    def get_name(self): 
        return self.__name

    def get_size(self): 

        return len(self.__words)

    def get_random_list(self, int): #input as integer
        rand_new = [] #Signifies empty list of words to be used among dictionaries
        for i in range(0, int): # variable 'int' tells us how many random words in 'rand_new'
            rand_new += self.__words[random.randint(0, self.get_size() - 1)] # number of random words in list
        return rand_new #Get how many random words I inputed.
  
    #Append list
    def insert(self, add):
        return self.__words.append(add)
    
    #Display one word every line
    def display(self, score = True): ###Optional variable for App 5 to work. If False, then returns nothing.
        if score == False:
            return  
        for i in range(0, self.get_size()):
            print(self.__words[i])
    
    #Calculate time to shuffle words 
    def shuffle(self):
        t1 = time.process_time()
        n = self.get_size() #get length of dictionary
        for i in range(n-1, 0, -1): #using out loop
            random_indx = random.randint(0, i) #random value
            self.__words[i], self.__words[random_indx] = self.__words[random_indx], self.__words[i] #Swap indexes
        t2 = time.process_time()
        return t2 - t1

    # Linear search scanning from first index to last index
    def lsearch(self, input):
        """####O(N) algorithm####."""
        self.__index = 0 #Index starting point
        n = self.get_size() # get length of dictionary
        for i in range(0, n): 
            if self.__words[i] == input: #If input in dictionary, return True Boolean
                return True
            else:
                self.__index += 1 #Reveals index number that is True. 
        self.__index = -1 #Index is -1 if False
        return False 

    # Binary search scanning by approximate intervals of two in a sorted list
    def bsearch(self, input):
        """####O(log N) algorithm#### """
        ### From 0 to length of dictionary
        low = 0 
        high = self.get_size() -1   
        self.__steps = 0 #Number of steps initially at zero. 
        """This TRY/EXCEPT statement deals with scenarios where self.__words[0] is a list and input is a string. 
        If statement fails, string becomes a list. I put this in for App 3."""
        try: 
            self.__words[0]<input 
        except: 
            input=[input] 

        """Return True if mid matches input. Otherwise, if too low, change high to mid-1. 
        If too high, change low to mid+1"""
        while low <= high:
            mid = low + (high - low)//2 
            if self.__words[mid] == input:
                self.__index = mid
                self.__steps += 1 #If True finally add last one.
                return True  
            elif self.__words[mid] < input:
                low = mid + 1
                self.__steps += 1 #If False add one
            else:
                high = mid - 1
                self.__steps += 1 #If False add one
        self.__index = low 
        """ variable 'low' reveals index where false word can be inserted."""
        self.__steps += 1 #If False add one to signify last step
        return False 
    
    #Get methods
    def get_steps(self):
        return self.__steps

    def get_index(self):
        return self.__index 

    """###### App1 ######"""
    def insertion_sort(self):
        t1 = time.process_time()
        n = len(self.__words)
        for index in range(1, n): #outer loop
            key = self.__words[index] #select and store key/pivot
            shift = index #Shift starts at key
            while shift > 0 and self.__words[shift - 1] > key: #Check previous ones by linearly until index zero
                self.__words[shift] = self.__words[shift - 1] #shift key
                shift -= 1 #Increment one step down
                self.__words[shift] = key #insertion

        t2 = time.process_time()
        return t2 - t1
    

        
    def enhanced_insertion_sort(self):
        t1 = time.process_time()
        n = len(self.__words) # Length of dictionary
        located = 0 # Starting at 0
        for index in range(1, n): # For each word. 
            key = self.__words[index] #Key is starting at self.__words[1].
            low = 0 #Low remains constant
            high = index  #High changes value starting from 1. 
            """Similar to Binary Search algorithm. Main difference is high = mid in case mid-1 is greater than the word."""
            while low < high:
                mid = (low + high)//2
                if self.__words[mid] <= self.__words[index]:
                    low = mid + 1
                else:
                    high = mid 
            located = low ### In b-search, located = low refers to index that a FALSE word should be inputted. 
            shift = index #Store index value that can be potentially shifted
            while index > 0 and shift > located: #If located value is greater than key index,  and index is greater than 0. 
                self.__words[shift] = self.__words[shift - 1] #Shift values greater than key index to the right
                shift -= 1 
            self.__words[located] = key #Insert key into self.__words[located] based on binary search
        t2 = time.process_time()
        return t2 - t1
    #Save files based on name. Write down key information from self.__word list. 
    def save(self, name):
        f = open(name, "w")
        for i in range(0, len(self.__words)):
            f.write(str(self.__words[i][0]) + "\n")
        f.close()
        print("Save " + name)

    """###### App 3 ######"""
    def spell_check(self, analyze):
        try: 
            f = open(analyze, 'r') #If file can be read, it exists
        except:
            print("File " + self.__name + ' does not exist!')
            sys.exit(0) #Exit properly
        f = open(analyze, 'r') #Read file for preperation

        #Create three seperate lists: one for original and other for changed. 

        self.__original_list = []
        self.__changed_list = []
        
        punc = '''!-()[]\{\};:',\"<>.\\/?@#$%^&*_~'''
        for lines in f:
            #Remove \n in self.__original_list. Create a list of original text by line.
            self.__original_list += [lines.rstrip('\n')]  
            for words in lines:
                """Create self.__changed_list where punctuation is stripped. Also, all words lowercased. """
                self.__changed_list += words.lower()
        
        ### Use list to remove punc that has a blank space or new/line adjacent by index.
        self.__changed = []

        for i in range(0,len(self.__changed_list)):
            """IF statement removes punc whenever there is a blank space or newline. It also does not count index 0
            or the end of the index to avoid the list getting out of range. """
            if (self.__changed_list[i] in punc and i!=0 and i!=len(self.__changed_list)-1 and (self.__changed_list[i+1]==" "
            or self.__changed_list[i-1]==" " or self.__changed_list[i+1]=="\n" or self.__changed_list[i-1]=="\n")):
                self.__changed_list+=[""] ### This removes puncuation by making it an empty string. 
            else:
                self.__changed += self.__changed_list[i] ### add text if normal

        """self.__changed_list now should be a bunch of letters and spaces with n\lines. """
        """self.__original_list should be a list where each line of text represents an index."""
        ### Empty lists and string to change composition of self.__changed_list to self.__original_list
        self.__format = ""
        self.__byLine = []
        self.__changed_linedlist = []
        self.__original_linedlist = []

        for i in range(0, len(self.__changed)):
            ##### create a string from each index of self.__changed_list with certain conditions. 
            if self.__changed[i] != "\n" and self.__changed[i] != " ":
                self.__format += self.__changed[i] 
            #### If there is a space, add string self.__format to self.__byLine. Reset the string self.__format 
            elif self.__changed[i] == " ":
                self.__byLine += [self.__format] 
                self.__format = ""
            ##### For every new line, after adding the last word before the new line, put the list containing a line of words
            #####  into a new list as an index. Reset line and string. 
            elif self.__changed[i] == "\n":
                self.__byLine += [self.__format]
                self.__changed_linedlist += [self.__byLine]
                self.__format = ""
                self.__byLine = []

        #### For self.__original_linedlist. Seperate each index by string. 
        for j in range(0, len(self.__original_list)):
            self.__original_linedlist += [self.__original_list[j].split()]
        print() #One blank line of space

        #### Empty string and list for final modifications
        self.__improved = ""
        self.__final = []

        """In two FOR loops, I'm scanning each word in original list."""
        for k in range(0, len(self.__original_linedlist)):
            for l in range(0, len(self.__original_linedlist[k])):
                if self.bsearch(self.__changed_linedlist[k][l]) == False:
                    #### In IF statement, if the word is not found in self.__changed_linedlist, 
                    #### add parenthesis to the word in self.__original_linedlist
                    self.__original_linedlist[k][l] = "(" + self.__original_linedlist[k][l] + ")"
                #### Add the word to self.___improved. 
                self.__improved += self.__original_linedlist[k][l] + " " 
            self.__final += [self.__improved] #### Put each line of into a final list by index
            self.__improved = "" #### Reset for every line

        for n in range(0, len(self.__final)):
            print(self.__final[n]) #### Print by line of modified text. 
        f.close()

    """##### App4 #####"""

    def anagram(self, input):
        #### Empty lists 
        self.__scope = []
        self.__narrowed_down = []
        dict4 = Dictionary() ###Instantiate variable to later use sort_word static method
        ult_key = dict4.sort_word(input) #Should return an ordered string. 
        for i in range(0, len(self.__words)):
            for j in range(0, len(input)):
                if len(input) == len(self.__words[i][0]) and input[j] in self.__words[i][0]: 
                    """In IF statement,  If the input has the right length compared to a word in dictionary and a rightly placed
                    letter in input exists in the word from the dictionary,  I put it in self.__scope list to later narrrow down
                    possibilities. """ 
                    self.__scope += self.__words[i]
        for k in range(0, len(self.__scope), len(input)): ### Used len(input) to skip repeats. 
            if dict4.sort_word(self.__scope[k]) == ult_key: 
                """For possible words in dictionary, after being ordered, if there is match, put the word in self.__narrowed_down"""
                self.__narrowed_down += [self.__scope[k]]
        return self.__narrowed_down ### Return a list

    @staticmethod
    def sort_word(word):  # to complete
        """ must return a string with letters included in 'word' that are now sorted"""
        list_word = list(word) # Change word into a list of letters. 
        ordered_word = "" ### Empty string for ordered_word
        n = len(list_word) ### Length of word.
        """I chose to use enhanced insertion since I thought it would be the fastest."""
        located = 0 ### Located initially at zero.
        for index in range(1, n):
            key = list_word[index] #Key is starting at self.__words[1].
            low = 0
            high = index
            while low < high:
                mid = (low + high)//2
                if list_word[mid] <= list_word[index]:
                    low = mid + 1
                else:
                    high = mid
            located = low
            shift = index #Store index value that can be potentially shifted
            while index > 0 and shift > located: #If located value is greater than key index,  and index is greater than 0. 
                list_word[shift] = list_word[shift - 1] #Shift values greater than key index to the right
                shift -= 1 
            list_word[located] = key #Insert key into self.__words[located] based on binary search
        for i in range(0, n):
            ordered_word += list_word[i]
        return ordered_word

       
    
    """##### App5 #####"""
    
    def compute_score_scrabble(self):
        self.__int_list = [0]*len(self.__words) 
        ### In self.__int_list, create length suitable for incrementing points from 0 for every word in self.__words
        """Here, I determine point raise based on whether a letter is in a combination"""
        for i in range(0, len(self.__words)):
            for j in range(0, len(self.__words[i])):

                if ('e' in self.__words[i][j] or 'a' in self.__words[i][j]
                 or 'i' in self.__words[i][j] or 'n' in self.__words[i][j]
                 or 'r' in self.__words[i][j] or 't' in self.__words[i][j]
                 or 'l' in self.__words[i][j] or 's' in self.__words[i][j]
                 or 'u' in self.__words[i][j]):
                    self.__int_list[i] += 1

                if 'd' in self.__words[i][j] or 'g' in self.__words[i][j]:
                    self.__int_list[i] += 2

                if ('b' in self.__words[i][j] or 'c' in self.__words[i][j]
                 or 'm' in self.__words[i][j] or 'p' in self.__words[i][j]):
                    self.__int_list[i] += 3

                if ('f' in self.__words[i][j] or 'h' in self.__words[i][j]
                 or 'v' in self.__words[i][j] or 'w' in self.__words[i][j]
                 or 'b' in self.__words[i][j]):
                    self.__int_list[i] += 4

                if 'k' in self.__words[i][j]:
                    self.__int_list[i] += 5

                if 'j' in self.__words[i][j] or 'x' in self.__words[i][j]:
                    self.__int_list[i] += 8

                if 'q' in self.__words[i][j] or 'z' in self.__words[i][j]:
                    self.__int_list[i] += 10
        return self.__int_list ### Return list

    def score_sort(self):
        """I again used enhanced insertion sort for speed. """
        n = len(self.__int_list)
        located = 0
        for index in range(1, n):
            key = self.__int_list[index] #Key is starting at self.__words[1].
            low = 0
            high = index
            while low < high:
                mid = (low + high)//2
                if self.__int_list[mid] <= self.__int_list[index]:
                    low = mid + 1
                else:
                    high = mid
            located = low
            shift = index #Store index value that can be potentially shifted
            while index > 0 and shift > located: #If located value is greater than key index,  and index is greater than 0. 
                self.__int_list[shift] = self.__int_list[shift - 1] #Shift values greater than key index to the right
                shift -= 1 
            self.__int_list[located] = key #Insert key into self.__int_list[located] based on binary search
        for i in range(0, len(self.__words)):
            self.__words[i] = self.__words[i] + " " + str(self.__int_list[i]) ## Have word and then score
        

    """"##### App6 ######"""
    def crack_lock(self, list_combinations):
        #### Empty string and lists 
        self.__rand_str = ""
        self.__rand_list = []
        self.__desired = [] 
        self.__newdict = []
        x=0

        """Goal of this FOR loop is to find the index within list_combination with
        greatest number of potential letters."""
        for g in range(0,len(list_combinations)):
            if len(list_combinations[g])>x:
                x=g
        for h in range(0,len(list_combinations)**len(list_combinations[x])*6): 
            #### In first FOR loop, I have (length of word)^(potential letters)*6 as a range

            for i in range(0,len(list_combinations)):
                """Here, I have a random string decided by a randomly chosen letter per index."""

                self.__rand_str+=list_combinations[i][random.randint(0,len(list_combinations[i])-1)]

                """In IF statement, once the length of the string is the same as the number of user 
                inputted letters, I put this string in a new list and reset the string."""
                if len(list(self.__rand_str)) == len(list_combinations):
                    self.__rand_list += [self.__rand_str]
                    self.__rand_str=""

        for j in range(0,len(self.__rand_list)):
            """This IF statement gets rid of repeats."""
            if self.__rand_list[j] not in self.__desired:
                self.__desired+=[self.__rand_list[j]]
        for k in range(0,len(self.__desired)):
            #### This IF statement determines if word can be found in the dictionary using binary search.
            if self.bsearch(self.__desired[k])==True:
                self.__newdict += [self.__desired[k]]
        """Write a new file called new.txt and in every line, write a word"""
        f = open("new.txt", "w")
        for t in range(0, len(self.__newdict)):
            f.write(self.__newdict[t] + "\n")
        f.close()
        """Return Dictionary object. This way, in App 6, after variable is instantiated, dlock_code.display() and
        other called methods can work. """
        return Dictionary("new.txt") 
        
        

    """##### Provided Information ######"""
    def selection_sort(self):    #provided to you
        """Perfom selection sort,  must return the time it takes to sort the list of words
        Remark: Routine works 'in-place'"""
        t1 = time.process_time() #capture time
        n = self.get_size()
        for out in range(n-1):        #outer loop
            #find minimum between out + 1 and n-1
            imin = out
            for i in range(out + 1, n):  #inner loop
                if self.__words[i] < self.__words[imin]: 
                    imin = i #update  minimum index
            #swap (3 step here)
            temp = self.__words[imin]
            self.__words[imin] = self.__words[out]
            self.__words[out] = temp
        t2 = time.process_time() #capture time
        return t2-t1


    @staticmethod  # provided to you
    def get_word_combination(word,  combs = ['']):
        """ return a list that contains all the letter combinations (all length) of the input 'word' """
        if len(word) == 0:
            return combs
        head,  tail = word[0],  word[1:]
        combs = combs + list(map(lambda x: x+head,  combs))
        return Dictionary.get_word_combination(tail,  combs)







########################################################################
########################################################################


def main():

    ### step-1 test constructor
    name=input("Enter dictionary name (from file 'name'.txt): ")    
    dict1=Dictionary(name+".txt")

    ### step-2 test get_name, get_size, get_random_list        
    print('Name first dictionary:', dict1.get_name())   
    print('Size first dictionary:', dict1.get_size()) 
    print("Five random words:", end=" ")
    rlist=dict1.get_random_list(5) # 5 means the number of random words we want
    for w in rlist: print(w, end=" ")
    print("\n")

    ### step-3 test constructor again
    dict2=Dictionary()
    print('Name second dictionary:', dict2.get_name())
    
    ### step-4 test insert and display
    for w in rlist: dict2.insert(w)
    print('Display second dictionary:')
    dict2.display()

    ### step-5 test shuffle 
    t=dict2.shuffle()
    print('\nSecond dictionary shuffled in %ss:'%t)
    print('Display second dictionary:')
    dict2.display()

    ### step-6 test linear search
    word="morning"
    print("\nLinear search for the word '%s' in second dictionary"%word)
    status=dict2.lsearch(word)
    print("Is '%s' found: %s at index %s"%(word, status, dict2.get_index()))

    ### sort second using selection sort (provided to you)
    t=dict2.selection_sort()
    print('\nSecond dictionary sorted in %ss:'%t)
    print('Display second dictionary:')
    dict2.display()

    ### step-7 test binary search (find it)
    word="morning"
    print("\nBinary search for the word '%s' in second dictionary"%word)
    status=dict2.bsearch(word)
    print("Is '%s' found: %s at index %s"%(word, status, dict2.get_index()))

    # binary search (did no find it)
    word="ning"
    print("\nBinary search for the word '%s' in second dictionary"%word)
    status=dict2.bsearch(word)
    print("'%s' is not found so it must be inserted at index %s"%(word, dict2.get_index()))
    

    


## call the main function if this file is directly executed
if __name__ == "__main__":
    main()
