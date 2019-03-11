import base64
import os

from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Tabs, RecipientViewRequest, TemplateRole, Text
from flask import Flask, request

from ds_config import DS_CONFIG

# Set FLASK_ENV to development if it is not already set
if 'FLASK_ENV' not in os.environ:
    os.environ['FLASK_ENV'] = 'development'


def get_api_client_by_jwt_authorization_flow():
    """
        This method create a ApiClient object and configure it using
        JWT authorization flow.
    """

    api_client = ApiClient()
    api_client.host = DS_CONFIG['base_path']

    # IMPORTANT NOTE:
    # the first time you ask for a JWT access token, you should grant access by making the following call
    # get DocuSign OAuth authorization url:
    oauth_login_url = api_client.get_jwt_uri(DS_CONFIG['integrator_key'], DS_CONFIG['redirect_uri'],
                                             DS_CONFIG['oauth_base_url'])
    # open DocuSign OAuth authorization url in the browser, login and grant access
    # web_browser.open_new_tab(oauth_login_url)
    print(oauth_login_url)
    # END OF NOTE

    # configure the ApiClient to asynchronously get an access token and store it
    api_client.configure_jwt_authorization_flow(DS_CONFIG['private_key_filename'], DS_CONFIG['oauth_base_url'],
                                                DS_CONFIG['integrator_key'], DS_CONFIG['user_admin_id'], 3600)

    return api_client


def get_api_client_by_access_token():
    """
        This method create a ApiClient object and configure it using
        Token Access Control.
    """

    api_client = ApiClient()
    api_client.host = DS_CONFIG['base_path']
    api_client.set_default_header("Authorization", "Bearer " + DS_CONFIG['access_token'])

    return api_client


def embedded_signing_ceremony():
    """
    The document <file_name> will be signed by <signer_name> via an
    embedded signing ceremony.
    """

    #
    # Step 1. Create and define the API Client.
    #

    api_client = get_api_client_by_jwt_authorization_flow()

    #
    # Step 2. The envelope definition is created.
    #         One signHere tab is added.
    #         The document path supplied is relative to the working directory
    #

    env_def = EnvelopeDefinition()
    env_def.email_subject = 'Sign the document needed to finish the loan process!!'
    env_def.template_id = DS_CONFIG['template_id']

    t_role = TemplateRole()
    t_role.role_name = DS_CONFIG['signer_role']
    t_role.name = DS_CONFIG['signer_name']
    t_role.email = DS_CONFIG['signer_email']
    t_role.client_user_id = DS_CONFIG['client_user_id']

    text_name = Text()
    text_name.tab_label = 'name'
    text_name.value = 'Jonathan'

    text_last_name = Text()
    text_last_name.tab_label = 'lastname'
    text_last_name.value = 'Vallejo'

    tabs = Tabs()
    tabs.text_tabs = [text_name, text_last_name]
    t_role.tabs = tabs

    env_def.template_roles = [t_role]
    env_def.status = DS_CONFIG['environment_status']
    
    #
    #  Step 3. Create/send the envelope.
    #
    #

    envelope_api = EnvelopesApi(api_client)
    envelope_summary = envelope_api.create_envelope(DS_CONFIG['account_id'], envelope_definition=env_def)
    envelope_id = envelope_summary.envelope_id

    print("Envelope {} has been sent to {} and the summary id: {}".format(envelope_id, t_role.email, envelope_summary))

    recipient_view_request = RecipientViewRequest(
        authentication_method=DS_CONFIG['authentication_method'], client_user_id=DS_CONFIG['client_user_id'],
        recipient_id='1', return_url=DS_CONFIG['app_url'] + '/ds_return?envelope_id={}'.format(envelope_id),
        user_name=DS_CONFIG['signer_name'], email=DS_CONFIG['signer_email']
    )

    results = envelope_api.create_recipient_view(DS_CONFIG['account_id'], envelope_id,
                                                 recipient_view_request=recipient_view_request)

    return results.url


# Mainline
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        url_doc_signed = embedded_signing_ceremony()
        return '''
    <html lang="en">
        <body>
            <form action="{url}" method="post">
                <input type="submit" value="Sign the document!"
                    style="width:13em;height:2em;background:#1f32bb;color:white;font:bold 1.5em arial;margin: 3em;"/>
                <iframe name="LendingFront" src="{url_doc_signed}" height="720" width="720"></iframe>
            </form>
        </body>
    </html>
                '''.format(url=request.url, url_doc_signed=url_doc_signed)
    else:
        return '''
    <html lang="en">
        <body>
            <form action="{url}" method="post">
                <input type="submit" value="Sign the document!"
                    style="width:13em;height:2em;background:#1f32bb;color:white;font:bold 1.5em arial;margin: 3em;"/>
            </form>
        </body>
    </html>
        '''.format(url=request.url)


@app.route('/ds_return', methods=['GET'])
def ds_return():
    print(request.args)
    envelope_id = request.args.get('envelope_id')

    api_client = get_api_client_by_jwt_authorization_flow()

    envelope_api = EnvelopesApi(api_client)
    docs_list = envelope_api.list_documents(DS_CONFIG['account_id'], envelope_id)

    print("EnvelopeDocumentsResult:\n{0}", docs_list)

    document_id = docs_list.envelope_documents[0].document_id

    data = envelope_api.get_document(DS_CONFIG['account_id'], document_id, envelope_id)
    print(data)

    with open(os.path.join(data), "rb") as document:
        content_bytes = document.read()
        base64_file_content = base64.b64encode(content_bytes).decode('ascii')

    print(base64_file_content)

    # <p>The signing ceremony was completed with status {event}</p>
    # <p>This page can also implement post-signing processing.</p>

    return '''
        <html lang="en">
            <body>
                <iframe name="LendingFront" src="data:application/pdf;base64, {file}" height="700" width="700"></iframe>
            </body>
        </html>          
    '''.format(event=request.args.get('event'), file=base64_file_content)


app.run(port=5001, debug=True)
