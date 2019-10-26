##############################
#
#  Made by:  Pc1h6a9h6
#  Name:     ChangeWallpaper
#  Version:  2-beta
#
##############################

# Call the libraries
import os, shutil

# Create de fuction who change the wallpaper
def copyImg(fileFrom, user):
    # Erase existing wallpaper
    try:
        os.remove("C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles\\CachedImage_????_???_POS?.jpg")
        os.remove("C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")
    except:
        pass
    
    # Create the new wallpaper
    try:
        shutil.copy2(fileFrom, "C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\CachedFiles\\CachedImage_1600_900_POS4.jpg")
        shutil.copy2(fileFrom, "C:\\Users\\"+user+"\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper")

        # print if successful
        print("The wallpaper was successfully created!")
    except:
        # print if error
        print("Error creating Wallpaper!")

def main():
    # clear the screen console
    os.system("cls")

    # get the name of user
    user = os.environ["USERNAME"]

    # get the name of image
    name = input("\nMove your image here:\n>> ")

    # call the function
    copyImg(name, user)

# execute program
if __name__ == "__main__":
    main()