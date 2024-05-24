# Python-StressTest
Stress test with python send requests

## Installation

`
python3 - venv venv
`


## Activate Environment 

`
source venv/bin/activate
`

## Upgrad PIP if you want to upgrade the version to latest

`
pip install --upgrade pip
`

## Install dependencies

`
pip install locust
`

## Start run scrap

Put the website url in file `start_stress.py` you want to send requests and then run the following command:

`
locust -f start_stress.py
`

## Create a requirements.txt

`
pip freeze > requirements.txt
`
