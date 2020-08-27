"""
@author Deepak Chakravarthy
-------------------------------
This Program is for Study and Personal Purpose Only
Program run Only to the Specifed Link
TO Check the Program with the Link Ask Admin of this Code or Admin of the Repository
to send the Link
Mail Me @
DeepakChakravarthy@Cyberservices.com
"""
# install Requests Module using  Pip
import requests
print('\n')
print("############### Book Downloader ###################")
print("###@Author: DeepakChakravarthy  ###################")
print("##Note:=>Enter Only the Link Given By Admin########")
print("###################################################")
print('\n')
#Enter_Link  = input("Enter the Link to Kick Start :")
pgno = int(input("Enter the Maximum Page Number"))
filename = "dc[download]pg="

try:
    for i in range(pgno):
        flink = ("")#Link of the book #
        flink = flink + str(i)#where i is the Page Number which is concat with flink above
        pgsize = "&pit=2"#Page Size with Default
        flink = flink+pgsize# Concat all above to 1
        #print(flink)
        #--------------IMAGE DOWNLOADER --------------#
        # REQUESTING FROM THE WEBSITE TO DOWNLOAD THE IMAGES
        response = requests.get(flink)
        # Filename must be of filename+i(loop)count
        filename = filename+str(i)
        # Extension to Save the File
        extension = ".png"
        # Concatination of the both Filename and the Extension
        filename = filename+extension
        #------------------------- Printing Conventions-----------------#
        #Seperation of File NAME
        print("###########################")
        print(filename)
        print("###########################")
        # SAVING PROCESS TO THE IMAGES
        file = open(filename, "wb")
        file.write(response.content)
        # CLOSING OF ALL THE FILE OPERATIONS
        file.close
        # ----------------------------------------------------------
        # BELOW LINE IS USED TO REMOVE THE DUPLICATED EXTENSIOM
    
    """ Because each time the loop Runs all name Nameing Convention
Changes example
    1)dc[download]pg0.png
    2)dc[download]pg=0.png1.png
    3)dc[download]pg=0.png1.png2.png
    4)dc[download]pg=0.png1.png2.png3.png
    """
    filename = filename.replace(extension,'')
    #-------------------------------------------------------------
    # BELOW LINE IS USED TO CHANGE THE FILENAME WITH CONTINUOUS NUMBER
    """ Because each time the loop Runs all name Nameing Convention
Changes example
    1)dc[download]pg=0.png
    2)dc[download]pg=01.png
    3)dc[download]pg=012.png
    4)dc[download]pg=0123.png
    5)dc[download]pg=01234.png
    """
    filename = "dc[download]pg="
    print("#########################################")
    print("     #-------Images Ready------#         ")
    print("#########################################")

    #--------------------------------------------
except Exception as a:
    print("--->Get the Link From the Admin<----")

