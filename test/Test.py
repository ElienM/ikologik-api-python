import datetime
import os

from ikologikapi.IkologikApi import IkologikAPI

## Prepare the API
from ikologikapi.dataiterator.GraphDataIterator import GraphDataIterator
from ikologikapi.domain.Search import Search

api = IkologikAPI(
    url=os.getenv('URL'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
)

## Load the customer and installation id's
customerId = os.getenv('CUSTOMER')
installationId = os.getenv('INSTALLATION')
dataImportTypeId = os.getenv('DATAIMPORTTYPE')
dataImportId = os.getenv('DATAIMPORT')
tag = os.getenv('TAG')
second_tag = os.getenv('TAG2')
maintenance_type_id = os.getenv('MAINTENANCE_TYPE')
maintenance_type_field_id = os.getenv('MAINTENANCE_TYPE_FIELD_TYPE')
maintenance_task = os.getenv('MAINTENANCE_TASK')

# ## Login
# print('## Logging-in ##')
# api.login()
# print('')
#
# ## Get customer
# print('## Customer ##')
# customer = api.customer.get_by_id(customerId)
# print(customer.name)
# print('')
#
# ## List installations
# print('## Installations ##')
# installations = api.installation.list(customerId)
# for installation in installations:
#     print(installation.name)
# print('')
#
# ## List tags
# print('## Tags ##')
# tags = api.tag.list(customerId, installationId)
# for tag in tags:
#     print(tag.name)
# print('')
#
# ## List dashboards
# print('## Dashboards ##')
# dashboards = api.dashboard.list(customerId, installationId)
# for dashboard in dashboards:
#     print(dashboard.name)
# print('')
#
# ## List dashboard widget types
# print('## Dashboard widget type ##')
# dashboardWidgetTypes = api.dashboardWidgetType.list()
# for dashboardWidgetType in dashboardWidgetTypes:
#     print(dashboardWidgetType.name)
# print('')
#
# ## List data import types
# print('## Data import type ##')
# dataImportTypes = api.dataImportType.list(customerId, installationId)
# for dataImportType in dataImportTypes:
#     print(dataImportType.name)
# print('')

## Get meter graph

print('## Get meter graph')
graphMeter = api.graph.get_data(installationId, tag, 1652392800000, 1652479200000)
print(graphMeter)

graphMeter = api.graph.get_data_with_data_type(installationId, tag, 'DATA', 1652392800000, 1652479200000)
print(graphMeter)

## Get graph data

print('## Get meter graph data')
graphMeterData = api.graph.get_graph_data(installationId, tag, 'DATA', 1652392800000, 1652479200000, 50, False)
print(graphMeterData)

## Graph data iterator

tags = [{'id': tag}, {'id': second_tag}]

graphDataIterator = GraphDataIterator(installationId, 1652392800000, 1652479200000, api)
graphDataIterator.add_meters(tags)
graphDataIterator.init()


counter = 0
while graphDataIterator.has_next():
    graphDataIterator.next()

    for tag in tags:
        data = graphDataIterator.get_meter_data(tag['id'])

        print(f'Tag: {tag["id"]}, Date: {datetime.datetime.fromtimestamp(data.date/1000)}, Value: {data.value}')

## Maintenance type

print('## Get maintenance type list')
mt_list = api.maintenanceType.list(customerId)
print(mt_list)

print('## Get maintenance type')
mt = api.maintenanceType.get_by_id(customerId, maintenance_type_id)
print(mt)

print('## Get maintenance type field type list')
mtft_list = api.maintenanceTypeFieldType.list(customerId, maintenance_type_id)
print(mtft_list)

print('## Get maintenance type field type')
mtft = api.maintenanceTypeFieldType.get_by_id(customerId, maintenance_type_id, maintenance_type_field_id)
print(mtft)

## Maintenance task

print('## Get maintenance tasks')
mt_list = api.maintenanceTask.list(customerId, installationId)
print(mt_list)

print('## Get maintenance task')
mt = api.maintenanceTask.get_by_id(customerId, installationId, maintenance_task)
print(mt)

print('## Get maintenance task update')
mt = api.maintenanceTask.update_status(customerId, installationId, maintenance_task, 'STATUS_4_FINISHED')
print(mt)





