# Ryan W (https://github.com/onlinePB)
# URL Opener (https://github.com/onlinePB/URL_Opener)
# Version 1.0.0

import webbrowser
import sys

# Try to open the file
try:
    urls = open("urls.txt", "r")
except FileNotFoundError:
    print("ERROR: urls.txt not found.")
    input("Press enter to continue...")
    sys.exit()

# Open URLs
for line in urls:
    webbrowser.open(line, new=0, autoraise=True)

# Close the file
urls.close()
