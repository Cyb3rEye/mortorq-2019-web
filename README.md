# Mortorq 2019 Web
This is the updated Team1515.org website
## Installing

### Quick Host + Installation Command (For use if using Flask Server)
```
git clone https://github.com/mortorqrobotics/mortorq-2019-web.git && cd mortorq-2019-web && python -m virtualenv env || virtualenv env && source env/bin/activate && pip install -r requirements.txt && cd src && flask run --port 80
```

### To generate full HTML files (For use if using traditional web servers)
```
python freeze.py
```

The build files will be in /src/build

### Manual Installation

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

## Built With
* [Flask](http://flask.pocoo.org/) - Web Microframework for Python
* [Bootstrap](https://getbootstrap.com/) - JS, CSS, HTML Responsive Design Library
