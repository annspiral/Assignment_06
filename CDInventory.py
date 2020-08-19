#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AAllen, 2020-Aug-15, Added function get_new_entry() in IO
# AAllen, 2020-Aug-15, Added functions add_CD(), delete_CD() in DataProcessor
# AAllen, 2020-Aug-15, Added function write_file() in FileProcessor
# AAllen, 2020-Aug-15, updated function comments, added get_sorted_values_list()
# AAllen, 2020-Aug-15, added error checking in get_new_entry() for ID
# AAllen, 2020-Aug-17, cleaned up some docstrings
# AAllen, 2020-Aug-18, moved call to DataProcessor.get_sorted_values_list()
#                       out of IO.get_new_entry()
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    @staticmethod
    def add_CD(tplEntry, table):
        """Function to add a CD dictionary entry to the table/inventory
        
        Takes a tuple of entry strings (ID, Title, Artist) and creates a 
        dictionary collection {'ID':num, 'Title':string, 'Artist':string}
        that is added to the full inventory table, which is a list of dictionaries
        
        Args:
            tplEntry: a tuple of strings containing values to be added into
            dictionary collection and table - expected order of ID, Title, Artist.
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime
        
        Returns:
            None
        
        """
        # convert tuple values into dictionary item
        dicRow = {'ID': int(tplEntry[0]),
                  'Title': tplEntry[1],
                  'Artist': tplEntry[2]}
        # add dictionary to current table
        table.append(dicRow)


    @staticmethod
    def delete_CD(intDelID, table):
        """Function to delete a CD dictionary entry from the table/inventory
        
        Deletes the row identified by the ID value from the inventory table.
        The row is a dictionary entry that represents each CD.
        
        Args:
            intDelID: ID value for the dictionary collection in the list that
            will be deleted
            table (list of dict): 2D data structure (list of dicts) that holds
            the CD inventory data during runtime
        
        Returns:
            None.
        
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == intDelID:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
      
        
    @staticmethod
    def get_sorted_values_list(table, key='ID'):
        """Function to get all values of the specified key from a list of
        dictionaries
        
        Creates a sorted list of all the values for the key provided that are
        currently in the inventory table (2D list of dictionaries)
        
        Args:
            table: expects a 2D table that is a list of dictionaries
            key: key for which values are retrieved from the dictionaries,
            defaults to look for a key name 'ID'
        
        Returns:
            sorted list of all values with the provided key that are
            in the 2D table
        
        """
        lstIDsUsed = []
        #get a list of all values for the key parameter
        for row in lstTbl:
            lstIDsUsed.append(row.get(key))
        lstIDsUsed.sort()
        return lstIDsUsed
        


class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one 
        dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()
        pass


    @staticmethod
    def write_file(file_name, table):
        """Function to write updated inventory list of dictionaries to file

        Writes the data in table to the file identified by file_name. Table is
        a list of dictionaries. Each dictionary item is written to a line in 
        the file, with a newline ending. The dictionary is written as the 
        value from each key/value pair separated by a comma

        Args:
            file_name (string): name of file used to save to
            table (list of dict): 2D data structure (list of dicts) that holds 
            the data during runtime

        Returns:
            None
        """
        objFile = open(strFileName, 'w')
        # for each dictionary 'row' in the table, convert values into a single,
        # comma separated string with an ending newline and write to file
        for row in table:
            lstValues = list(row.values())
            # ID integer value needs to be converted to string for output
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        pass

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')


    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice


    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that
            holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')


    @staticmethod
    def get_new_entry(lstTestIDs):
        """Requests the new entry values, ID, Title, Artist
            
         Args:
            lstTestIDs: a list containing IDs currently in use in the table

        Returns:
            tplNewEntry: a tuple of three strings with the user's input for the
            (ID, Title, Artist) for a new CD entry
    
        """
        # Get a unique entry ID
        entryID = '' # create empty default ID
        validID = False # Flag to indicate valid ID identified
        # request an ID number from user
        entryID = input('Enter ID number: ').strip()
        # verify ID number and re-ask as needed
        while not validID:
            # if the user does not enter an ID, find one and assign it
            # if the list of current IDs is empty, start with ID 0
            if entryID == '' and ((lstTestIDs == []) or (lstTestIDs == None)):
                entryID = 0
                break
            # assign a CD ID, by finding the next ID number to use
            # get last, highest ID value and get next ID 
            elif entryID == '':
                entryID = lstTestIDs[-1] + 1
                break
            # if the user enters a non-numeric character, ask for ID again,
            # and loop back through
            if not entryID.isnumeric():
                entryID = input('Please Enter a numerical ID number: ').strip()
                continue
            # if the user enters an ID already in the list, ask for a new ID
            if int(entryID) in lstTestIDs:
                entryID = input('ID =' + entryID + ' is already being used.\n' +
                                'Please choose a different ID or [enter] to' +
                                ' assign one automatically: ').strip()
            else:
                validID = True
                            
        # get the entry title and artist, these can be blank                    
        entryTitle = input('What is the CD\'s title? ').strip()
        entryArtist = input('What is the Artist\'s name? ').strip()
        
        # create new entry tuple with ID, Title and Artist
        tplNewEntry = (entryID, entryTitle, entryArtist)
        return tplNewEntry


# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.0 get the sorted list of IDs currently in use
        lstTestIDs = DataProcessor.get_sorted_values_list(lstTbl)
        # 3.3.1 Ask user for new ID, CD Title and Artist
        tplUserEntry = IO.get_new_entry(lstTestIDs)
        # 3.3.2 Add item to the table
        # 3.3.2.1 Add item with users values to the table
        DataProcessor.add_CD(tplUserEntry, lstTbl)
        # 3.3.2.2 Display inventory to user to confirm CD added
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        # 3.5.2.1 delete CD with requested ID
        DataProcessor.delete_CD(intIDDel, lstTbl)
        # 3.5.2.2 display inventory to user after delete for confirmation
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




