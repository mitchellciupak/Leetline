#CreatedBy: Mitchell Ciupak
#Created On: 20200616

# Import
import os
import platform
import sys

# This class holds all important system information and user data
class Program: 

    def __del__(self):
        #Trigger Deconstructor by: del obj
        #TODO Set Some Values to null before pickiling
        #Pickle it!
        print("Self Destructing .....")

    # Pull Operating System ("Windows,"Linux","Darwin")
    def getOS(self):
        self.os = platform.system()
        return self.os

    # Pull Current DateTime (yyyyMMdd_hhmmssss)
    def getDateTime(self): 
        print ("Under Construction")
        return "17760704_00000000"

    def getPrefDirectory(self):
        try:
            os.path.isdir(self.dir)
            return self.dir
        except:
            self.dir = input("Please enter your folder path: ") 
            while not (os.path.isdir(self.dir)):
                print("This folder was not found. Please Create and Try Again")
                self.dir = input("Please enter your folder path: ") 
            return self.dir

    def getPrefEditor(self):
        self.editor = "VS Code"
        return self.editor

    def getPrefLanguage(self):
        try:
            return self.lang
        except:
            self.lang = input("Please enter your programming language: ") 
            while not(self.lang == "Python" or self.lang == "C/C++"):
                print("I'm sorry, we are currently only supporting 'Python' or 'C/C++.'")
                self.lang = input("Please enter your programming language: ") 
            return self.lang

    def getPrefName(self):
        try:
            return self.author
        except:
            self.author = input("Please enter your name/alias: ")
        return self.author

    def changeUser(self):
        del self.author
        del self.lang
        del self.dir
        del self.editor
        self.newUser()

    def newUser(self):
        name = self.getPrefName()
        lang = self.getPrefLanguage()
        folder = self.getPrefDirectory()
        editor = self.getPrefEditor()

        print("Please review the following settings:")
        print("Your name is " + name + ", who speaks in the toung of " + lang + ", in the land of " + folder + " and you use " + editor + " as your wepon of choice against evil!\n")
        confirmation = input("Press enter to continue or type 'I have a small penis' to change your settings: ")
        if(confirmation != ''):
            self.changeUser()
        #TODO Production
        #print("Great! Remember you can chage your settings anytime by using the command 'leetline.exe changeUser'")