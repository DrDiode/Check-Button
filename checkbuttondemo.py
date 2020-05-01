"""
Program: checkbuttondemo.py
Author: Andrew 4/29/2020
Exercise on pages 281 - 282
"""

from breezypythongui import EasyFrame

class CheckbuttonDemo(EasyFrame):
    """Allows the user to place a restaurant order from a set of options."""
    def __init__(self):
        # Sets up the window and the widgets.
        EasyFrame.__init__(self, title = "Check Button Demo")

        # Add four check buttons
        self.chickCB = self.addCheckbutton(text = "Chicken", row = 0, column = 0)
        self.taterCB = self.addCheckbutton(text = "French Fries", row = 0, column = 1)
        self.beanCB = self.addCheckbutton(text = "Green Beans", row = 1, column = 0)
        self.sauceCB = self.addCheckbutton(text = "Applesauce", row = 1, column = 1)

        # Add the command button
        self.addButton(text = "Place Order", row = 2, column = 0, columnspan = 2, command = self.placeOrder)
        
    # Event handling method
    def placeOrder(self):
        """Display a message box with the roder information."""
        message = ""
        if self.chickCB.isChecked():
            message += "Chicken\n\n"
        if self.taterCB.isChecked():
            message += "French Fries\n\n"
        if self.beanCB.isChecked():
            message += "Green Beans\n\n"
        if self.sauceCB.isChecked():
            message += "Applesauce\n\n"
        # Do this only when no checkbuttons are selected
        if message == "":
            message = "No food ordered!"

        self.messageBox(title = "Customer Order", message = message)

# Definition of main() function
def main():
    CheckbuttonDemo().mainloop()

main()