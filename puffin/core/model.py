from ..util import truncate
from flask.ext.security import UserMixin
from enum import Enum
from datetime import datetime


class User(UserMixin):
    
    def __init__(self, login, name, email, password, active, roles, 
            confirmed=False):
        self.login = login
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        if confirmed:
            self.confirmed_at = datetime.now()
    
    @property
    def id(self):
        return self.user_id

    @property
    def roles(self):
        return []

    @roles.setter
    def roles(self, role):
        pass

    @property
    def confirmed(self):
        return self.confirmed_at != None

class Application:
    
    def __init__(self, application_id, path, name, logo, subtitle, website, description, compose, screenshots):
        self.application_id = application_id
        self.path = path
        self.name = name
        self.logo = logo
        self.subtitle = subtitle
        self.website = website
        self.description = description
        self.compose = compose
        self.screenshots = screenshots


class ApplicationStatus(Enum):
    DELETED = 0
    CREATED = 10
    UPDATING = 20
    ERROR = 90


class ApplicationSettings:
    
    def __init__(self, user_id, application_id, settings):
        self.user_id = user_id
        self.application_id = application_id
        self.settings = settings


class Machine:
    
    def __init__(self, url, path):
        self.url = url
        self.path = path

    @property
    def cert(self):
        return self.path + 'cert.pem' if self.path else None
    
    @property
    def key(self):
        return self.path + 'key.pem' if self.path else None
    
    @property
    def ca(self):
        return self.path + 'ca.pem' if self.path else None

