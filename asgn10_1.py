#Aaditya Jadhav
#12/6/2021
#CSE 20, Harikrishna Kuttivelil, Assignment 10.1
#From the description of 10.1 : "You will need to implement a class that is based on a real-world object.
# Your class will also have to follow encapsulation, meaning that all internal object variables will have to be private. Your custom class will require the following variables and methods:
# At least 1 class variable.
# At least 2 data variables. Remember that due to encapsulation, you will have to make these variables private.
# At least 2 get-set methods. Because your class will follow encapsulation, methods must be used to access any variables that should be accessed. These methods are usually named with the scheme get_[variable] and set_[variables], hence the term "get-set". An example from class is when we implemented the Car class, we implemented self.set_position and self.get_position to access the private variable self.__position.
# At least 2 other methods. This does not include get-set methods. These methods will have to do something interesting and non-trivial. Use your own judgment on this and be creative; this is where you can display your skills the most (and score the most points!)."

class WirelessGamingMouse:
  #class variables that do not change
  trackingmethod = "optical"
  material = "plastic"

  #class constructor which takes in the current battery as a percentage, rgb color, the condition of the skates as a percentage, and the dpi which is dots per inch (essentially the sensitivity of the mouse)
  def __init__(self, battery, rgb, skatelife, dpi):
    #saving the data variables
    self.__battery = battery
    self.__rgb = rgb
    self.__skatelife = skatelife
    self.__dpi = dpi

  #first getter method which returns the current rgb color on the mouse
  def get_rgb(self):
    return f"The current RGB color is: {self.__rgb}"
  
  #second getter method which returns the current dpi on the mouse
  def get_dpi(self):
    return f"The current DPI is: {self.__dpi}"

  #first setter method sets the new desired color and returns an updated statement on the color
  def set_rgb(self, color):
    self.__rgb = color
    return f"The new RGB color is set to: {self.__rgb}"
  
  #second setter method sets the new desired dpi and returns an updated statement on the dpi
  def set_dpi(self, dotsperinch):
    self.__dpi = dotsperinch
    return f"The new DPI is set to: {self.__dpi}"

  #this method simulates using the mouse for a certain number of hours and for a certain activity
  def use(self, hours, activity):
    #temporary variables that are used for calculations
    batteryused = None
    skatesused = None
    #if the activity is gaming, the rate at which the battery depletes and the skates deteriorate is greater
    if activity == "gaming":
      #This is the rate at which the battery depletes while gaming
      batteryused = 8.3 * hours
      #This is the rate at which the skates deteriorate while gaming
      skatesused = 0.002 * hours
      #updates the object's data variables after the usage
      self.__battery = self.__battery - int(batteryused)
      self.__skatelife = self.__skatelife - skatesused
      #ensures that the battery cannot go below 0%
      if self.__battery <= 0:
        print("The mouse battery is dead, please charge!")
      else:
        print(f"You have {self.__battery}% charge left!")
      #ensures that the skate condition cannot go below 0%
      if self.__skatelife > 0:
        print(f"Your mouse skates' condition is at {self.__skatelife}% of peak performance")
      else:
        print("Please replace your mouse skates!")
    #if the activity is anything else, the rates of depletion and deterioration are lesser
    else:
      #batter and skate life calculations which are less than when gaming
      batteryused = 5 * hours
      skatesused = 0.001 * hours
      #data variables are updated
      self.__battery = self.__battery - int(batteryused)
      self.__skatelife = self.__skatelife - skatesused
      #ensures that the battery does not drop below 0%
      if self.__battery <= 0:
        print("The mouse battery is dead, please charge!")
      else:
        print(f"You have {self.__battery}% charge left.")
      #ensures that the skate condition does not drop below 0%
      if self.__skatelife > 0:
        print(f"Your mouse skates' condition is at {self.__skatelife}% of peak performance")
      else:
        print("Please replace your mouse skates!")

  #this method simulates charging the mouse over a certain period of time with different amounts of watts
  def charge(self, hours, watts):
    #temporary variable to help with calculations
    batteryadded = None
    #checks if the charger is compatible (20Watts) and then does calculations to determine how much battery life has been added
    if watts == 20:
      batteryadded = hours * watts * 1.75
      self.__battery = self.__battery + batteryadded
      #ensures that the battery cannot go over 100%
      if self.__battery >= 100:
        self.__battery = 100
        print("The mouse is fully charged!")
      else:
        print(f"The mouse is at {self.__battery}% charge.")
    #returns an error statement if the incorrect charger is being used
    elif watts < 20:
      print("Charger wattage is too low!")

    else:
      print("Charger wattage is too high!")
  
  #simulates changing the skates on the mouse with brand new skates
  def replaceskates(self):
    #condition becomes set to 100%
    self.__skatelife = 100
    print("The skates have successfully been replaced!")

#this the main method and the demo code which goes through all the methods in the class and tests them out
def main():
  #creates a new razer mouse object and it is given complete new stats
  razermouse = WirelessGamingMouse(100, "green", 100, 800)
  #these 4 methods are just the get and set methods for the intitial parameters of the mouse. It gets the color, dpi, sets it to blue and 1600 dpi
  print(razermouse.get_rgb())
  print(razermouse.get_dpi())
  print(razermouse.set_rgb("blue"))
  print(razermouse.set_dpi(1600))
  #these next statements show the methods that simulate using and charging the mouse
  #The mouse is used for gaming for 5 hours 
  razermouse.use(5,"gaming")
  #The mouse is charged for 2 hours at 20 watts
  razermouse.charge(2,20)
  #The mouse is used for work for 3 hours
  razermouse.use(3,"work")
  #The mouse is then charged twice with the incorrect wattages (once under and once over the wattage)
  razermouse.charge(3,10)
  razermouse.charge(3,25)
  #Prints out the class variables that are unchanging
  print(f"The tracking method this mouse uses is: {razermouse.trackingmethod}")
  print(f"The material that this mouse is made of is: {razermouse.material}")
  
  #new glorious mouse object which has worn out skates and low battery
  gloriousmouse = WirelessGamingMouse(30, "purple", 0.01, 2400)
  #sets the dpi to 400 dots per inch
  print(gloriousmouse.set_dpi(400))
  #uses the mouse for gaming for 10 hours
  #this makes the mouse run out of battery and the skates need to be replaced
  gloriousmouse.use(10, "gaming")
  #the skates on the glorious mouse are then replaced
  gloriousmouse.replaceskates()
  #charges the mouse with the correct wattage for 12 hours
  gloriousmouse.charge(12, 20)

#runs the main function
if __name__ == "__main__":
    main()