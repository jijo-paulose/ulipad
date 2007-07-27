#	Programmer:	limodou
#	E-mail:		chatme@263.net
#
#	Copyleft 2004 limodou
#
#	Distributed under the terms of the GPL (GNU Public License)
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
#	$Id: mWindow.py 93 2005-10-11 02:51:02Z limodou $

from modules import Mixin
import wx
import os.path
from modules import common

menulist = [(None,
	[
		(700, 'IDM_WINDOW', tr('Window'), wx.ITEM_NORMAL, '', ''),
	]),
	('IDM_WINDOW',
	[
		(100, 'IDM_WINDOW_LEFT', tr('Left Window'), wx.ITEM_CHECK, 'OnWindowLeft', tr('Shows or hides the left Window')),
		(110, 'IDM_WINDOW_BOTTOM', tr('Bottom Window'), wx.ITEM_CHECK, 'OnWindowBottom', tr('Shows or hides the bottom Window')),
		(120, '-', '', wx.ITEM_SEPARATOR, '', ''),
		(130, 'IDM_WINDOW_SHELL', tr('Open Shell Window'), wx.ITEM_NORMAL, 'OnWindowShell', tr('Opens shell window.')),
		(140, 'IDM_WINDOW_MESSAGE', tr('Open Message Window'), wx.ITEM_NORMAL, 'OnWindowMessage', tr('Opens message window.')),
	]),
]
Mixin.setMixin('mainframe', 'menulist', menulist)


def OnWindowLeft(win, event):
	flag = not win.panel.LeftIsVisible

	if flag:
		win.createSnippetWindow()

	win.panel.showWindow('left', flag)
Mixin.setMixin('mainframe', 'OnWindowLeft', OnWindowLeft)

def OnWindowBottom(win, event):
	flag = not win.panel.BottomIsVisible
	if flag:
		win.createShellWindow()
		win.createMessageWindow()

	win.panel.showWindow('bottom', flag)
Mixin.setMixin('mainframe', 'OnWindowBottom', OnWindowBottom)

def OnUpdateUI(win, event):
	eid = event.GetId()
	if eid == win.IDM_WINDOW_LEFT:
		event.Check(win.panel.LeftIsVisible)
	elif eid == win.IDM_WINDOW_BOTTOM:
		event.Check(win.panel.BottomIsVisible)
Mixin.setPlugin('mainframe', 'on_update_ui', OnUpdateUI)

def afterinit(win):
	wx.EVT_UPDATE_UI(win, win.IDM_WINDOW_LEFT, win.OnUpdateUI)
	wx.EVT_UPDATE_UI(win, win.IDM_WINDOW_BOTTOM, win.OnUpdateUI)
	win.messagewindow = None
	win.shellwindow = None
Mixin.setPlugin('mainframe', 'afterinit', afterinit)

toollist = [
	(450, 'left'),
	(500, 'bottom'),
]
Mixin.setMixin('mainframe', 'toollist', toollist)

#order, IDname, imagefile, short text, long text, func
toolbaritems = {
	'left':(wx.ITEM_CHECK, 'IDM_WINDOW_LEFT', common.unicode_abspath('images/left.gif'), tr('Left Window'), tr('Shows or hides the left Window'), 'OnViewToolWindowLeft'),
	'bottom':(wx.ITEM_CHECK, 'IDM_WINDOW_BOTTOM', common.unicode_abspath('images/bottom.gif'), tr('Bottom Window'), tr('Shows or hides the bottom Window'), 'OnViewToolWindowBottom'),
}
Mixin.setMixin('mainframe', 'toolbaritems', toolbaritems)

def createShellWindow(win):
	if not win.panel.getPage(tr('Shell')):
		from ShellWindow import ShellWindow

		page = ShellWindow(win.panel.createNotebook('bottom'), win)
		win.panel.addPage('bottom', page, tr('Shell'))
	win.shellwindow = win.panel.getPage(tr('Shell'))
Mixin.setMixin('mainframe', 'createShellWindow', createShellWindow)

def createMessageWindow(win):
	if not win.panel.getPage(tr('Message')):
		from MessageWindow import MessageWindow

		page = MessageWindow(win.panel.createNotebook('bottom'), win)
		win.panel.addPage('bottom', page, tr('Message'))
	win.messagewindow = win.panel.getPage(tr('Message'))
Mixin.setMixin('mainframe', 'createMessageWindow', createMessageWindow)

def OnWindowShell(win, event):
	win.createShellWindow()
	win.panel.showPage(tr('Shell'))
Mixin.setMixin('mainframe', 'OnWindowShell', OnWindowShell)

def OnWindowMessage(win, event):
	win.createMessageWindow()
	win.panel.showPage(tr('Message'))
Mixin.setMixin('mainframe', 'OnWindowMessage', OnWindowMessage)

popmenulist = [ (None,
	[
		(120, 'IDPM_SHELLWINDOW', tr('Open Shell Window'), wx.ITEM_NORMAL, 'OnShellWindow', tr('Opens shell window.')),
		(130, 'IDPM_MESSAGEWINDOW', tr('Open Message Window'), wx.ITEM_NORMAL, 'OnMessageWindow', tr('Opens message window.')),
	]),
]
Mixin.setMixin('notebook', 'popmenulist', popmenulist)

def OnShellWindow(win, event):
	win.mainframe.createShellWindow()
	win.panel.showPage(tr('Shell'))
Mixin.setMixin('notebook', 'OnShellWindow', OnShellWindow)

def OnMessageWindow(win, event):
	win.mainframe.createMessageWindow()
	win.panel.showPage(tr('Message'))
Mixin.setMixin('notebook', 'OnMessageWindow', OnMessageWindow)

