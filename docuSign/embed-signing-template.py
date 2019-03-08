import os
from flask import Flask, request
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Tabs, TemplateRole, Text, Title

# Settings
#
# Obtain an OAuth access token from https://developers.hqtest.tst/oauth-token-generator
access_token = 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQkAAAABAAUABwCAljUsyKPWSAgAgNZYOguk1kgCALk7xTqm_V1Akk8CFOmsnOEVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjBmMjdmMGUtODU3ZC00YTcxLWE0ZGEtMzJjZWNhZTNhOTc4MACAlP7Tx6PWSDcAxAkY_dTa20i_b-JSx4oGpA.1gu3gjsm7tWzqQZuOEzLjc78zrXtWZA_jQ1CngBgrrMWA_hkJhyVEdvLbpnxNIoQvJ4terxn2sL5nWlifS-_kdom1tvKp7_1gdTUJ-TOtWaxuoTBr3GHfpCTw14DM_1vslx_iqdxOpJOIzc9r862oZOQmcwIuVH7WPdK_sgXQtLbiGav5q9Q3RIyUPQiQE5vpxAP7E29WggP8OzbjitCWOKDTxoAhavZZgfh5Sp5tuHVEiC14NJaTimjboOzFq2kmrLefHIEtUBWomcOrNd7xohxEbT6OFq7wLemzK7l095_v2QWlpZmJ22dheoKMJhZ5SLaBwD6MoIFzPI5szxHiA'

# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture.
account_id = '8063857'

# Random number to be assigned to the client
client_user_id = '1091'

# Base URL to be returned after finish the sign
base_url = 'http://localhost:5001'

# The API base_path
base_path = 'https://demo.docusign.net/restapi'

# The Template ID
template_id = 'd5e617be-da0a-4431-9014-4575282f61d4'

# User and role configuration
role_name = 'Manager'
user_name = 'LendingFront'
user_email = 'lendingfront@mailinator.com'

# Environment configuration
environment_status = 'sent'

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
    env_def.template_id = template_id

    t_role = TemplateRole()
    t_role.role_name = role_name
    t_role.name = user_name
    t_role.email = user_email
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
    env_def.status = environment_status

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


app.run(port=5001, debug=True)
