#!/usr/bin/python
# -*- coding: utf8 -*-

import cherrypy
import CheckCode

class DownloadCode:
    
    def index(self):
        # Let's link to another method here.
        return '<form action="CheckCode" method="post"> \
                    <p>Wie lautet dein Download-Code?</p> \
                    <input type="text" name="code" value="" \
                        size="15" maxlength="40"/> \
                    <p><input type="submit" value="Überprüfe den Code"/></p> \
                </form>'
    index.exposed = True
    
    def CheckCode(self, code=None):
        self.check=CheckCode.check(code)
        self.count=CheckCode.count(code)
        if self.check == 0:
            return "Dein Code ist falsch"
        elif self.check == 1:
            return '<form action="Download" method="post"> \
                    <p>Dein Code wurde  '+ self.count +' von 5 Malen verwendet </p> \
                    <p><input type="submit" value="Download"/></p> \
                    </form>'
        else:
            return "Da ist was schief gegangen.... check=" + str(self.check) + " count=" + str(self.count) + " code=" + code
    CheckCode.exposed = True

    def Download(self, check=None, code=None):
        if check == 1:
            CheckCode.CodeAnzahlVerringern(code)
            datei="/home/matto/python/cherrypy/tutorial/test.zip"
            return cherrypy.lib.static.serve_file(datei, content_type=None, disposition=None, name="DAMNiAM-MADAMIN.zip", debug=False) 
        else:
            return "Da ist was schief gegangen.... check=" + str(self.check) + " count=" + str(self.count) + " code=" + code
    Download.exposed = True



cherrypy.quickstart(DownloadCode())
