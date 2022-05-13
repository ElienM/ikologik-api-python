import json
from types import SimpleNamespace

import requests

from ikologikapi.IkologikApiCredentials import IkologikApiCredentials
from ikologikapi.IkologikException import IkologikException


class GraphService:
    def __init__(self, jwtHelper: IkologikApiCredentials):
        self.jwtHelper = jwtHelper

    # CRUD Actions

    def get_headers(self, headers=None):
        default_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.jwtHelper.get_jwt()}'
        }
        if headers is not None:
            default_headers.update(headers)
        return default_headers

    def get_url(self, installation: str, id: str) -> str:
        return f'{self.jwtHelper.get_url()}/api/v1/installation/{installation}/graphmeter/{id}/graph/data'

    def get_graph_meter_list(self, installation):
        pass

    def search_graph_meter_list(self, installation, search):
        pass

    def get_active_meter_list(self, installation):
        pass

    def search_active_meter_list(self, installation, search):
        pass

    def get_graph_meter(self, installation, meter_id):
        pass

    def get_data(self, installation, meter_id, start_date, end_date):
        pass

    def get_data_with_data_type(self, installation, meter_id, data_type, start_date, end_date):
        pass

    def get_graph_data(self, installation, meter_id, data_type, start_date, end_date):
        try:
            response = requests.get(
                self.get_url(installation, meter_id) + f'/{data_type}/{start_date}/{end_date}',
                headers=self.get_headers()
            )
            if response.status_code == 200:
                result = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
                return result
            else:
                raise IkologikException("Error while performing get_data, the request returned status " + str(response.status_code))
        except IkologikException as ex:
            raise ex
        except Exception as ex:
            raise IkologikException("Error while performing get_by_id")

    def get_graph_alerts(self, installation, meter_id, data_type, start_date, end_date):
        pass

    def get_graph_navigator_data_list(self, installation, meter_id, data_type, start_date, end_date):
        pass

