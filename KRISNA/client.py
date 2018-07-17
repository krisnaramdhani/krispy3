# -*- coding: utf-8 -*-
from .auth import Auth
from .models import Models
from .talk import Talk
from .square import Square
from .call import Call
from .timeline import Timeline
from akad.ttypes import Message

class KRIS(Auth, Models, Talk, Square, Call, Timeline):

    def __init__(self, authTokenCAB=None, passwd=None, certificate=None, systemName=None, appName=None, showQr=False, keepLoggedIn=True):
        
        Auth.__init__(self)
        if not (authTokenCAB or authTokenCAB and passwd):
            self.loginWithQrCode(keepLoggedIn=keepLoggedIn, systemName=systemName, appName=appName, showQr=showQr)
        if authTokenCAB and passwd:
            self.loginWithCredential(_id=authTokenCAB, passwd=passwd, certificate=certificate, systemName=systemName, appName=appName, keepLoggedIn=keepLoggedIn)
        elif authTokenCAB and not passwd:
            self.loginWithAuthToken(authToken=authTokenCAB, appName=appName)

        self.__initAll()

    def __initAll(self):

        self.profile    = self.talk.getProfile()
        self.groups     = self.talk.getGroupIdsJoined()

        Models.__init__(self)
        Talk.__init__(self)
        Square.__init__(self)
        Call.__init__(self)
        Timeline.__init__(self)