import random
def Create_Matrix_Fixed_Size():
    Dimension = input("Enter Dimension:")
    if Dimension.isnumeric():
        Matrix_Size = int(Dimension)
        Matrix_n_n = [[] for k in range(Matrix_Size)]
        print("You Need To Enter {} Values".format(Matrix_Size ** 2))
        print("Press 1 fill Random Values to your Matrix")
        print("Press 2 to fill Manual values(Time Consuming)")
        Matrix_Input_Data = input("Which One Do you Prefer:")
        if Matrix_Input_Data.isnumeric():
            if str(Matrix_Input_Data) == "1":
                for x in range(0, Matrix_Size):
                    for y in range(0, Matrix_Size):
                        Matrix_n_n[x].append(random.randrange(1000, 9999))
                return Matrix_n_n
            elif str(Matrix_Input_Data) == "2":
                for x in range(0, Matrix_Size):
                    for y in range(0, Matrix_Size):
                        Matrix_n_n[x].append(input("Enter Value For [{0}][{1}]\t".format(x,y)))
                        
                return Matrix_n_n
            else:
                print("Invalid Option")
                return Create_Matrix()
                
    else:
        print("Please Enter Numeric Values")
        return Create_Matrix()

def Create_Matrix_Var_Size():
    Row_Size_m  = input("Enter Row_Size\t:")
    Column_Size_n  = input("Enter Column_Size\t:")
    if(Row_Size_m.isnumeric() and Column_Size_n.isnumeric()):
        print("You Need To Enter {} Values\t:".format(int(Column_Size_n) * int(Row_Size_m)))
        print("Press 1 fill Random Values to your Matrix:")
        print("Press 2 to fill Manual values(Time Consuming:)")
        Matrix_m_n =[ [x for x in range(int(Column_Size_n))] for k in range(int(Row_Size_m))]
            #     print(Matrix_m_n)
        Matrix_Input_Data = input("Which One Do you Prefer:")
        if Matrix_Input_Data.isnumeric():
            if str(Matrix_Input_Data) == "1":
            #             print("In 1 loop")
                for x in range(0, int(Row_Size_m)):
                    for y in range(0, int(Column_Size_n)):
                        Matrix_m_n[x][y]=(random.randrange(1000, 9999))
                return (Matrix_m_n)
            elif str(Matrix_Input_Data) == "2":
                print("In elif")
                for x in range(0, int(Row_Size_m)):
                    for y in range(0, int(Column_Size_n)):
                        Matrix_m_n[x][y]=(input("Enter Value For [{0}][{1}]\t".format(x,y)))
                return (Matrix_m_n)
print(Create_Matrix_Var_Size())
print(Create_Matrix_Fixed_Size())