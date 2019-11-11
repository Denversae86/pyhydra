import os
print("Greetings! Please fill in the fields carefully. \n Use this program only for the files of the same format (for example 'pdf')")
path=str(input("please enter the destination folder path: "))
format=input("please enter the file format (like 'exe' or 'xlsx' without dot): ")
fname=input("Please enter the constant part of the name: ")
    
def main():
    i=int(input("Please enter the first number for counting process \n(only number values are accepted): "))
    for filename in os.listdir(path):
        dst =str(fname) + "_"+str(i) + "." + str(format)
        src=path +"\\"+filename
        dst=path +"\\"+dst 
        if format in str(filename):
            pass
        else:
            print("At least one of the files does not have the mentioned format")
            quit()
        #rename() function will rename all the files 
        os.rename(src, dst) 
        i += 1
  
 #Driver Code 
if __name__ == '__main__':     
    # Calling main() function 
   main()
print("Proceeding...Done!")