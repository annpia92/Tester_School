import requests
import hashlib

class PeopleClientError(Exception):
    pass

class PeopleClient:

    lista_kluczy = ['first_name', 'last_name', 'email', 'phone', 'ip_address']
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_all(self, limit):
        # response = requests.get(self.base_url) <- to samo co ponizej, tylko bardziej rozpisane
        # response.json()
        if limit is None:
            response = requests.get(self.base_url)
            return response
        if limit <= 0:
            raise ValueError("limit has to be positive")
        response = requests.get(self.base_url,
                                params={'_limit': limit})

        total_records = int(response.headers['X-Total-Count'])
        pages_count = total_records // limit
        if total_records % limit !=0:
            pages_count += 1
            people = response.json()
        for page in range(2, pages_count+1):
            chunk = requests.get(self.base_url,
                                 params={'_limit': limit, '_page': page}).json()
            for person in chunk:    ##zamiast tego moglo byc people.extend(chunk)
                people.append(person)
        return people

    def add_person(self, first_name, last_name, email, phone, ip_address):

        person = {'first_name': first_name, "last_name": last_name, 'email': email, 'phone': phone, 'ip_address': ip_address}
        headers = {"Authorization": 'Bearer ' + self.token}
        response = requests.post(self.base_url, json=person, headers=headers)
        if not response.ok:
            raise PeopleClientError(response.json()['error'])

    def get_user_by_id(self, user_id):
        response = requests.get(self.base_url+str(user_id))
        response.raise_for_status()
        if response.status_code != 200:
            raise PeopleClientError(response.json()['error'])
        return response.json()

    def query(self, **criteria):

        response = requests.get(self.base_url + str(criteria))
        for key in criteria:
            if key in self.lista_kluczy:
                return requests.get(self.base_url + str(criteria))
            else:
                raise ValueError("Unknown field: "+key)

    def people_by_partial_ip(self, ip):
        response = requests.get(self.base_url, params={'ip_address_like': "^" + str(ip)}).json()

        return response


if __name__ == '__main__':
    token = hashlib.md5('relayr'.encode('ascii')).hexdigest()
    client = PeopleClient('http://polakow.eu:3000/people/', token)
    people = client.get_all(None)
    people2 = client.get_all(50)
    print(people)
    print(people2)
    client.add_person('Jaime', 'Lannister', 'hearmeroar@yahoo.com', '+45678653', '192.168.1.1')
    moj_user = client.get_user_by_id(89)
    print(moj_user)
    szukany = client.query(first_name='Jaime')
    print(szukany)
    adresses = client.people_by_partial_ip('192.168')
    print(adresses)
