class AllFunctions():
    def Subfields():
        Fields=("Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
        print("Sub-fields in AI are:")
        for subFields in Fields:
            print(subFields)
    def OddEven():
        Number=int(input("Enter a number:"))
        if (Number%2==1):
            print(Number,"is odd number")
        else:
            print(Number,"is Even number")
        return Number
    def Elegible():
        Gender=str(input("Your Gender:"))
        Age=int(input("Your Age:"))
        Gender1=Gender.lower()
        if Gender1=="male":
            if Age>20:
                print("ELIGIBLE")
                status ="ELIGIBLE"
            else:
                print("NOT ELIGIBLE")
                status ="NOT ELIGIBLE"
        elif Gender1=="female":
            if Age>18:
                print("ELIGIBLE")
                status ="ELIGIBLE"
            else:
                print("NOT ELIGIBLE")
                status ="NOT ELIGIBLE"
        return status
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        percentage= (total/500)*100
        print("Total :",total)
        print("Percentage :",percentage)
        return percentage
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        AOT=(Height*Breadth)/2
        print("Area of Triangle:",AOT)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth1=int(input("Breadth1:"))
        print("Perimeter formula: Height1+Height2+Breadth1")
        POT=Height1+Height2+Breadth1
        print("Perimeter of Triangle:",POT)
