# Ikologik API

### Who is Ikologik?
Ikologik is a reliable partner for process monitoring in the industry. With software for visualisation, 
reporting and smart analysis of various process data, we bring the performance of your production 
facilities constantly into focus.

### The REST API
The Ikologik platform offers a REST API to automate and manage your data logging environment. 
Through the API, you can closely integrate your data logging environment with other production 
systems and exchange data from and to the Ikologik platform. To be able to invoke requests to 
the REST API, you need to request a JWT token by using your Ikologik credentials.

### Build and deploy
To build the project, run following command:

`./venv/bin/python setup.py bdist_wheel`

After the build has been completed, add the possiblity to use twine by running:

`./venv/bin/python -m pip install --upgrade twine`

To upload the project to Pypi:

`./venv/bin/twine upload dist/*`

During the upload, your Pypi credentials will be requested.