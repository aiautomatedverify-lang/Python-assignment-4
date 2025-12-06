try:
    filename = "output.txt"
    x = input("Enter the content to write in the file :")
    with open(filename,"w") as file:
        file.write(x)
        print("The data that written successfully in file ",filename)

    y = input("Enter the additional content to write in the file :")
    with open(filename,"a") as file:
        file.write("\n")
        file.write(y)
        print("Data Sucessfully appended")

    print("The final content of the file ", filename)
    with open(filename, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("The File ",filename," was not found.")

except Exception as e:
    print("Error",e)






