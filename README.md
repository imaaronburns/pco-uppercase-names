# pco-uppercase-names
Changes the first and last names of every user in your Planning Center account to start with an uppercase letter.


### To Use:
1. Install the python requests library » http://docs.python-requests.org/en/master/user/install/
2. Change the Planning Center API Activity ID and Secret Key » https://api.planningcenteronline.com/oauth/applications
3. Change the number of church attendees in your Planning Center account. This number can be found on your People dashboard.


This script automatically changes the first and last letters of names to be uppercase letters.

For example:
"ronda mcCarley" becomes "Ronda McCarley"

If a name is shorter than 3 letters, the name is not checked.

I understand that there are some cases where some names would intentionally want to start with a lowercase letter (e.g. van Wieren, del Ray).
I have not accounted for those names. If you run the script, you would need to manually change those names back.

Most of the credit for this script belongs to Jerome Myers and his PCO Gender API Script.
Find it at:
https://github.com/jeromemyers02/planning_center_gender_api_script
