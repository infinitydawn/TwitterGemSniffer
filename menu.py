from consolemenu import *
from consolemenu.items import *
import scrape

# Create the menu
menu = ConsoleMenu("Twitter Gem Sniffer", "Choose From The Following Functions")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
func1 = FunctionItem("Get First % Users Of Account", scrape.getTopPercent)
func2 = FunctionItem("Get User List Intersection", scrape.calculateIntersections, args=[False, []])
func3 = FunctionItem("Get Followers From The List", scrape.getFollowers)
func4 = FunctionItem("Get Whom Users are Following From The List", scrape.getFollowing, args=[False])
func5 = FunctionItem("Compare Users From One list To Users In Multiple Lists One by One", scrape.compareLists)
func6 = FunctionItem("Monitor Following List", scrape.monitorList)
#func4 = FunctionItem("Get First 10% Users Of Account", scrape.getTopPercent)

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu([func1, func2, func3])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Bot Functions", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(func1)
menu.append_item(func2)
menu.append_item(func3)
menu.append_item(func4)
menu.append_item(func5)
menu.append_item(func6)
#menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()