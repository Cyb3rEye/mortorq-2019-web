# mortorq-2019-web
This is the updated Team1515.org website
## Installing
Clone the repository
```
git clone https://github.com/mortorqrobotics/mortorq-2019-web.git
```
Create a Virtual Environment
```
python3 -m virtualenv env
```
Activate the Virtual Environment
```
. env/bin/activate
```
Install Dependencies
```
pip install -r requirements.txt
```
Start up the Flask webserver
```
python start.py
```

### One Command Installation
```
git clone https://github.com/mortorqrobotics/mortorq-2019-web.git && cd mortorq-2019-web && python -m virtualenv env || virtualenv env && source env/bin/activate && pip install -r requirements.txt && cd src && python start.py
```
## Built With
* [Flask](http://flask.pocoo.org/) - Web Microframework for Python
* [Bootstrap](https://getbootstrap.com/) - JS, CSS, HTML Responsive Design Library
