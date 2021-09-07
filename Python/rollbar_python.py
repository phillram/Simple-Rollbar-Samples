####################################################################
# Simple Rollbar setup using Python
####################################################################

###################################################################
# Imports that are good to use
###################################################################
import rollbar, os, sys

###################################################################
# Place your access token here ('post' or 'client' scope as noted)
# If not set explicity, then check if it is set as an environment variable 
###################################################################
POST_SERVER_ITEM_ACCESS_TOKEN = ''

if POST_SERVER_ITEM_ACCESS_TOKEN:
    print('Token is set')
elif os.environ['PROJECT_POST_SERVER_ITEM_TOKEN']:
    POST_SERVER_ITEM_ACCESS_TOKEN = os.environ['PROJECT_POST_SERVER_ITEM_TOKEN']
    print('Token is set in the environment')
else:
    print('No token found')

###################################################################
# Rollbar configuration
###################################################################
rollbar.init(
    # Required configuration
    ############################
    access_token = POST_SERVER_ITEM_ACCESS_TOKEN,
    environment = 'Tester',
    
    # Optional configuration
    ############################
    # enabled = 'False', # Turns off Rollbar reporting
    # code_version = '', # Set your code version here
    # root = '',  # Root of your application
    # capture_ip = 'True', # Capture client requst IP
    # capture_email = 'True', # Capture client requst email
    # capture_username = 'True', # Capture client requst username
    # timeout = 3, # Rollbar API timeout length in seconds
    # endpoint = 'https://api.rollbar.com/api/1/item/', # Change the Rollbar API endpoint
    )

# Vanilla Python requires the following override to report uncaught exceptions
def rollbar_excepthook(exc_type, exc_value, traceback):
    # Report the issue to rollbar:
    rollbar.report_exc_info((exc_type, exc_value, traceback))
    # Display the error normally:
    sys.__excepthook__(exc_type, exc_value, traceback)
sys.excepthook = rollbar_excepthook


###################################################################
# Running a function to encounter an error
###################################################################

# A function which combines two strings together.
# Reports to Rollbar if the first string has two characters and the second has five
def combine_strings(i, j):
    if len(i) == 2:
        rollbar.report_message(str(i) + ' has two characters', 'error')
    if len(j) == 5:
        rollbar.report_message(str(j) + ' has five characters', 'error')
    return i + j

# Run the function with a five character second word. Shows a caught exception.
combine_strings('hello', 'world')
# Run the function with incorrect parameters. Shows an uncaught exception.
combine_strings('hello')