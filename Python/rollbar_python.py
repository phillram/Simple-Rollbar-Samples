####################################################################
# Simple Rollbar setup using Python
####################################################################

###################################################################
# Imports that are good to use
###################################################################
import rollbar, os




if os.environ['PROJECT_POST_SERVER_ITEM_TOKEN']:
    print('yo! It is here')
else:
    print('No go Joe')


# command_executor='https://'+os.environ['SAUCE_USERNAME']+':'+os.environ['SAUCE_ACCESS_KEY']+'@ondemand.saucelabs.com:443/wd/hub',