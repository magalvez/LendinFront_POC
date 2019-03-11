import os
from flask import Flask, request
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Tabs, RecipientViewRequest, CustomFields, TextCustomField, TemplateRole, Text, Title


# Settings
#
# Obtain an OAuth access token from https://developers.hqtest.tst/oauth-token-generator
access_token = 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQkAAAABAAUABwCArM1O1KPWSAgAgOzwXBek1kgCALk7xTqm_V1Akk8CFOmsnOEVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjBmMjdmMGUtODU3ZC00YTcxLWE0ZGEtMzJjZWNhZTNhOTc4MAAAmS1w0qPWSDcAxAkY_dTa20i_b-JSx4oGpA.vHIY03CiNytv6gKJ9bw3o8Gx_i8CcAP9KrgBTV1ars0pHR8kgDIvZ-ovW1rwfjKC8NbYVuOSjIuAqo_cWwAik0m3Hisaf-77rPnUlT2bC-N8im4Fm-B0Wzd-f4vYNSfcqnIKjf7bCb3tMkwDNgQbagvNRAPbwIpBVCZwNaWgZMVBvVPktkbP2FKNbBg3iIqlP2NxrlSEzW4lIAVTaHRbQ5EFcTO8rdX_Y0CO-N1zGYAoP4bFs6hXwJtPom-iDjnRTydkJBoxmAMELOCZVTqshiLy0Egj5rTxpJrx-LYFGcKOP5X8oHguLzCpucMRt5y8XXGy5AH4hOYN5n6fkwkrhw'

# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture.
account_id = '8063857'

# Random number to be assigned to the client
client_user_id = '2'

# Base URL to be returned after finish the sign
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

    env_def = EnvelopeDefinition()
    env_def.email_subject = 'PLEASE GOD HELP ME, I NEED THIS WORKING!!'
    # env_def.template_id = 'd5e617be-da0a-4431-9014-4575282f61d4'
    env_def.template_id = '57e2a00c-b8b5-415c-8c8b-db31d75e8253'

    t_role = TemplateRole()
    t_role.role_name = 'Cliente'
    t_role.name = 'Alejandro Galvez'
    t_role.email = 'galvez.alejo@gmail.com'
    t_role.client_user_id = client_user_id

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
    t_role.tabs = tabs

    env_def.template_roles = [t_role]
    env_def.status = 'sent'

    #
    #  Step 2. Create/send the envelope.
    #
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    envelope_summary = envelope_api.create_envelope(account_id, envelope_definition=env_def)
    envelope_id = envelope_summary.envelope_id

    print("Envelope {} has been sent to {}".format(envelope_id, t_role.email))

    ''''
    recipient_view_request = RecipientViewRequest(
        authentication_method='None', client_user_id=client_user_id,
        recipient_id='1', return_url=base_url + '/dsreturn',
        user_name='Lending Front', email='lendingfrontdocu@mailinator.com'
    )

    results = envelope_api.create_recipient_view(account_id, envelope_id, recipient_view_request=recipient_view_request)

    return results.url
    '''

    return ''


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
