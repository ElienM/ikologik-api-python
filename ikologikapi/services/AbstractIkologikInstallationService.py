import json
from types import SimpleNamespace

import requests

from ikologikapi.IkologikApiCredentials import IkologikApiCredentials
from ikologikapi.IkologikException import IkologikException
from ikologikapi.domain.Search import Search
from ikologikapi.services.AbstractIkologikCustomerService import AbstractIkologikCustomerService


class AbstractIkologikInstallationService(AbstractIkologikCustomerService):

    def __init__(self, jwtHelper: IkologikApiCredentials):
        super().__init__(jwtHelper)

    # CRUD Actions

    def get_url(self, customer: str, installation: str):
        pass

    def get_by_id(self, customer: str, installation: str, id: str) -> object:
        try:
            response = requests.get(
                self.get_url(customer, installation) + f'/{id}',
                headers=self.get_headers()
            )
            if response.status_code == 200:
                result = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
                return result
            else:
                raise IkologikException("Request returned status " + str(response.status_code))
        except IkologikException as ex:
            raise ex
        except Exception as ex:
            raise IkologikException("Error while getting an installation with id: " + id)

    def list(self, customer: str, installation: str) -> list:
            try:
                response = requests.get(
                    self.get_url(customer, installation),
                    headers=self.get_headers()
                )
                if response.status_code == 200:
                    result = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
                    return result
                else:
                    raise IkologikException("Request returned status " + str(response.status_code))
            except IkologikException as ex:
                raise ex
            except Exception as ex:
                raise IkologikException("Error while querying a list")

    def search(self, customer: str, installation: str, search: Search) -> list:
        try:
            data = json.dumps(search, default=lambda o: o.__dict__)
            response = requests.post(
                f'{self.get_url(customer, installation)}/search',
                data=data,
                headers=self.get_headers()
            )
            if response.status_code == 200:
                result = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
                return result
            else:
                raise IkologikException("Request returned status " + str(response.status_code))
        except IkologikException as ex:
            raise ex
        except Exception as ex:
            raise IkologikException("Error while searching for an installation")

    def create(self, customer: str, installation: str, o: object = None) -> object:
        try:
            data = json.dumps(o, default=lambda o: o.__dict__)
            response = requests.post(
                self.get_url(customer, installation),
                data=data,
                headers=self.get_headers()
            )
            if response.status_code == 201:
                result = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
                return result
            else:
                raise IkologikException("Request returned status " + str(response.status_code))
        except IkologikException as ex:
            raise ex
        except Exception as ex:
            raise IkologikException("Error while creating an installation")

    def update(self, customer: str, installation: str, id: str, o: object) -> object:
        try:
            data = json.dumps(o, default=lambda o: o.__dict__)
            response = requests.put(
                f'{self.get_url(customer, installation)}/{id}',
                data=data,
                headers=self.get_headers()
            )
            if response.status_code == 200:
                result = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
                return result
            else:
                raise IkologikException("Request returned status " + str(response.status_code))
        except IkologikException as ex:
            raise ex
        except Exception as ex:
            raise IkologikException("Error while updating an installation")

    def delete(self, customer: str, installation: str, id: str):
        try:
            response = requests.delete(
                f'{self.get_url(customer, installation)}/{id}',
                headers=self.get_headers()
            )
            if response.status_code != 204:
                raise IkologikException("Request returned status " + str(response.status_code))
        except IkologikException as error:
            raise IkologikException("Error while deleting an installation")
        except Exception as ex:
            raise IkologikException("Error while deleting an installation")
