class Calculator:
    brand='Casio Ms000'
    price=1000
    Battery_quality='AA/AAA or Casio MS series'

    def deduct(self,a,b):
        result=a-b
        print(result)

    def multiply(self,a,b):
        result=a*b
        print(result)

    def divide(self,a,b):
        if b==0:
            print("Enter valid value")
        else:
            result=a/b
            print(result)

my_calculator=Calculator()
my_calculator.deduct(17,5)
my_calculator.divide(9,0)
my_calculator.multiply(4,5)