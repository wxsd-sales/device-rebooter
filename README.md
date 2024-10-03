
# Device Rebooter
Reboot workspace devices that have been granted access to a Webex bot!

<!-- ![image/gif](insert img link here) -->


## Overview

This application uses Cloud xAPI commands to reboot the devices the bot has access to.




## Setup

### Prerequisites & Dependencies: 

1. A Webex Bot is required.  You can create a Bot [here](https://developer.webex.com/my-apps/new) (login with Webex account required).  
+ Give it any name, icon, and description.  
+ Once created, a new token is generated.  **Copy it somewhere secure - you will need it in the next steps.**

2. The bot must be added to each workspace you wish to reboot in Control Hub.  An admin can login to Control Hub (admin.webex.com), select each desired workspace and then click "Edit API Access".

3. Clone this repository.
4. Navigate to the root directory of this repo on your local machine, and create a file called ```.env```  
The ```.env``` file must contain the following line:
```
BOT_TOKEN=""
```
Place the Bot token you copied in step 1 between the double quotes above.


### Installation Steps:
+ python >= v3.8.1
+ [pip](https://pip.pypa.io/en/stable/installation/) required
+ With pip installed, run these commands from the command line/terminal:
```
pip install aiohttp
pip install python-dotenv
```


#### Run
**Open a command prompt or terminal.**  If you simply double click the process, the command prompt will close if it reaches any unexpected errors, and you will **not see the reason for the failure**.

Once you have opened a terminal, navigate to the source directory, then run:  
```python device-rebooter.py```


## Demo
*For more demos & PoCs like this, click [here](https://github.com/wxsd-sales).

<!-- [![Your Video Title ](assets/peer_support_main.PNG)](https://www.youtube.com/watch?v=SqZhiC8jHhU&t=10s, "<insert demo name here>") -->


## License
All contents are licensed under the MIT license. Please see [license](LICENSE) for details.


## Disclaimer
Everything included is for demo and Proof of Concept purposes only. Use of the site is solely at your own risk. This site may contain links to third party content, which we do not warrant, endorse, or assume liability for. These demos are for Cisco Webex usecases, but are not Official Cisco Webex Branded demos.


## Questions
Please contact the WXSD team at [wxsd@external.cisco.com](mailto:wxsd@external.cisco.com?subject=DeviceRebooter) for questions. Or, if you're a Cisco internal employee, reach out to us on the Webex App via our bot (globalexpert@webex.bot). In the "Engagement Type" field, choose the "API/SDK Proof of Concept Integration Development" option to make sure you reach our team. 
