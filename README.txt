Aaditya Jadhav
Harikrishna Kuttivelil
CSE 20
asgn10.1 README.txt
Wireless Gaming Mouse Documentation
* Class: WirelessGamingMouse
   * The real world object that I chose was a wireless gaming mouse that I ended up choosing because I was looking around and I saw my mouse lying on my table. This ended up working out because the mouse has multiple things that can be used for getter and setter methods. I ended up picking the rgb (red/green/blue) colors and the dpi (dots per inch) sensitivity for these methods. The attributes that I gave the mouse class were the rgb color, dpi, battery life, and skate condition. The skates are the smooth attachments on the bottom of mice that help them glide across surfaces. The mouse class also has two unchanging class variables which are the tracking method and material composition. Both will always be optical and plastic for this class of wireless gaming mice. For my other methods, I simulated using the mouse, charging the mouse, and replacing the skates on the mouse.
* Variables
   * Class Variables
      * trackingmethod - this class variables is to define that all the mice in this class will have the same method of tracking which is optical tracking
      * material - this class variable explains that all of the mice in this class will be composed of the same material which is plastic
   * Data Variables
      * battery - the battery data variable stores the amount of charge that is left in the battery as a percentage with a max of 100%
      * rgb - the rgb data variable stores the current color that the mouse is displaying
      * skatelife - the skatelife data variable stores the current condition of the skates of the mouse as a percentage with a max of 100%
      * dpi - the dpi data variable stores what the current sensitivity is set to on the mouse
* Methods
   * get_rgb - This method returns the current color that is being displayed on the mouse. Doesn’t take anything as an argument.
   * get_dpi - This method returns the current dpi sensitivity that the mouse is set to. Doesn’t take anything as an argument
   * set_rgb - Takes in a string with a color as an argument. Sets the new color being displayed on the mouse to that color
   * set_dpi - Takes in an int as an argument. Sets the new dpi sensitivity on the mouse as the int.
   * use - This method simulates using the mouse for a certain number of hours and for a certain activity. Takes in hours as an int and activity as a string as parameters. This method calculates how much battery is left and the condition of the mouse skates after a session of using the mouse and returns the values as percentages. The battery depletion and skate deterioration occurs at a greater rate when the mouse is being used for gaming.
   * charge - This method simulates charging the mouse over a certain period of time  with different wattages. Takes in hours as an int and amount of watts as an int for the parameters. This method calculates how much battery has been charged and returns the total capacity remaining.
   * replaceskates - This method simulates changing the skates on the mouse with brand new skates. It doesn’t take in anything as a parameter and updates the data variable for skates to be 100%.
* Demo Program Documentation
   * Essentially what happens in the demo program is that two different wireless gaming mouse objects are created and they are run through multiple methods to see what the return values are and how the attributes of the object change. The first is a razer mouse which is new so the stats are maxed out (100% battery, 100% skate condition). The getter and setter methods are tested, then the mouse is used for 5 hours of gaming, then charging for 2 hours, then used again for 3 hours of work. The charge method is also tested for what happens when the mouse is charged with the wrong charger of incorrect wattage. The razer mouse is also charged to the max at one point. The class variables are then printed out. A new mouse, glorious mouse, object is made which has worn out skates and low battery. The mouse is used for 10 hours and both the battery runs out and skates become unusable. Then the replaceskates method is called to change the old skates with new ones and the mouse is charged to the max.
   * The main function runs by itself when the file is run. There is no need for special user input as the demo code has the parameters already set when the functions are being called. It explores all of the extremities so that it can show how the method reacts to different inputs.