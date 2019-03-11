import sys
import docuSign.chilkat
# import requests

# url = 'https://demo.docusign.net/restapi/v2/login_information'
# data = '{  "platform": {    "login": {      "userName": "name",      "password": "pwd"    }  } }'

# response = requests.get(url)  # , data=data,headers={"Content-Type": "application/json",
                            #                     "X-DocuSign-Authentication" : "{ \"Username\":\"manuel@lendingfront.com\",  \"Password\":\"l3nd1ngfr0nt\",  \"IntegratorKey\":\"29088eac-3cd3-44e5-8aae-03bcb7287b3f\" }" })
# print(response)
# sid = response.json()['platform']['login']['sessionId']   # to extract the detail from response
# print(response.text)
# print(sid)


glob = docuSign.chilkat.CkGlobal()
success = glob.UnlockBundle("Anything for 30-day trial")
if (success != True):
    print(glob.lastErrorText())
    sys.exit()

status = glob.get_UnlockStatus()
if (status == 2):
    print("Unlocked using purchased unlock code.")
else:
    print("Unlocked in trial mode.")

rest = docuSign.chilkat.CkRest()
# ok = rest.UnlockBundle("Anything for 30-day trial")
#  URL: https://demo.docusign.net/restapi/v2/login_information
bTls = True
port = 443
bAutoReconnect = True
success = rest.Connect("demo.docusign.net",port,bTls,bAutoReconnect)
if (success != True):
    print("ConnectFailReason: " + str(rest.get_ConnectFailReason()))
    print(rest.lastErrorText())
    sys.exit()

rest.AddHeader("X-DocuSign-Authentication","{ \"Username\":\"manuel@lendingfront.com\",  \"Password\":\"l3nd1ngfr0nt\",  \"IntegratorKey\":\"29088eac-3cd3-44e5-8aae-03bcb7287b3f\" }")

sbResponseBody = docuSign.chilkat.CkStringBuilder()
success = rest.FullRequestNoBodySb("GET","/restapi/v2/login_information",sbResponseBody)
if (success != True):
    print(rest.lastErrorText())
    sys.exit()

respStatusCode = rest.get_ResponseStatusCode()
if (respStatusCode >= 400):
    print("Response Status Code = " + str(respStatusCode))
    print("Response Header:")
    print(rest.responseHeader())
    print("Response Body:")
    print(sbResponseBody.getAsString())
    sys.exit()

jsonResponse = docuSign.chilkat.CkJsonObject()
jsonResponse.LoadSb(sbResponseBody)

i = 0
count_i = jsonResponse.SizeOfArray("loginAccounts")
while i < count_i :
    jsonResponse.put_I(i)
    name = jsonResponse.stringOf("loginAccounts[i].name")
    accountId = jsonResponse.stringOf("loginAccounts[i].accountId")
    baseUrl = jsonResponse.stringOf("loginAccounts[i].baseUrl")
    isDefault = jsonResponse.stringOf("loginAccounts[i].isDefault")
    userName = jsonResponse.stringOf("loginAccounts[i].userName")
    userId = jsonResponse.stringOf("loginAccounts[i].userId")
    email = jsonResponse.stringOf("loginAccounts[i].email")
    siteDesc = jsonResponse.stringOf("loginAccounts[i].siteDescription")

    print('This is the login information: '
          '\n\tname             = {}, '
          '\n\taccountId        = {}, '
          '\n\tbaseUrl          = {}, '
          '\n\tisDefault        = {},'
          '\n\tuserName         = {},'
          '\n\tuserId           = {},'
          '\n\temail            = {},'
          '\n\tsiteDescription  = {}'.format(name, accountId, baseUrl, isDefault, userName, userId, email, siteDesc))
    i = i + 1
