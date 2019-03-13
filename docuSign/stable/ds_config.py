# ds_config.py
#
# DocuSign configuration settings
import os

from EncryptionHelper import AESCipher

cyfrer = AESCipher()

DS_CONFIG = {
    # Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
    # upper right corner of the screen by your picture or the default picture.
    'account_id': '8100898',
    'api_account_id': '918f638e-30fd-41c9-b6b2-e3f56f9c831b',
    'template_id': 'bfabb622-2aec-4c10-8861-0fa0cba325b7',  # The Template ID
    'integrator_key': '25a63cfa-c9b6-4411-85ac-257996135e16',  # The app's DocuSign integration key
    'user_admin_id': '00057a6e-9fe8-406e-accc-12570b8a22d2',  # User Admin ID
    'secret_key': '49fe683f-9593-4094-85e1-c921b462f09a',  # The app's DocuSign integration key's secret
    'key_pair_id': '64a563b9-e622-45e9-b7d4-568dbc3a6717',  # ID for RSA Key Pair
    # User and role configuration (Signer)
    'signer_role': 'Guarantor',
    'signer_name': 'Christopher Alan Farage',  # LendingFront Team
    'signer_email': 'christopheraf@bfs.com',
    'client_user_id': '54657688',  # Random number to be assigned to the client
    'routing_order': '1',  # Order of the recipient
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
    'id_rsa': cyfrer.encrypt("-----BEGIN RSA PRIVATE KEY-----\n"
                             "MIIEowIBAAKCAQEAiEcgIygqeCLDjxaYCX83cxl4GwWEFetW29QTdqssmCxJhcvy\n"
                             "14e1KrbhdK4lNAfgKBWWSn+wwHGwplmjl+/uYkSKIsZEWFBrVkZemfe4L/CoQD6O\n"
                             "0m4rN1i3Wz+P8nhFXW5rvfBHEQESC/QHES5G6rZ+DS+0MwK3yDaIbSsSE1FRkQ9X\n"
                             "gR+et6XLamMge4wDta/68mCC6eC1a2cRxe4cYYfBWb3guC8mfuaBsGmscCgza9uf\n"
                             "HIBsMBiJNj7ExozTl7QmhF6Ewj2TUzjlPYrRL3CAXo8UT8BmoQQ9t2nxfsIn19EK\n"
                             "mMlNnDUfEUeckOF8Ks8t7V4UyWMYLPZXaAqrsQIDAQABAoIBAEHXm39g+KPyp+mK\n"
                             "UQrFnFTQCWeE0ryEaALuBDlhmrorK5qpXzsjJjTtByEIwpDQ/Uxgoax85TkVtPOq\n"
                             "e4/9LH/t/Y+vm3XP5QxaE3rwZN1EuQXRM9AXymmDQ5OisjnEQj9SClxKqwtcKQv9\n"
                             "ayyx3zGn2l8knTvIJGNndaLJHIKYGiCQkX6RsPfbWrmmvpmkrMqC+HXEJTvQ9RzF\n"
                             "pi+5f3XmSFJE3UEmX7J13G/3imNnU6tDNhVmGtA0OgpXmcrBBK7mPz+ygtkPvRdj\n"
                             "6mC4f6QNbDGmPlNq/Hih9oCdeUzkN+iXEw88fJjidglwyMFQnOw9X1N31kUyfh1P\n"
                             "engCwMECgYEA/0+A4KFEmur7bF9tHHoeozLKCLdzApIiF+ZRGCO41y08iy2kePxs\n"
                             "baeidDcl+p/UcL4DWzD5uM5BJmzf2YtQRHLgynduAJf9OG5o6NgOz6qpOUG3FqWv\n"
                             "v1fstYhUCVyegfbBsCJoFa9AOuTl8sW0N277JMf6a+FSPMOSTbeYzt8CgYEAiKVV\n"
                             "qNBOiRc0omXjUkOh2CyeQfk9vm9d+iijFMFiz59bIxZjykF83JoI0MHufj2e/WMF\n"
                             "JEl4mVSGdEL0S1NW0syD0bfv2VGOLdHJ5ExdmpPOx1BwHcvhsoKrRB7iNnDPI2Ho\n"
                             "td4g9gnwwrPk0JWL+RWmJj6vg6zg1qCEUIRbJ28CgYEAs6Mc6vCNdPMhNH9wJjlG\n"
                             "lU2HGdr58TUhB+/l3zZDOCN8FfFnaDkzkXQBugOTlWQf9bO8aM1s57s32/F/D3IW\n"
                             "aBLsV4jwvToz0SDeb/aVdUh/COpUCHtLzTXwN0pU1sF0Rb15SpTq51cHumiT4t14\n"
                             "kAhmbNrIOF+xnU9+AXDM88ECgYA+ocG0gd4tegR3F0ptj3BkXHcheDNz0Sn7Gps9\n"
                             "TTKURc+JMp8EuqWXm8bEoM9G78mrDLLzofV0GkkSiwncaNOYBYO6IZv/OSF5IPpv\n"
                             "+QzCaFNUCiuJjMTjhH8p1xoKqARZjGwUyD7FZ2MCa2BKtvEUd3bTetIKAbiAx8w9\n"
                             "95ysYwKBgCuaAzkmQhIodtcDykd6tV/OzkEDYSc1CMMtneaFjZkKmx00/0UFYo31\n"
                             "tvhFLNd58ZPrjRU61BX9rFtNREZ1xJfxfQ7BZ0z+DfUkf9ZNCtkyjIxhHRHYQAun\n"
                             "djIsmfunWKYgRc3tp6Comd7/hZZVYolSBg1V/dkm7TqO3uUcW6II\n"
                             "-----END RSA PRIVATE KEY-----"),  # Private RSA Key
    'private_key_filename': 'docusign_private_key_lendingfront.txt',  # Private RSA Key file
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