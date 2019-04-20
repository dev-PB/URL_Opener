# Ryan W (https://github.com/onlinePB)
# URL Opener (https://github.com/onlinePB/URL_Opener)
# Version 1.0.0

import webbrowser
import sys

print("URLOpener version 1.0.0 (https://github.com/onlinePB/URL_Opener)\nBy Ryan W (https://github.com/onlinePB)")

# Try to open the file
try:
    urls = open("urls.txt", "r")
except FileNotFoundError:
    print("\nERROR: urls.txt not found.\nIs this a bug? Report it here: https://github.com/onlinePB/URL_Opener/issues")
    input("Press enter to continue...")
    sys.exit()

# Open URLs
for line in urls:
    webbrowser.open(line, new=0, autoraise=True)

# Close the file
urls.close()
