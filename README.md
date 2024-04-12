# OrthancManager

Python based Orthanc Manager

## Info

This is a simple python interface to Orthanc instances. 

It provides commandline level querying and utilities, e.g. upload. 

A OrthancManager.conf file may be used to set variables applicable to your Orthanc instance to save repeated typing at commandline. 

OrthancManager.conf is searched for at:
- os.path.join(rootDir,OrthancManager.conf), 
- os.path.join(os.path.expanduser("~"),OrthancManager.conf),
- os.path.join(os.path.expanduser("~"),'.'+OrthancManager.conf), 
- os.path.join(os.path.expanduser("~"), '.config',OrthancManager.conf),
- os.environ.get("OrthancManager_CONF", '')
