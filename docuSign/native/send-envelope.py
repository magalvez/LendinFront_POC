# Python3 Quick start example: send an envelope to be signed. The signer is notified by email
# Copyright (c) 2018 by DocuSign, Inc.
# License: The MIT License -- https://opensource.org/licenses/MIT

import base64, os
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Tabs, Recipients, Document

# Settings
# Fill in these constants
#
# Obtain an OAuth access token from https://developers.hqtest.tst/oauth-token-generator
access_token = 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQoAAAABAAUABwCA-2khDaPWSAgAgDuNL1Cj1kgCALk7xTqm_V1Akk8CFOmsnOEVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjBmMjdmMGUtODU3ZC00YTcxLWE0ZGEtMzJjZWNhZTNhOTc4EgABAAAACwAAAGludGVyYWN0aXZlMAAAOKAfDaPWSDcAxAkY_dTa20i_b-JSx4oGpA.M8C0sdlNNBlUKHXUv-zQn4ZnPLXXjpHFst1Ei9dIl4_ykIInayXAfinDwpzY7uPkaow6nN_wi4wuHsfT_o2bhe5BFR7x6MiS3adzwEIYefGU_nXh5JMf9e3yYHLgv9obe4WOH7O9to7qXIg-CE6Wkd6AbobIzVHPYW6agZsFjh_YqAAs5V9DlH_CoKPmHpoJ3LNqe3YTB2nfFtp_LQuqpwWItIyek-Kv0Flxcdtll0ingBhqI6YXSaU5yUZYknCIFGha_4XElkB-IIKwO083LT44atKUblcsO_npDCheXS0MSnLae1kzBjO5kiaDo2_RidxwZoa1kAl1ASnUTzvtsw'

# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture. 
account_id = '8063857'

# Recipient Information:
signer_name = 'Jonathan Vallejo'
signer_email = 'jvallejo@lendingfront.com'

# The document you wish to send. Path is relative to the root directory of this repo.
file_name_path = 'demo_documents/World_Wide_Corp_lorem.pdf';
base_path = 'https://demo.docusign.net/restapi'

# Constants
APP_PATH = os.path.dirname(os.path.abspath(__file__))


def send_document_for_signing():
    """
    Sends the document <file_name> to be signed by <signer_name> via <signer_email>
    """

    # Create the component objects for the envelope definition...
    with open(os.path.join(APP_PATH, file_name_path), "rb") as file:
        content_bytes = file.read()
    base64_file_content = base64.b64encode(content_bytes).decode('ascii')

    document = Document(  # create the DocuSign document object
        document_base64 = base64_file_content,
        name = 'Example document',  # can be different from actual file name
        file_extension = 'pdf',  # many different document types are accepted
        document_id = 1  # a label used to reference the doc
    )

    # Create the signer recipient model 
    signer = Signer( # The signer
        email = signer_email, name = signer_name, recipient_id = "1", routing_order = "1")

    # Create a sign_here tab (field on the document)
    sign_here = SignHere( # DocuSign SignHere field/tab
        document_id = '1', page_number = '1', recipient_id = '1', tab_label = 'SignHereTab',
        x_position = '195', y_position = '147')

    # Add the tabs model (including the sign_here tab) to the signer
    signer.tabs = Tabs(sign_here_tabs = [sign_here]) # The Tabs object wants arrays of the different field/tab types

    # Next, create the top level envelope definition and populate it.
    envelope_definition = EnvelopeDefinition(
        email_subject = "Please sign this document sent from the Python SDK",
        documents = [document], # The order in the docs array determines the order in the envelope
        recipients = Recipients(signers = [signer]), # The Recipients object wants arrays for each recipient type
        status = "sent" # requests that the envelope be created and sent.
    )
    
    # Ready to go: send the envelope request
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    results = envelope_api.create_envelope(account_id, envelope_definition=envelope_definition)
    return results


# Mainline
results = send_document_for_signing()
print("\nEnvelope status: " + results.status + ". Envelope ID: " + results.envelope_id + "\n")
