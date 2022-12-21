import os

print ("List File dalam directory : ")

for x in os.listdir():

    if x.endswith(".txt"):

        # Prints only text file present in My Folder

        print(x)

print("\n========== Teks Editor ==========")

filename = ""

print("There is no Opened file..")

def checkfile() :

    global filename

    if filename == "" :

        filename = input("Type filename : ")

    else :

        print("Opened file : ", filename)

while True :

    

    checkfile()

    menu = input("(R)ead (A)dd (W)rite (C)lear: ")

    if menu == "R" :

        try :

            f = open(filename,"r")

            print(f.readline())

        except FileNotFoundError :

            print("File tidak ditemukan")

            filename = ""

            checkfile()
