import sys
import chilkat

glob = chilkat.CkGlobal()
success = glob.UnlockBundle("Anything for 30-day trial")
if (success != True):
    print(glob.lastErrorText())
    sys.exit()

status = glob.get_UnlockStatus()
if (status == 2):
    print("Unlocked using purchased unlock code.")
else:
    print("Unlocked in trial mode.")

rest = chilkat.CkRest()

#  URL: https://demo.docusign.net/restapi/v2/accounts/4750109/envelopes
bTls = True
port = 443
bAutoReconnect = True
success = rest.Connect("demo.docusign.net",port,bTls,bAutoReconnect)
if (success != True):
    print("ConnectFailReason: " + str(rest.get_ConnectFailReason()))
    print(rest.lastErrorText())
    sys.exit()

json = chilkat.CkJsonObject()
json.UpdateString("emailSubject","DocuSign REST API Quickstart Sample")
json.UpdateString("emailBlurb","Shows how to create and send an envelope from a document.")
json.UpdateString("recipients.signers[0].email","sally.smith@example.com")
json.UpdateString("recipients.signers[0].name","Sally Smith")
json.UpdateString("recipients.signers[0].recipientId","1")
json.UpdateString("recipients.signers[0].routingOrder","1")
json.UpdateString("documents[0].documentId","d5e617be-da0a-4431-9014-4575282f61d4")
json.UpdateString("documents[0].name","test.pdf")
json.UpdateString("documents[0].documentBase64","base64_encoded_document_bytes")
json.UpdateString("status","sent")

rest.AddHeader("X-DocuSign-Authentication","{ \"Username\":\"manuel@lendingfront.com\",  \"Password\":\"l3nd1ngfr0nt\",  \"IntegratorKey\":\"29088eac-3cd3-44e5-8aae-03bcb7287b3f\" }")
rest.AddHeader("Content-Type","application/json")
rest.AddHeader("Accept","application/json")

sbRequestBody = chilkat.CkStringBuilder()
json.EmitSb(sbRequestBody)
sbResponseBody = chilkat.CkStringBuilder()
success = rest.FullRequestSb("POST","/restapi/v2/accounts/8063857/envelopes",sbRequestBody,sbResponseBody)
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

jsonResponse = chilkat.CkJsonObject()
jsonResponse.LoadSb(sbResponseBody)

envelopeId = jsonResponse.stringOf("envelopeId")
uri = jsonResponse.stringOf("uri")
statusDateTime = jsonResponse.stringOf("statusDateTime")
status = jsonResponse.stringOf("status")