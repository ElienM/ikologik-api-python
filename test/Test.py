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

## Login
print('## Logging-in ##')
api.login()
print('')

## Get customer
print('## Customer ##')
customer = api.customer.get_by_id(customerId)
print(customer.name)
print('')

## List installations
print('## Installations ##')
installations = api.installation.list(customerId)
for installation in installations:
    print(installation.name)
print('')

## List tags
print('## Tags ##')
tags = api.tag.list(customerId, installationId)
for tag in tags:
    print(tag.name)
print('')

## List dashboards
print('## Dashboards ##')
dashboards = api.dashboard.list(customerId, installationId)
for dashboard in dashboards:
    print(dashboard.name)
print('')

## List dashboard widget types
print('## Dashboard widget type ##')
dashboardWidgetTypes = api.dashboardWidgetType.list()
for dashboardWidgetType in dashboardWidgetTypes:
    print(dashboardWidgetType.name)
print('')

## List data import types
print('## Data import type ##')
dataImportTypes = api.dataImportType.list(customerId, installationId)
for dataImportType in dataImportTypes:
    print(dataImportType.name)
print('')

## Get meter graph

print('## Get meter graph')
graphMeter = api.graph.get_data(installationId, tag, 1652392800000, 1652479200000)
print(graphMeter)

graphMeter = api.graph.get_data_with_data_type(installationId, tag, 'DATA', 1652392800000, 1652479200000)
print(graphMeter)

## Get graph data

print('## Get meter graph data')
graphMeterData = api.graph.get_graph_data(installationId, tag, 'DATA', 1652392800000, 1652479200000, 50)
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


