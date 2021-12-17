import os
import time

from ikologikapi.IkologikApi import IkologikAPI

api = IkologikAPI(
    url=os.getenv('URL'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
)

## Load the customer id
customerId = os.getenv('CUSTOMER')

counter = 0
while counter < 20:
    installations = api.installation.list(customerId)
    print("Found " + str(len(installations)) + " installations")
    time.sleep(2)
    counter += 1

print('')
