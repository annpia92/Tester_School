from time import time

# Requires requests library. Install using pip
import requests


class EapiRequests(object):
    """Allows to make requests to EAPI on given setup."""

    def __init__(self, eapi_url, rui_url, user_name, user_password):
        """
        :param eapi_url: Eapi address on tested setup in following format: ^http[s]?:\/\/[a-z0-9\.-]+\.com$
        :type eapi_url: str
        :param rui_url: Rui address on tested setup in following format: ^http[s]?:\/\/[a-z0-9\.-]+\.com$
        :type rui_url: str
        :type user_name: str
        :type user_password: str
        """
        self.eapi_url = eapi_url + '/rest/'
        self.rui_url = rui_url + '/oauth/token'
        self.user_name = user_name
        self.user_password = user_password
        self.token = self._generate_token()

    def request(self, method, command, **kwargs):
        """Creates request to EAPI.
        See http://docs.python-requests.org/en/master/api/ for documentation on arguments.
        """
        response = requests.request(method.upper(), self.eapi_url + command, headers={
            'Authorization': self.token, 'Content-Type': 'application/json'}, verify=False,
                                    **kwargs)
        return response

    def _generate_token(self):
        """Returns token used for authentication"""
        return 'bearer ' + requests.post(url=self.rui_url,
                                         data={'grant_type': 'password',
                                               'password': self.user_password,
                                               'response_type': 'token',
                                               'username': self.user_name},
                                         verify=False
                                         ).json()['access_token']


    def test_isGetOK(self,asdid):
        """
        Method checks if the device with given asdid can be retrieved with Status 200 OK
        :return: "Jest OK" if True or "Nie dziala" if False

        """
        response = eapi_requests.request('GET', '2.0/devices/'+str(asdid))

        if response.status_code == 200:
            return print("Jest OK", response.status_code, response.reason)
        else:
            print("Nie dziala",response.status_code,"Przyczyna: ", response.reason)

    def test_isDeleteOK(self,asdid):
        """
        Method checks if the device with given asdid can be deleted with Status 204 No Content
        :return: "Jest OK" if True or "Nie dziala" if False

        """
        response = eapi_requests.request('DELETE', '2.0/devices/'+str(asdid))

        if response.status_code == 200:
            return print("Jest OK", response.status_code, response.reason)
        else:
            print("Nie dziala",response.status_code,"Przyczyna: ", response.reason)

    def test_isPatchOK(self,asdid, **kwargs):
        """
        Method checks if the device with given asdid can be updated with new alarm parameters (Status 201 Created)
        :return: "Jest OK" if True or "Nie dziala" if False

        """
        response = eapi_requests.request('PATCH', '2.0/devices/{}/alarms'.format(asdid))

        if response.status_code == 201:
            return print("Jest OK, status: ", response.status_code, response.reason)
        else:
            print("Nie dziala, status: ",response.status_code, "Przyczyna: ", response.reason)

eapi_requests = EapiRequests(eapi_url='https://eapigeic-qa2.proximetry.com',
                             rui_url='https://geic-qa2.proximetry.com',
                             user_name='user08',
                             user_password='P@ssw0rd')
# Send request to retrieve details about first device from systems
systems_response = eapi_requests.request('GET', '1.9/systems', params={'limit': 1})
# Retrieve asdid from response
asdid = systems_response.json()[0]['asdid']
# Set alarm for device identified by asdid taken from system
set_alarm_response = eapi_requests.request('PATCH',
                                           '2.0/devices/{}/alarms'.format(asdid),
                                           json={
                                               "data": [
                                                   {
                                                       "alarm_id": "test_alarm_1",
                                                       "action": "SET",
                                                       "timestamp": int(time()) * 1000,
                                                       "severity": "EMERGENCY",
                                                       "description": "Device overheating",
                                                       "details": "Temperature is above safe levels",
                                                       "optional": {}
                                                   }
                                               ]
                                           }
                                           )

if __name__ == '__main__':

    result = eapi_requests.test_isGetOK('7AD4CDD5B933')
    print(result)
    result2 = eapi_requests.test_isPatchOK('7AD4CDD5B933',
                                           json={
                                               "data": [
                                                   {
                                                       "alarm_id": "test_alarm_2",
                                                       "action": "SET",
                                                       "timestamp": int(time()) * 1000,
                                                       "severity": "CRITICAL",
                                                       "description": "Device detached",
                                                       "details": "Device is not correctly plugged in",
                                                       "optional": {}
                                                   }
                                               ]
                                           })
    print(result2)
    result3 = eapi_requests.test_isDeleteOK('7AD4CDD5B933')
    print(result3)


