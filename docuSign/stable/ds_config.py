# ds_config.py
#
# DocuSign configuration settings
import os

DS_CONFIG = {
    # Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
    # upper right corner of the screen by your picture or the default picture.
    'account_id': '8100898',
    'api_account_id': '918f638e-30fd-41c9-b6b2-e3f56f9c831b',
    'template_id': '36fd5b8d-b750-4606-8e38-93692f37c9fe',  # The Template ID
    'integrator_key': '25a63cfa-c9b6-4411-85ac-257996135e16',  # The app's DocuSign integration key
    'user_admin_id': '00057a6e-9fe8-406e-accc-12570b8a22d2',  # User Admin ID
    'secret_key': '49fe683f-9593-4094-85e1-c921b462f09a',  # The app's DocuSign integration key's secret
    'key_pair_id': '64a563b9-e622-45e9-b7d4-568dbc3a6717',  # ID for RSA Key Pair
    # User and role configuration (Signer)
    'signer_role': 'Non-Employee',
    'signer_name': 'x',  # LendingFront Team
    'signer_email': 'technology+bfs@lendingfront.com',
    'app_url': 'http://localhost:5001',  # The url of the application. Eg http://localhost:5000
    # NOTE: You must add a Redirect URI of appUrl/ds/callback to your Integration Key.
    #       Example: http:#localhost:5000/ds/callback
    'redirect_uri': 'http://localhost:5001/ds_return',  # Redirect URI
    'base_path': 'https://demo.docusign.net/restapi',  # The API base_path
    'oauth_base_url': 'account-d.docusign.com',
    'authentication_method': 'None',
    # Obtain an OAuth access token from https://developers.hqtest.tst/oauth-token-generator
    # Or https://developers.docusign.com/oauth-token-generator
    'access_token': 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQoAAAABAAUABwAAoNVrE6TWSAgAAOD4eVak1kgCALk7xTqm_V1Akk8CFOmsnOEVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjBmMjdmMGUtODU3ZC00YTcxLWE0ZGEtMzJjZWNhZTNhOTc4EgABAAAACwAAAGludGVyYWN0aXZlMACA3AtqE6TWSDcAxAkY_dTa20i_b-JSx4oGpA.0PEf38MnbSrmPPyCjO-hEDLnkIRahNWwIjJb5gVJCehYHlrpeMpbLf06-5Gcb4VxMOF9Arscft3mOvffbhrMx3pabV5a4axr977yy_d59rHO0Botw9ohQ4kZNPiCjMR_1FQW72kQ4sLAfw7ImEm4WAC6f0K47wd25wE5-qL36k9j5uHO7nu2XH1DzP4DgDozN8EhEG6thHq_P7xGG4YOT5A_h1lrn-nnmeKj4S2EpJ7cC-PRDd6K5AQY8SCNM7VscXSAs78ij-l8WBlQZJdVzimFggkDLuwQkzTYaO2Vn8VYLQ8lVUS9fOv0QhjKnBwL8o1M_5-5EDp4xFW2_2U54w',
    'session_secret': '{SESSION_SECRET}',  # Secret for encrypting session cookie content
                                           # Use any random string of characters
    'private_key_filename': 'docusign_private_key_lendingfront.txt',  # Private RSA Key file
    'client_user_id': '985612',  # Random number to be assigned to the client
    'allow_silent_authentication': True,  # a user can be silently authenticated if they have an
    # active login session on another tab of the same browser
    'target_account_id': None,  # Set if you want a specific DocuSign AccountId,
                                # If None, the user's default account will be used.
    'demo_doc_path': 'demo_documents',
    'doc_docx': 'World_Wide_Corp_Battle_Plan_Trafalgar.docx',
    'doc_pdf':  'World_Wide_Corp_lorem.pdf',
    # Payment gateway information is optional
    'gateway_account_id': '{DS_PAYMENT_GATEWAY_ID}',
    'gateway_name': "stripe",
    'gateway_display_name': "Stripe",
    'github_example_url': 'https://github.com/docusign/eg-03-python-auth-code-grant/tree/master/app/',
    'documentation': '',  # Use an empty string to indicate no documentation path.
    'environment_status': 'sent'  # Environment configuration
}