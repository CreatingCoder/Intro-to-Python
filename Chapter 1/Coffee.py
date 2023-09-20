class Coffee:
    def __init__(self, roast, sweetner):
        self.roast= roast
        self.sweetner = sweetner
    
myCoffee = Coffee("Dark", "Sweet n Low")
print(myCoffee.roast + " roast, with " + myCoffee.sweetner + " sweetner")
