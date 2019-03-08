# Python3 Quick start example: list envelopes in the user's account
# Copyright (c) 2018 by DocuSign, Inc.
# License: The MIT License -- https://opensource.org/licenses/MIT

import base64, os
from docusign_esign import ApiClient, EnvelopesApi
import pendulum # pip install pendulum
import pprint

# Settings
# Fill in these constants
#
# Obtain an OAuth access token from https://developers.hqtest.tst/oauth-token-generator
access_token = 'eyJ0eXAiOiJNVCIsImFsZyI6IlJTMjU2Iiwia2lkIjoiNjgxODVmZjEtNGU1MS00Y2U5LWFmMWMtNjg5ODEyMjAzMzE3In0.AQoAAAABAAUABwCA-2khDaPWSAgAgDuNL1Cj1kgCALk7xTqm_V1Akk8CFOmsnOEVAAEAAAAYAAEAAAAFAAAADQAkAAAAZjBmMjdmMGUtODU3ZC00YTcxLWE0ZGEtMzJjZWNhZTNhOTc4EgABAAAACwAAAGludGVyYWN0aXZlMAAAOKAfDaPWSDcAxAkY_dTa20i_b-JSx4oGpA.M8C0sdlNNBlUKHXUv-zQn4ZnPLXXjpHFst1Ei9dIl4_ykIInayXAfinDwpzY7uPkaow6nN_wi4wuHsfT_o2bhe5BFR7x6MiS3adzwEIYefGU_nXh5JMf9e3yYHLgv9obe4WOH7O9to7qXIg-CE6Wkd6AbobIzVHPYW6agZsFjh_YqAAs5V9DlH_CoKPmHpoJ3LNqe3YTB2nfFtp_LQuqpwWItIyek-Kv0Flxcdtll0ingBhqI6YXSaU5yUZYknCIFGha_4XElkB-IIKwO083LT44atKUblcsO_npDCheXS0MSnLae1kzBjO5kiaDo2_RidxwZoa1kAl1ASnUTzvtsw'

# Obtain your accountId from demo.docusign.com -- the account id is shown in the drop down on the
# upper right corner of the screen by your picture or the default picture. 
account_id = '8063857'
base_path = 'https://demo.docusign.net/restapi'

def list_envelopes():
    """
    Lists the user's envelopes created in the last 10 days
    """
    
    #
    # Step 1. Prepare the options object
    #
    from_date = pendulum.now().subtract(days=10).to_iso8601_string()
    #
    # Step 2. Get and display the results
    # 
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header("Authorization", "Bearer " + access_token)

    envelope_api = EnvelopesApi(api_client)
    results = envelope_api.list_status_changes(account_id, from_date = from_date)
    return results


# Mainline
results = list_envelopes()
print("\nEnvelopes:\n")
pprint.pprint(results, indent=4, width=80)

