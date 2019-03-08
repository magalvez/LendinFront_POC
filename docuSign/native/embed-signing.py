# Python3 Quick start example: embedded signing ceremony.
# Copyright (c) 2018 by DocuSign, Inc.
# License: The MIT License -- https://opensource.org/licenses/MIT

import base64, os
from flask import Flask, request, redirect
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Tabs, Recipients, Document, RecipientViewRequest, CustomFields, TextCustomField, TemplateRole
import docusign_esign as docusign

# Settings
# Fill in these constants
#
# Obtain an OAuth access token from https://developers.hqtest.tst/oauth-token-generator
access_token = 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQkAAAABAAUABwCArM1O1KPWSAgAgOzwXBek1kgCALk7xTqm_V1Akk8CFOmsnOEVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjBmMjdmMGUtODU3ZC00YTcxLWE0ZGEtMzJjZWNhZTNhOTc4MAAAmS1w0qPWSDcAxAkY_dTa20i_b-JSx4oGpA.vHIY03CiNytv6gKJ9bw3o8Gx_i8CcAP9KrgBTV1ars0pHR8kgDIvZ-ovW1rwfjKC8NbYVuOSjIuAqo_cWwAik0m3Hisaf-77rPnUlT2bC-N8im4Fm-B0Wzd-f4vYNSfcqnIKjf7bCb3tMkwDNgQbagvNRAPbwIpBVCZwNaWgZMVBvVPktkbP2FKNbBg3iIqlP2NxrlSEzW4lIAVTaHRbQ5EFcTO8rdX_Y0CO-N1zGYAoP4bFs6hXwJtPom-iDjnRTydkJBoxmAMELOCZVTqshiLy0Egj5rTxpJrx-LYFGcKOP5X8oHguLzCpucMRt5y8XXGy5AH4hOYN5n6fkwkrhw'

# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture. 
account_id = '8063857'

# Recipient Information:
signer_name = 'Manuel Alejandro Galvez'
signer_email = 'manuel@lendingfront.com'

# The document you wish to send. Path is relative to the root directory of this repo.
file_name_path = 'demo_documento/test.pdf'

# The url of this web application
base_url = 'http://localhost:5001'
client_user_id = '123' # Used to indicate that the signer will use an embedded
                       # Signing Ceremony. Represents the signer's userId within
                       # your application.
authentication_method = 'None' # How is this application authenticating
                               # the signer? See the `authenticationMethod' definition
                               # https://developers.docusign.com/esign-rest-api/reference/Envelopes/EnvelopeViews/createRecipient

# The API base_path
base_path = 'https://demo.docusign.net/restapi'

# Set FLASK_ENV to development if it is not already set
if 'FLASK_ENV' not in os.environ:
    os.environ['FLASK_ENV'] = 'development'

# Constants
APP_PATH = os.path.dirname(os.path.abspath(__file__))

def embedded_signing_ceremony():
    """
    The document <file_name> will be signed by <signer_name> via an
    embedded signing ceremony.
    """

    #
    # Step 1. The envelope definition is created.
    #         One signHere tab is added.
    #         The document path supplied is relative to the working directory
    #
    '''with open(os.path.join(APP_PATH, file_name_path), "rb") as file:
        content_bytes = file.read()'''
    base64_file_content = '' #base64.b64encode(content_bytes).decode('ascii')

    # Create the document model
    '''document = Document( # create the DocuSign document object 
        document_base64 = base64_file_content, 
        name = 'Example document', # can be different from actual file name
        file_extension = 'pdf', # many different document types are accepted
        document_id = 1 # a label used to reference the doc
    )'''

    '''text_field = docusign.Text(
        tab_label='name',  # tab_label must exactly match the field you created in the Docusign GUI
        value='Manuel'  # value, as far as I can tell, must be a string.
    )

    docusign.Tabs(text_tabs=[text_field])'''

    patient_first_name = TextCustomField(name='name', value='Allen', show='true',
                                         required='false')
    patient_last_name = TextCustomField(name='lastname', value='Elks', show='true',
                                        required='false')
    custom_fields = CustomFields(text_custom_fields=[patient_first_name, patient_last_name])

    # envelope_definition.custom_fields = custom_fields


    # Custome fields
    custom_fields_old = CustomFields(
        ['name'],
        ['Manuel']
    )

    # Create the signer recipient model 
    signer = Signer( # The signer
        email = signer_email, name = signer_name, recipient_id = "1", routing_order = "1",
        client_user_id = client_user_id, # Setting the client_user_id marks the signer as embedded
    )

    # Create a sign_here tab (field on the document)
    sign_here = SignHere( # DocuSign SignHere field/tab
        document_id = '1', page_number = '3', recipient_id = '1', tab_label = 'SignHereTab',
        x_position = '175', y_position = '320')


    # Add the tabs model (including the sign_here tab) to the signer
    signer.tabs = Tabs(sign_here_tabs = [sign_here]) # The Tabs object wants arrays of the different field/tab types

    # Next, create the top level envelope definition and populate it.
    '''envelope_definition = EnvelopeDefinition(
        email_subject = "Please sign this document sent from the Python SDK",
        documents = [document], # The order in the docs array determines the order in the envelope
        recipients = Recipients(signers = [signer]), # The Recipients object wants arrays for each recipient type
        status = "sent", # requests that the envelope be created and sent.
        custom_fields = custom_fields
    )'''

    envDef = EnvelopeDefinition()
    envDef.email_subject = 'PLEASE GOD HELP ME, I NEED THIS WORKING!!'
    envDef.template_id = 'd5e617be-da0a-4431-9014-4575282f61d4'

    tRole = TemplateRole()
    tRole.role_name = 'Manager'
    tRole.name = 'Manuel Alejandro Galvez'
    tRole.email = 'manuel@lendingfront.com'

    envDef.template_roles = [tRole]
    envDef.status = 'sent'
    envDef.custom_fields = custom_fields
    
    #
    #  Step 2. Create/send the envelope.
    #
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    results = envelope_api.create_envelope(account_id, envelope_definition=envDef)

    #
    # Step 3. The envelope has been created.
    #         Request a Recipient View URL (the Signing Ceremony URL)
    #
    envelope_id = results.envelope_id
    recipient_view_request = RecipientViewRequest(
        authentication_method = authentication_method, client_user_id = client_user_id,
        recipient_id = '1', return_url = base_url + '/dsreturn',
        user_name = signer_name, email = signer_email
    )

    results = envelope_api.create_recipient_view(account_id, envelope_id)
        #recipient_view_request = recipient_view_request)
    
    #
    # Step 4. The Recipient View URL (the Signing Ceremony URL) has been received.
    #         Redirect the user's browser to it.
    #
    return results.url


# Mainline
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        return redirect(embedded_signing_ceremony(), code=302)
    else:
        return '''
            <html lang="en"><body><form action="{url}" method="post">
            <input type="submit" value="Sign the document!"
                style="width:13em;height:2em;background:#1f32bb;color:white;font:bold 1.5em arial;margin: 3em;"/>
            </form></body>
        '''.format(url=request.url)


@app.route('/dsreturn', methods=['GET'])
def dsreturn():
    return '''
        <html lang="en"><body><p>The signing ceremony was completed with
          status {event}</p>
          <p>This page can also implement post-signing processing.</p></body>
    '''.format(event=request.args.get('event'))

app.run(port=5001)
