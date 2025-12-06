try:
    filename = "sample.txt"
    print("Reading the file content:")
    with open(filename,'r') as file:
        x = 0
        for line in file:
            print("Line",x,":",line)
            x+=1

except FileNotFoundError:
    print("The File ",filename," was not found.")


