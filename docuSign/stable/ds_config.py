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
                             "MIIEpAIBAAKCAQEAnlZusewKR/r5bvclYHf7B7m2tVOMFC/MsbX651f8xa0WKN16\n"
                             "cW1BbZ9nI436xqzYuuJAcap1pBx8eNp2Uc86dHrpE5wXG1NW7D1JZ+QoAEpo1oII\n"
                             "7Y4s+Z7LqbvWL697gTiJjKgo8Lt4UggSkr1RgQg7aLveV8xKVDHWBVLblYwXnwAf\n"
                             "+nJgKp3yPVwvneGeUjE+pqlst4plC05Vu5uQ6KSjA9f7vQCpvmaBeBD9IybwAxU2\n"
                             "0KxfAPHRXZgQrikVIP7js0qLIhjI+WUnsW1tLcN0zX768q4j/RUL25ATdS9G8DIn\n"
                             "OBNTEkZyfswHeXr8YFyDx6XX4B7uWRVrUKAbFwIDAQABAoIBABynX5jrMmEcVg9y\n"
                             "wlzW2aLoRNxDplHw5IY0fJdpIOFVFXGHwyTLtM91zWBtzTgvB3mqgCcRxgBQ92WX\n"
                             "g1oCun1h0NQvpy7WwiA2ZxZZ/7MtxBMtrRfwZss1pX2t9HDkvOEBrkK6G86U3o1Z\n"
                             "0KKliB5lsvqdJPuWiMz7x9Nmzz4ctym3x2wHp2rEMraYyJoDWEYsJkcqaX0PqRJo\n"
                             "VQUKM5d2cgB3cBnL/WCGe08BTE2kg9wY5ZM1kuhY375tAefToK+RmJlLF2RjuuCc\n"
                             "UParvq1cvHKejF8A04gL3BdFIliU7Rvgs6tkSxIl0XI5+8VLiRGatdeebzGksp2d\n"
                             "DipZeaECgYEA0i25lnNZd63WucxS319Ux3qAQziHEZKFFKaQDgqEqv8s3VBetobw\n"
                             "ZwJ+mIkdnoReNsQ+CN5jDJI5sS5tBGFoKpvn8kIe3VtMwUh0AlYSHEmyNjNT9+Ks\n"
                             "itSECSyBDcuSmZVbjQ6UIi8IUpPaz43IPGREiZwvySr91DdxAJFIenUCgYEAwNtp\n"
                             "OLeN6WKJ+Rfxlkrl5LXsSdegqIRnAW78zZOT59ylPf8/7Yx9EVYG6Oa8Nn6lzz/G\n"
                             "Il/e/bDcYwbqza9STXvNSnu1+1JXqJ9upreNn5wSagukK2+7b1nLM3wtdynX9Onz\n"
                             "tXGXknx6ZjK0IeteK+LM9Yse4Qga4UT2cgNM1dsCgYEAsKVfirRt6GlBxCyXJkew\n"
                             "MGuj61tSIhG8KewHvNVYRYNsCKHoyI3G9Tyie78aFsV3jZ4H6VpHcyReuqyjUYAw\n"
                             "lUctfW3XFQIME5K6ddAzLnU+A9HF69wmWhRc2H0ABkEneE+Qf5BWLhjLbOP5jmHC\n"
                             "fgdjlyie/PtWFIt4PRreCJUCgYEAlnAQ6i80weMd4XLt/uC55+iJQyiyqAFwIEwl\n"
                             "Y29FJs6VD4F2qqS2Qrmqdi7WjmPIj5wdwF6soZQ+tfiFXKDwQITcJMfPsxYOTvje\n"
                             "5am1DdY+/v3JuCBWQ4v12Fl7VcMMNH3yn4zWQWxcRjAzF2p0cSNf4gH9umgKH8Md\n"
                             "wt4UJ5UCgYA95FyKVXO97T5uG9S+oKhAZUxqYeXMthz1YWQuPvlAsmnfv0CWcMiq\n"
                             "UrZuT/QMTwrqG83zVQXoS42g3EOjg4IN0imS26zmgmBT8eDfPcdSKZMbz1UJHRwM\n"
                             "cPjN4sIv5LS+U2rOfTZtriobhC+gXfqz3ohyGbWLjDZcJ7DRfKy3ig==\n"
                             "-----END RSA PRIVATE KEY-----"),  # Private RSA Key
    'private_key_filename': 'docusign_private_key_lendingfront_64a563b9-e622-45e9-b7d4-568dbc3a6717.txt',  # Private RSA Key file
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