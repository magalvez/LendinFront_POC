# Python3 Quick start example: embedded signing ceremony.
# Copyright (c) 2018 by DocuSign, Inc.
# License: The MIT License -- https://opensource.org/licenses/MIT

import base64, os
from flask import Flask, request, redirect
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Tabs, Recipients, Document, RecipientViewRequest, CustomFields, TextCustomField, TemplateRole, TemplatesApi as templateApi, ListCustomField, ListItem, Text, Title
import docusign_esign as docusign

# Settings
# Fill in these constants
#
# Obtain an OAuth access token from https://developers.hqtest.tst/oauth-token-generator
access_token = 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQkAAAABAAUABwCAljUsyKPWSAgAgNZYOguk1kgCALk7xTqm_V1Akk8CFOmsnOEVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjBmMjdmMGUtODU3ZC00YTcxLWE0ZGEtMzJjZWNhZTNhOTc4MACAlP7Tx6PWSDcAxAkY_dTa20i_b-JSx4oGpA.1gu3gjsm7tWzqQZuOEzLjc78zrXtWZA_jQ1CngBgrrMWA_hkJhyVEdvLbpnxNIoQvJ4terxn2sL5nWlifS-_kdom1tvKp7_1gdTUJ-TOtWaxuoTBr3GHfpCTw14DM_1vslx_iqdxOpJOIzc9r862oZOQmcwIuVH7WPdK_sgXQtLbiGav5q9Q3RIyUPQiQE5vpxAP7E29WggP8OzbjitCWOKDTxoAhavZZgfh5Sp5tuHVEiC14NJaTimjboOzFq2kmrLefHIEtUBWomcOrNd7xohxEbT6OFq7wLemzK7l095_v2QWlpZmJ22dheoKMJhZ5SLaBwD6MoIFzPI5szxHiA'

# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture. 
account_id = '8063857'

client_user_id = '1091'
base_url = 'http://localhost:5001'

# The API base_path
base_path = 'https://demo.docusign.net/restapi'

# Set FLASK_ENV to development if it is not already set
if 'FLASK_ENV' not in os.environ:
    os.environ['FLASK_ENV'] = 'development'


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

    envDef = EnvelopeDefinition()
    envDef.email_subject = 'PLEASE GOD HELP ME, I NEED THIS WORKING!!'
    envDef.template_id = 'd5e617be-da0a-4431-9014-4575282f61d4'

    tRole = TemplateRole()
    tRole.role_name = 'Manager'
    tRole.name = 'Lending Front'
    tRole.email = 'lendingfrontdocu@mailinator.com'
    tRole.client_user_id = client_user_id

    text_example = Text()
    text_example.tab_label = 'example'
    text_example.value = 'SIIII GRACIAS DIOS!! -- EXAMPLE'

    text_name = Text()
    text_name.tab_label = 'name'
    text_name.value = 'SIIII GRACIAS DIOS!! -- NAME'

    text_name2 = Text()
    text_name2.tab_label = 'name2'
    text_name2.value = 'SIIII GRACIAS DIOS!! -- NAME2'

    text = Text()
    text.document_id = '1'
    text.page_number = '1'
    text.recipient_id = '1'
    text.x_position = '100'
    text.y_position = '100'
    text.scale_value = '0.5'
    text.value = 'THANKS GOD!!'

    title_label = Title()
    title_label.tab_label = 'lablel_example'
    title_label.value = 'LendingFront'

    tabs = Tabs()
    tabs.text_tabs = [text_example, text_name, text_name2, text]
    tabs.title_tabs = [title_label]
    tRole.tabs = tabs

    envDef.template_roles = [tRole]
    envDef.status = 'sent'

    name = TextCustomField(field_id='name', name='name', value='Manuel')
    last_name = TextCustomField(field_id='lastname', name='lastname', value='Galvez')
    testing = TextCustomField(field_id='testing', name='testing', value='Elks')
    manu = TextCustomField(field_id='manu', name='manu', value='manu')
    example = TextCustomField(field_id='example', name='example', value='Siiiiiiii')

    '''item_name = ListItem(text='name', value='Allen')
    item_lastname = ListItem(text='lastname', value='Galvez')
    item_testing = ListItem(text='testing', value='testing')
    item_manu = ListItem(text='manu', value='manu')

    listcf = ListCustomField(list_items=[item_name, item_lastname, item_testing, item_manu])'''

    custom_fields = CustomFields(text_custom_fields=[example, name, last_name, testing, manu])

    envDef.custom_fields = custom_fields
    # envDef.recipients

    #
    print('*&**&*^&*&^%$#$%^&*(*&^%$#@!@#$%^&')
    print('')
    
    #
    #  Step 2. Create/send the envelope.
    #
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    envelopeSummary = envelope_api.create_envelope(account_id, envelope_definition=envDef)
    envelope_id = envelopeSummary.envelope_id

    print("Envelope {} has been sent to {}".format(envelope_id, tRole.email))

    '''client_user_id = '2939'


    return_url = 'http://www.docusign.com/developer-center'
    recipient_view_request = docusign.RecipientViewRequest()
    recipient_view_request.return_url = return_url
    recipient_view_request.client_user_id = client_user_id
    recipient_view_request.authentication_method = 'email'
    recipient_view_request.user_name = 'Manuel Galvez'
    recipient_view_request.email = 'manuel@lendingfront.com'

    view_url = envelope_api.create_recipient_view(account_id, envelope_id, recipient_view_request=recipient_view_request) '''

    recipient_view_request = RecipientViewRequest(
        authentication_method='None', client_user_id=client_user_id,
        recipient_id='1', return_url=base_url + '/dsreturn',
        user_name='Lending Front', email='lendingfrontdocu@mailinator.com'
    )

    results = envelope_api.create_recipient_view(account_id, envelope_id, recipient_view_request=recipient_view_request)

    return results.url


# Mainline
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        return '' + embedded_signing_ceremony()
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
