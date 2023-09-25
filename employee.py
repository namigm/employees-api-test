class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls, arg1, arg2):
        # cls refers to the class itself
        print(f"This is a class method of {cls}")
        print(f"Arguments: {arg1}, {arg2}")


# Create an instance of the class
obj = MyClass("I am an instance variable")

# Access the class variable
print(obj.class_variable)  # Output: I am a class variable

# Call the class method
obj.class_method("arg1", "arg2")
