from IkologikApiCredentials import IkologikApiCredentials
from api.services.AbstractIkologikCustomerService import AbstractIkologikCustomerService


class InstallationService(AbstractIkologikCustomerService):

    def __init__(self, jwtHelper: IkologikApiCredentials):
        super().__init__(jwtHelper)

    # CRUD Actions

    def get_url(self, customer: str):
        return f'{self.jwtHelper.get_url()}/api/v2/customer/{customer}/installation'
