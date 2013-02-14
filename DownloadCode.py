#!/usr/bin/python3
# -*- coding: utf8 -*-

import cherrypy
import CheckCode

class DownloadCode:


    
    def index(self):
        # Hier ist die Index-Whatever

        return '<form action="CheckCode" method="post"> \
                    <p>Wie lautet dein Download-Code?</p> \
                    <input type="text" name="code" value="" \
                        size="15" maxlength="40"/> \
                    <p><input type="submit" value="Überprüfe den Code"/></p> \
                </form>'
        # Der Code wird als "code" string an die checkCode Seite übergeben
    index.exposed = True
    



    def CheckCode(self, code=None):
        self.check=CheckCode.check(code)
        self.count=CheckCode.count(code)

        # aus dem Code wird zunächst die Gültigkeit 
        # des Codes abgefragt und die Anzahl wie oft
        # er schon verwendet wurde.

        self.code=code
        if self.check == 0:
            return "Dein Code ist falsch"
        elif self.check == 2:
            return "Das Maximum an 5 Downloads ist erreicht. du solltest eine weitere Platte kaufen!"
        elif self.check == 1:
            return '<form action="Download" method="post"> \
                    <p>Dein Code wurde  '+ self.count +' von 5 Malen verwendet </p> \
                    <p><input type="submit" value="Download"/></p> \
                    </form>'
        else:
            return "Da ist was schief gegangen... :("
        
        # Wenn der Code ungültig oder abgelaufen ist geht es nciht weiter
        # ist der code gültig, dann gehts weiter zur Downloadseite
    CheckCode.exposed = True





    def Download(self, check=None, code=None):
        # hier ist die Downloadseite
        # Besser nocheinmal die Gültigkeit vom Code checken,
        # denn diese Seite kann auch so aufgerufen werden und
        # soll dann keine Datei streamen :D
        if self.check == 1:
            CheckCode.CodeAnzahlVerringern(code)
            datei="/home/matto/python/cherrypy/tutorial/downloadcode/test.zip"
            return cherrypy.lib.static.serve_file(datei, content_type=None, disposition=None, name="DAMNiAM-MADAMIN.zip", debug=False) 
        else:
            return "Da ist was schief gegangen.... "
    Download.exposed = True


# Hier wird der Murks zum laufen gebracht
cherrypy.quickstart(DownloadCode())
