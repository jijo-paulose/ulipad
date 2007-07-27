#   Programmer: limodou
#   E-mail:     chatme@263.net
#
#   Copyleft 2004 limodou
#
#   Distributed under the terms of the GPL (GNU Public License)
#
#   NewEdit is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   $Id: i18n.py 93 2005-10-11 02:51:02Z limodou $

import gettext
import glob
import os.path
import locale
import codecs
from Debug import error
import gettext
import copy


def install(localedir=None, languages=None):
    _translations = {}
    
    class_ = gettext.GNUTranslations
    path = os.path.join(localedir, languages, '*.mo')
    mofiles = glob.glob(path)
    # TBD: do we need to worry about the file pointer getting collected?
    # Avoid opening, reading, and parsing the .mo file after it's been done
    # once.
    result = None
    for mofile in mofiles:
        key = os.path.abspath(mofile)
        t = _translations.get(key)
        if t is None:
            t = _translations.setdefault(key, class_(open(mofile, 'rb')))
        # Copy the translation object to allow setting fallbacks and
        # output charset. All other instance data is shared with the
        # cached object.
        t = copy.copy(t)
        if result is None:
            result = t
        else:
            result.add_fallback(t)
    return result

class I18n:

    def __init__(self, localedir=None, keyfunc='_'):

        self.translation ={}
        self.localedir = localedir
        self.lang = ''
        self.keyfunc = keyfunc

        self.install(self.lang)

    def _install(self, lang=None):
        if lang is None:
            lang = locale.getdefaultlocale()[0]
            
        self.lang = ''
        if not lang:
            return gettext.NullTranslations()
        else:
            if self.translation.has_key(lang):
                self.lang = lang
                return self.translation[lang]
            else:
                obj = install(self.localedir, lang)
                if obj:
                    self.translation[lang] = obj
                    self.lang = lang
                    return obj
                else:
                    return gettext.NullTranslations()

    def install(self, lang=None):
        obj = self._install(lang)
        
        import __builtin__
        __builtin__.__dict__[self.keyfunc] = unicode and obj.ugettext

    def printall(self):
        for lang, filename in self.translation.items():
            print lang, '=', filename

        print 'default=', self.defaultlang

def makefilename(filename, lang):
    f , e = os.path.splitext(filename)
    newfilename = "%s_%s%s" % (f, lang, e)
    if os.path.exists(newfilename):
        return newfilename
    else:
        return filename

if __name__ == '__main__':
    a = I18n('i18ntest', './lang')
    a.printall()

