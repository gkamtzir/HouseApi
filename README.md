# HouseApi

This repo consists of the backend codebase I'm developing for the 3rd deliverable of a 3 part exercice for the course of Databases. This course is part of the Electrical Engineering and Computer Engineering undergraduate program at Aristotle University of Thessaloniki.

The actual API is live on http://83.212.115.201/api/.<br />
The documentation is live on http://83.212.115.201/api/documentation/.

## Technical Notes
The 'House' API is a RESTful API which is built using Python 3 and Flask Microframework. It makes use of the Flask-RESTful extension, which helps build more organized and structured APIs, and the SQLAlchemy toolkit as the Object Relational Mapper. Lastly, there is an email-only authentication system based on JWT.

### Installation Guide

##### Clone the repo
```
$ git clone https://github.com/gkamtzir/HouseApi.git
$ cd HouseApi
```

##### Install Requirements
```
$ pip3 install -r requirements.txt
```

##### Database Configuration
Visit [HouseDB](https://github.com/gkamtzir/HouseDB) repo, download *housedb.sql* and import it on a MariaDB server. Make sure to modify database's user and password in *config.py* file to match your credentials.

##### Code Modifications
Replace *JWT_SECRET_KEY* in *config.py* with your own. For example, you can do:
```python
import os
os.urandom(24)
```
Alternatively, you can leave it as is. It's not secure though.

##### Run the API
```
$ py ./run.py
```
