class BookStore:
    NoOfBook = 0
    def __init__(self,N,A):
        self.name = N
        self.author = A
        BookStore.NoOfBook += 1

    def Display(self):
        print("Name: "+self.name)
        print("Author: "+self.author)
        print("No Of Book: ",self.NoOfBook)

def main():

    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display()

    print("------------------------------------------") 

    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display() 

if __name__ == "__main__":
    main()
      
