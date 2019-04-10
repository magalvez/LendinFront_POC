import base64
import os

from EncryptionHelper import AESCipher

from jwcrypto import jwk

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

    #
    # Using Crypto to encrypt and decrypt the as example the id RSA key
    #
    cyfrer = AESCipher()

    api_client = ApiClient()
    api_client.host = DS_CONFIG['base_path']

    # IMPORTANT NOTE:
    # the first time you ask for a JWT access token, you should grant access by making the following call
    # get DocuSign OAuth authorization url:
    oauth_login_url = api_client.get_jwt_uri(DS_CONFIG['integrator_key'], DS_CONFIG['redirect_uri'],
                                             DS_CONFIG['oauth_base_url'])

    # open DocuSign OAuth authorization url in the browser, login and grant access
    # web_browser.open_new_tab(oauth_login_url)
    # print(oauth_login_url)
    # END OF NOTE

    # configure the ApiClient to asynchronously get an access token and store it

    #
    # Get the application Path in case we are getting the id RSA from a file
    # otherwise the value passed on the method should be a empty string.
    #

    app_path_keys = os.path.dirname(os.path.abspath(__file__)).replace('stable', 'keys/')
    app_path_keys += DS_CONFIG['private_key_filename']

    #
    #   Getting the id RSA encrypted to be used by the JWT process
    #
    id_rsa = jwk.JWK.from_pem(cyfrer.decrypt(DS_CONFIG['id_rsa']))

    #
    # Call JWT Authorization and configure it into the API Client
    #

    api_client.configure_jwt_authorization_flow('', DS_CONFIG['oauth_base_url'],
                                                DS_CONFIG['integrator_key'],
                                                DS_CONFIG['user_admin_id'], 3600, key_bytes=id_rsa)

    return api_client


def get_api_client_by_access_token():
    """
        This method create a ApiClient object and configure it using
        Token Access Control.
    """

    #
    # Use Access Token Authorization and configure it into the API Client
    #

    api_client = ApiClient()
    api_client.host = DS_CONFIG['base_path']
    api_client.set_default_header("Authorization", "Bearer " + DS_CONFIG['access_token'])

    return api_client


def get_envelop_definition():

    env_def = EnvelopeDefinition()
    env_def.email_subject = 'Sign the document needed to finish the loan process!!'
    env_def.template_id = DS_CONFIG['template_id']

    return env_def


def generate_template_role_business_owner():

    t_role = TemplateRole()
    t_role.role_name = 'Business Owner'
    t_role.name = 'Andres Vasquez'
    t_role.email = 'andres@lendinfront.com'
    t_role.client_user_id = '54657681'
    t_role.routing_order = '1'

    text_business_legal_name = Text()
    text_business_legal_name.tab_label = 'business_legal_name'
    text_business_legal_name.value = 'Farage Tree and Stump Removal, L.L.C.'

    text_dba = Text()
    text_dba.tab_label = 'dba'
    text_dba.value = 'Farage Tree and Stump Removal'

    text_business_address = Text()
    text_business_address.tab_label = 'business_address'
    text_business_address.value = '9309 Northeast Paw Paw Drive, Kansas City, MO, 64157'

    text_state_of_incorporation = Text()
    text_state_of_incorporation.tab_label = 'state_of_incorporation'
    text_state_of_incorporation.value = 'MO'

    text_business_owner_1_first_last_name = Text()
    text_business_owner_1_first_last_name.tab_label = 'business_owner_1_first_last_name'
    text_business_owner_1_first_last_name.value = 'Christopher Alan Farage'

    text_business_owner_1_date_of_birth = Text()
    text_business_owner_1_date_of_birth.tab_label = 'business_owner_1_date_of_birth'
    text_business_owner_1_date_of_birth.value = '10/11/1970'

    text_business_owner_1_address = Text()
    text_business_owner_1_address.tab_label = 'business_owner_1_address'
    text_business_owner_1_address.value = '9309 Northeast Paw Paw Drive, Kansas City, MO, 64157'

    text_business_bank_name_provided = Text()
    text_business_bank_name_provided.tab_label = 'business_bank_name_provided'
    text_business_bank_name_provided.value = 'Bank of Midwest'

    text_business_bank_acct_number = Text()
    text_business_bank_acct_number.tab_label = 'business_bank_acct_number'
    text_business_bank_acct_number.value = '2860002344'

    text_business_bank_routing_number = Text()
    text_business_bank_routing_number.tab_label = 'business_bank_routing_number'
    text_business_bank_routing_number.value = '101006699'

    text_loan_amount_approved = Text()
    text_loan_amount_approved.tab_label = 'loan_amount_approved'
    text_loan_amount_approved.value = '$65,000.00'

    text_payback_amount = Text()
    text_payback_amount.tab_label = 'payback_amount'
    text_payback_amount.value = '$86,450.00'

    text_processing_fee = Text()
    text_processing_fee.tab_label = 'processing_fee'
    text_processing_fee.value = '$475.00'

    text_origination_fee = Text()
    text_origination_fee.tab_label = 'origination_fee'
    text_origination_fee.value = '$975.00'

    text_loan_frequency = Text()
    text_loan_frequency.tab_label = 'loan_frequency'
    text_loan_frequency.value = 'Daily'

    text_loan_payment_amount = Text()
    text_loan_payment_amount.tab_label = 'loan_payment_amount'
    text_loan_payment_amount.value = '$343.00'

    text_maturity_date_1 = Text()
    text_maturity_date_1.tab_label = 'maturity_date_1'
    text_maturity_date_1.value = 'twelve (12.00)'

    text_maturity_date_2 = Text()
    text_maturity_date_2.tab_label = 'maturity_date_2'
    text_maturity_date_2.value = 'twelve (12.00)'

    tabs = Tabs()
    tabs.text_tabs = [text_business_legal_name, text_dba, text_business_address, text_state_of_incorporation,
                      text_business_owner_1_first_last_name, text_business_owner_1_date_of_birth,
                      text_business_owner_1_address, text_business_bank_name_provided, text_business_bank_acct_number,
                      text_business_bank_routing_number, text_loan_amount_approved, text_payback_amount,
                      text_processing_fee, text_origination_fee, text_loan_frequency, text_loan_payment_amount,
                      text_maturity_date_1, text_maturity_date_2]
    t_role.tabs = tabs

    return t_role


def generate_template_role_business_guarantor():

    t_role = TemplateRole()
    t_role.role_name = 'Business Guarantor'
    t_role.name = 'Karen Duque'
    t_role.email = 'karen@lendinfront.com'
    t_role.client_user_id = '54657682'
    t_role.routing_order = '1'

    return t_role


def generate_template_role_guarantor():

    t_role = TemplateRole()
    t_role.role_name = 'Guarantor'
    t_role.name = 'Juan Sebastian Fernandez'
    t_role.email = 'checho@lendinfront.com'
    t_role.client_user_id = '54657683'
    t_role.routing_order = '1'

    return t_role


def generate_envelop(env_def, envelope_api, business_owner_role, business_guarantor_role, guarantor_role):

    env_def.template_roles = [business_owner_role, business_guarantor_role, guarantor_role]
    env_def.status = 'sent'

    envelope_summary = envelope_api.create_envelope(DS_CONFIG['account_id'], envelope_definition=env_def)
    envelope_id = envelope_summary.envelope_id

    print("Envelope {} has been sent, summary id: {}".format(envelope_id, envelope_summary))

    return envelope_id


def generate_recipient_view_request_by_role(envelope_id, envelope_api, role):

    recipient_view_request = RecipientViewRequest(
        authentication_method=DS_CONFIG['authentication_method'], client_user_id=role.client_user_id,
        recipient_id=role.routing_order, return_url=DS_CONFIG['app_url'] + '/ds_return?envelope_id={}'.format(envelope_id),
        user_name=role.name, email=role.email
    )

    results = envelope_api.create_recipient_view(DS_CONFIG['account_id'], envelope_id,
                                                 recipient_view_request=recipient_view_request)

    print("Results {} {} has been generated".format(role.routing_order, results))
    print("############################")

    generate_envelop_report_status(envelope_id, envelope_api, role)


def generate_envelop_report_status(envelope_id, envelope_api, role=None):

    envelope = envelope_api.get_envelope(DS_CONFIG['account_id'], envelope_id)

    if role is None:
        print("Envelop Results after all signs {}".format(envelope))
    else:
        print("Envelop Results {} after all signs {}".format(role.routing_order, envelope))

    print("############################")


def embedded_signing_ceremony():
    """
    The document <file_name> will be signed by <signer_name> via an
    embedded signing ceremony.
    """

    api_client = get_api_client_by_jwt_authorization_flow()

    envelope_api = EnvelopesApi(api_client)

    env_def = get_envelop_definition()

    business_owner_role = generate_template_role_business_owner()
    business_guarantor_role = generate_template_role_business_guarantor()
    guarantor_role = generate_template_role_guarantor()

    envelope_id = generate_envelop(env_def, envelope_api, business_owner_role, business_guarantor_role, guarantor_role)
    # envelope_id = ''

    generate_recipient_view_request_by_role(envelope_id, envelope_api, business_owner_role)
    generate_recipient_view_request_by_role(envelope_id, envelope_api, business_guarantor_role)
    generate_recipient_view_request_by_role(envelope_id, envelope_api, guarantor_role)

    generate_envelop_report_status(envelope_id, envelope_api)

    return ''


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
                <iframe name="LendingFront" src="{url_doc_signed}" height="720" width="800"></iframe>
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

    #
    #  Step 7. Get the envelop id from the request.
    #

    # print(request.args)
    envelope_id = request.args.get('envelope_id')

    #
    # Step 8. Create and define the API Client.
    #
    api_client = get_api_client_by_jwt_authorization_flow()

    #
    # Step 9. The envelope definition is created and ready to access list documents
    #

    envelope_api = EnvelopesApi(api_client)
    docs_list = envelope_api.list_documents(DS_CONFIG['account_id'], envelope_id)

    # print("EnvelopeDocumentsResult:\n{0}", docs_list)

    #
    # Step 10. Retrieve the document based on list documents and the envelope id
    #

    document_id = docs_list.envelope_documents[0].document_id

    data = envelope_api.get_document(DS_CONFIG['account_id'], document_id, envelope_id)
    # print(data)

    #
    # Step 11. Process the document in order to gat a base64 string to be showed into the html iframe
    #

    with open(os.path.join(data), "rb") as document:
        content_bytes = document.read()
        base64_file_content = base64.b64encode(content_bytes).decode('ascii')

    return '''
        <html lang="en">
            <body>
                <iframe name="LendingFront" src="data:application/pdf;base64, {file}" height="700" width="780"></iframe>
            </body>
        </html>          
    '''.format(event=request.args.get('event'), file=base64_file_content)


app.run(port=5001, debug=True)
