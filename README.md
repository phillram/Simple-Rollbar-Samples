# Simple-Rollbar-Samples

This is intended to be a collection of very simple code samples to demonstrate how to set up and use Rollbar.
Each main SDK language will be encapsulated within it's folder.


## Setting the Rollbar API Key (Access Token)
These scripts will use the following environment variables:
- `PROJECT_POST_CLIENT_ITEM_TOKEN`
- `PROJECT_POST_SERVER_ITEM_TOKEN`

These are to have the value of the respective `Server` or `Client` tokens. These will be used to communicate with Rollbar to record your messages. Both of these are used in the various Rollbar SDKs. Depending on your lanaguage you may only need one of them. 

### You can find your project tokens by:
- Clicking to the `Settings` icon on the left sidebar
- Selecting your project (if you have multiple)
- Clicking on `Project Access Tokens`

