                # Using Python For Patterns

def all():

                # Use Nested For Loop To Print Stars(*) In Patterns

    def my_func():
        n = 5
        for i in range (0 , n):
            for j in range(0,i+1):

                print("*" ,end="")
            print("\r")
    my_func()

                # Number Patterns Using Nested Loop

    def patt():
        n = 5
        num = 1
        for i in range(0,n):
            
            num = 1
            for j in range (0,i+1):

                print(num, end=" ")
                num += 1
            print("\r")
    patt()

                # Charecter Patterns Using Nested Loop

    def char():
        n = 5
        num = 65

        for i in range(0,n):
            
            for j in range(0, i+1):
                ch =chr(num)

                print(ch,end=" ")

            num += 1
            print("\r")
    char()

all()