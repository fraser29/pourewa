# POUREWA (formerly OrthancManager)

Python based Orthanc Manager

*pourewa* is the Māori word for tower.

## Installation

```bash
pip install pourewa
```

## Usage

```bash
pourewa --help
```

See full documentation [here](https://fraser29.github.io/pourewa/).

## Info

This is a simple python interface to Orthanc instances. 

It provides commandline level querying and utilities, e.g. upload, download, delete, push etc.

A POUREWA.conf file may be used to set variables applicable to your Orthanc instance to save repeated typing at commandline. 

POUREWA.conf is searched for at:
- os.path.join(rootDir,POUREWA.conf), 
- os.path.join(os.path.expanduser("~"),POUREWA.conf),
- os.path.join(os.path.expanduser("~"),'.'+POUREWA.conf), 
- os.path.join(os.path.expanduser("~"), '.config',POUREWA.conf),
- os.environ.get("POUREWA_CONF", '')

