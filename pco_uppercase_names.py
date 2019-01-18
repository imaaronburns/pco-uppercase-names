import requests # you must install the python requests library before running http://docs.python-requests.org/en/master/user/install/
import json
import time

# change this to the number of church attendees in your Planning Center People account
numberofusers = 777

# https://api.planningcenteronline.com/oauth/applications to get your planning center application id and secret key
planning_center_activity_id='c743bf00cbhh1348574fbebcfab'      # example 'c743bf0cbhh13d55b9649944fbebcfab'
planning_center_secret='baf8544a1c23423aabce1e32cdc9ae89'      # example  'baf854a1c23426585fs0d41eabbcef2b1e32cdc9ae89'

offsetnumber = 0 # leave at 0 to start from the beginning of your list
per_page = 100  # acceptable values are 1-100, 100 is the max amount of names you can call at a time and makes the script run the quickest


# ----------------------------------


def getPlanningCenter(url):
    # get from planning center
    stuff2= requests.get(url, auth=(planning_center_activity_id, planning_center_secret))
    data=json.loads(stuff2.text)
    return data

def updatePlanningCenter(url,jsonData):
    # update planning center
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    data=requests.patch(url,auth=(planning_center_activity_id, planning_center_secret), data=json.dumps(jsonData),headers=headers )
    return data

def renameuppercase(offsetnumber,per_page):
    name_url='https://api.planningcenteronline.com/people/v2/people?order=last_name&offset={}&per_page={}'.format(offsetnumber,per_page)
    data=getPlanningCenter(name_url)
    for row in data['data']:
        unsurefirstname = row['attributes']['first_name']
        unsurelastname = row['attributes']['last_name']

        if row['type']=='Person' and unsurefirstname[0].istitle()==False:
            if len(row['attributes']['first_name'])>=3:
                FirstLowerCaseLetter = unsurefirstname[0]
                RestOfFirstName = unsurefirstname[1:]
                FirstTitle = FirstLowerCaseLetter.title()
                CapitalizedFirstLetterName = FirstTitle+RestOfFirstName
                jsonData={"data":{"type":"Person","id":row['id'],"attributes":{"first_name":CapitalizedFirstLetterName}}}
                post_url='https://api.planningcenteronline.com/people/v2/people/{}'.format(row['id'])
                response=updatePlanningCenter(post_url,jsonData)
                print(response.status_code,CapitalizedFirstLetterName,row['attributes']['last_name'],'https://people.planningcenteronline.com/people/{}'.format(row['id']))
            else:
                print('3FC {fir} {las}'.format(fir=row['attributes']['first_name'], las=row['attributes']['last_name']),'https://people.planningcenteronline.com/people/{}'.format(row['id']))

        if row['type']=='Person' and unsurelastname[0].istitle()==False:
            if len(row['attributes']['last_name'])>=3:
                LastLowerCaseLetter = unsurelastname[0]
                RestOfLastName = unsurelastname[1:]
                LastTitle = LastLowerCaseLetter.title()
                CapitalizedLastLetterName = LastTitle+RestOfLastName
                jsonData={"data":{"type":"Person","id":row['id'],"attributes":{"last_name":CapitalizedLastLetterName}}}
                post_url='https://api.planningcenteronline.com/people/v2/people/{}'.format(row['id'])
                response=updatePlanningCenter(post_url,jsonData)
                print(response.status_code,row['attributes']['first_name'],CapitalizedLastLetterName,'https://people.planningcenteronline.com/people/{}'.format(row['id']))
            else:
                print('3LC {fir} {las}'.format(fir=row['attributes']['first_name'], las=row['attributes']['last_name']),'https://people.planningcenteronline.com/people/{}'.format(row['id']))


while offsetnumber < numberofusers:
    renameuppercase(offsetnumber,per_page)
    offsetnumber = offsetnumber + per_page
    print("Finished with the first",offsetnumber, "people!")
    time.sleep(2) # sleep between json pulls so that you don't exceed the rate limit of 100 per 20 seconds, however unlikely it may be
