class Test:
    "Run this class"
    count = 1;

    #print(count);

    def __init__(self,name,salary):
        super().__init__()
        self.name=name;
        self.salary=salary;
        Test.count += 1;

    def displayCount(self):
       # print(self.count);
        #print(self.salary)
        print(self.name)


#emp1 = Test("Zara", 2000);
emp2= Test("Lara", 4000)
emp2.age=7
print(delattr(emp2,"salary"))
setattr(emp2,"age",2)
print(getattr(emp2,"age"))
print(hasattr(emp2,"salary"))
#print(delattr(emp2,"salary"))
#emp1.displayCount();
emp2.displayCount();

print ("Employee.__doc__:", Test.__doc__)
print ("Employee.__name__:", Test.__name__)
print ("Employee.__module__:", Test.__module__)
print ("Employee.__bases__:", Test.__bases__)
print ("Employee.__dict__:", Test.__dict__)