## Setup Virtual Environment

Where ENV is a directory in which to place the new virtual environment.

```
virtualenv ENV
```
Activate virtual environment

```
source ./ENV/bin/activate
```

install requirements with Python 3
```
pip install -r requirements.txt 
```

Start Test Application Server on localhost:5000

```
cd server
python run.py 
```

Demo Request

```
curl -X "POST" "http://localhost:5000/service/yourapiname" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -H 'Cookie: csrfToken=wdlqq9HRpycDNslZx4rgleKI' \
     -d $'{
  "test": "ttttt"
}'
```

*Deactivate virtual environment

```
deactivate
```

## Developement

Add your dependencies in **requirements.txt**

Your API:

```
server/api/
```

Your algorithm:

```
server/algorithm/
```

## Deployment

Run Application Server on Real Environment with Gunicorn

```
gunicorn -c gunicorn.py run:app
```

Or

Deploy your service with [Docker](https://hub.docker.com/editions/community/docker-ce-desktop-mac/)

```
docker-compose up -d --build
```