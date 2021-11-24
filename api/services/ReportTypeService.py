from IkologikApiCredentials import IkologikApiCredentials
from api.services.AbstractIkologikInstallationService import AbstractIkologikInstallationService


class ReportTypeService(AbstractIkologikInstallationService):

    def __init__(self, jwtHelper: IkologikApiCredentials):
        super().__init__(jwtHelper)

    # CRUD Actions

    def get_url(self, customer: str, installation: str):
        return f'{self.jwtHelper.get_url()}/api/v2/customer/{customer}/installation/{installation}/reporttype'
