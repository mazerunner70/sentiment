import boto3
import botocore
import os
import requests
from os.path import join, dirname 
from dotenv import load_dotenv


class CognitoProof:

    def testlogin(self):
        dotenv_path = join(os.getcwd(), '.env')
        print(dotenv_path)
        load_dotenv(dotenv_path)
        username = os.environ['USERNAME']
        password = os.environ['PASSWORD']
        temp_password = os.environ['TMP_PASSWORD']
        app_clientid = os.environ['POOL_CLIENT_ID']

        print('u/p:', username, password)
        print('app id', app_clientid)
        client = boto3.client('cognito-idp')
        response = ""
        try:
            response = client.initiate_auth(
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': username,
                    'PASSWORD': password
                },
                ClientId=app_clientid
            )
        except Exception as e:
            print('666error {}'.format(e))
            response = client.initiate_auth(
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': username,
                    'PASSWORD': temp_password
                },
                ClientId=app_clientid
            )
            print ('444', response)
            challenge_name = response.get('ChallengeName')
            session = response.get('Session')
            response = client.respond_to_auth_challenge(
                ClientId=app_clientid,
                ChallengeName=challenge_name, 
                Session=session,
                ChallengeResponses={
                    'USERNAME': username,
                    'NEW_PASSWORD': password
                }
            )

#        print('Response')
        print(response)
        print('ID Token')
        idToken = response['AuthenticationResult']['IdToken']
#        print(idToken)

        apiGateway=os.environ['API_URL']
        print('url='+apiGateway+'reports')
        response = requests.get(apiGateway+'reports', headers={'Authorization': idToken})
        print('res')
        print(response.json())
        response = requests.get(apiGateway+'reports')
        print('res')
        print(response.json())


if __name__ == '__main__':
    CognitoProof().testlogin()
