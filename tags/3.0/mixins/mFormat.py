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
#	$Id: mFormat.py 111 2005-10-16 10:10:27Z limodou $

from modules import Mixin
import wx
import wx.stc
import os.path
from modules import common

menulist = [ ('IDM_EDIT',
	[
		(250, 'IDM_EDIT_FORMAT', tr('Format'), wx.ITEM_NORMAL, None, ''),
	]),
	('IDM_EDIT_FORMAT',
	[
		(100, 'IDM_EDIT_FORMAT_CHOP', tr('Trim Trailing Spaces'), wx.ITEM_NORMAL, 'OnEditFormatChop', tr('Trims trailing white spaces')),
		(110, 'IDM_EDIT_FORMAT_SPACETOTAB', tr('Leading Spaces to Tabs'), wx.ITEM_NORMAL, 'OnEditFormatSpaceToTab', tr('Converts leading spaces to tabs')),
		(120, 'IDM_EDIT_FORMAT_TABTOSPACE', tr('Leading Tabs To Spaces'), wx.ITEM_NORMAL, 'OnEditFormatTabToSpace', tr('Converts leading tabs to spaces')),
		(125, 'IDM_EDIT_FORMAT_ALLTABTOSPACE', tr('ALL Tabs To Spaces'), wx.ITEM_NORMAL, 'OnEditFormatAllTabToSpace', tr('Converts all tabs to spaces')),
		(130, '', '-', wx.ITEM_SEPARATOR, None, ''),
		(140, 'IDM_EDIT_FORMAT_INDENT', tr('Increase Indent') + '\tE=Ctrl+I', wx.ITEM_NORMAL, 'OnEditFormatIndent', tr('Increases the indentation of current line or selected block')),
		(150, 'IDM_EDIT_FORMAT_UNINDENT', tr('Decrease Indent') + '\tE=Ctrl+Shift+I', wx.ITEM_NORMAL, 'OnEditFormatUnindent', tr('Decreases the indentation of current line or selected block')),
		(160, '', '-', wx.ITEM_SEPARATOR, None, ''),
		(170, 'IDM_EDIT_FORMAT_COMMENT', tr('Line Comment...') + '\tE=Ctrl+/', wx.ITEM_NORMAL, 'OnEditFormatComment', tr('Inserts comment sign at the beginning of line')),
		(180, 'IDM_EDIT_FORMAT_UNCOMMENT', tr('Line Uncomment...') + '\tE=Ctrl+\\', wx.ITEM_NORMAL, 'OnEditFormatUncomment', tr('Removes comment sign at the beginning of line')),
		(190, '', '-', wx.ITEM_SEPARATOR, None, ''),
		(200, 'IDM_EDIT_FORMAT_QUOTE', tr('Text Quote...') + '\tE=Ctrl+Q', wx.ITEM_NORMAL, 'OnEditFormatQuote', tr('Quote selected text')),
		(210, 'IDM_EDIT_FORMAT_UNQUOTE', tr('Text Unquote...') + '\tE=Ctrl+Shift+Q', wx.ITEM_NORMAL, 'OnEditFormatUnquote', tr('Unquote selected text')),
	]),
]
Mixin.setMixin('mainframe', 'menulist', menulist)

popmenulist = [ (None, #parent menu id
	[
		(220, 'IDPM_FORMAT', tr('Format'), wx.ITEM_NORMAL, None, ''),
	]),
	('IDPM_FORMAT',
	[
		(100, 'IDPM_FORMAT_CHOP', tr('Trim Trailing Spaces'), wx.ITEM_NORMAL, 'OnFormatChop', tr('Trims trailing white spaces')),
		(110, 'IDPM_FORMAT_SPACETOTAB', tr('Leading Spaces to Tabs'), wx.ITEM_NORMAL, 'OnFormatSpaceToTab', tr('Converts leading spaces to tabs')),
		(120, 'IDPM_FORMAT_TABTOSPACE', tr('Leading Tabs To Spaces'), wx.ITEM_NORMAL, 'OnFormatTabToSpace', tr('Converts leading tabs to spaces')),
		(125, 'IDPM_FORMAT_ALLTABTOSPACE', tr('ALL Tabs To Spaces'), wx.ITEM_NORMAL, 'OnFormatAllTabToSpace', tr('Converts all tabs to spaces')),
		(130, '', '-', wx.ITEM_SEPARATOR, None, ''),
		(140, 'IDPM_FORMAT_INDENT', tr('Increase Indent') + '\tCtrl+I', wx.ITEM_NORMAL, 'OnFormatIndent', tr('Increases the indentation of current line or selected block')),
		(150, 'IDPM_FORMAT_UNINDENT', tr('Decrease Indent') + '\tCtrl+Shift+I', wx.ITEM_NORMAL, 'OnFormatUnindent', tr('Decreases the indentation of current line or selected block')),
		(160, '', '-', wx.ITEM_SEPARATOR, None, ''),
		(170, 'IDPM_FORMAT_COMMENT', tr('Line Comment...') + '\tCtrl+/', wx.ITEM_NORMAL, 'OnFormatComment', tr('Inserts comment sign at the beginning of line')),
		(180, 'IDPM_FORMAT_UNCOMMENT', tr('Line Uncomment...') + '\tCtrl+\\', wx.ITEM_NORMAL, 'OnFormatUncomment', tr('Removes comment sign at the beginning of line')),
		(190, '', '-', wx.ITEM_SEPARATOR, None, ''),
		(200, 'IDPM_FORMAT_QUOTE', tr('Text Quote...') + '\tCtrl+Q', wx.ITEM_NORMAL, 'OnFormatQuote', tr('Quote selected text')),
		(210, 'IDPM_FORMAT_UNQUOTE', tr('Text Unquote...') + '\tCtrl+Shift+Q', wx.ITEM_NORMAL, 'OnFormatUnquote', tr('Unquote selected text')),
	]),
]
Mixin.setMixin('editor', 'popmenulist', popmenulist)

imagelist = {
	'IDM_EDIT_FORMAT_INDENT':common.unicode_abspath('images/indent.gif'),
	'IDM_EDIT_FORMAT_UNINDENT':common.unicode_abspath('images/unindent.gif'),
}
Mixin.setMixin('mainframe', 'imagelist', imagelist)

imagelist = {
	'IDPM_FORMAT_INDENT':common.unicode_abspath('images/indent.gif'),
	'IDPM_FORMAT_UNINDENT':common.unicode_abspath('images/unindent.gif'),
}
Mixin.setMixin('editor', 'imagelist', imagelist)

#toollist = [
#	(840, '|'),
#	(850, 'indent'),
#	(860, 'unindent'),
#]
#Mixin.setMixin('mainframe', 'toollist', toollist)
#
##order, IDname, imagefile, short text, long text, func
#toolbaritems = {
#	'indent':(wx.ITEM_NORMAL, 'IDM_EDIT_FORMAT_INDENT', common.unicode_abspath('images/indent.gif'), tr('indent'), tr('Increases the indentation of current line or selected block'), 'OnEditFormatIndent'),
#	'unindent':(wx.ITEM_NORMAL, 'IDM_EDIT_FORMAT_UNINDENT', common.unicode_abspath('images/unindent.gif'), tr('unindent'), tr('Decreases the indentation of current line or selected block'), 'OnEditFormatUnindent'),
#}
#Mixin.setMixin('mainframe', 'toolbaritems', toolbaritems)
#

def OnEditFormatIndent(win, event):
	win.document.CmdKeyExecute(wx.stc.STC_CMD_TAB)
Mixin.setMixin('mainframe', 'OnEditFormatIndent', OnEditFormatIndent)

def OnEditFormatUnindent(win, event):
	win.document.CmdKeyExecute(wx.stc.STC_CMD_BACKTAB)
Mixin.setMixin('mainframe', 'OnEditFormatUnindent', OnEditFormatUnindent)

def OnFormatIndent(win, event):
	win.CmdKeyExecute(wx.stc.STC_CMD_TAB)
Mixin.setMixin('editor', 'OnFormatIndent', OnFormatIndent)

def OnFormatUnindent(win, event):
	win.CmdKeyExecute(wx.stc.STC_CMD_BACKTAB)
Mixin.setMixin('editor', 'OnFormatUnindent', OnFormatUnindent)

def OnFormatQuote(win, event):
	win.mainframe.OnEditFormatQuote(event)
Mixin.setMixin('editor', 'OnFormatQuote', OnFormatQuote)

def OnFormatUnquote(win, event):
	win.mainframe.OnEditFormatUnquote(event)
Mixin.setMixin('editor', 'OnFormatUnquote', OnFormatUnquote)

def init(pref):
	pref.tabwidth = 4
	pref.last_comment_chars = '#'
Mixin.setPlugin('preference', 'init', init)

preflist = [
	(tr('Document'), 140, 'num', 'tabwidth', tr('Tab width:'), None),
]
Mixin.setMixin('preference', 'preflist', preflist)

def init(win):
	#set tab width
	win.SetTabWidth(win.mainframe.pref.tabwidth)
Mixin.setPlugin('editor', 'init', init)

def savepreference(mainframe, pref):
	for document in mainframe.editctrl.list:
		document.SetTabWidth(mainframe.pref.tabwidth)
Mixin.setPlugin('prefdialog', 'savepreference', savepreference)

def OnEditFormatChop(win, event):
	for i in win.document.getSelectionLines():
		text = win.document.getLineText(i)
		newtext = text.rstrip()
		win.document.replaceLineText(i, newtext)
Mixin.setMixin('mainframe', 'OnEditFormatChop', OnEditFormatChop)

def OnFormatChop(win, event):
	win.mainframe.OnEditFormatChop(event)
Mixin.setMixin('editor', 'OnFormatChop', OnFormatChop)

def OnEditFormatComment(win, event):
	from modules import Entry

	dlg = Entry.MyTextEntry(win, tr("Comment..."), tr("Comment Char:"), win.pref.last_comment_chars)
	answer = dlg.ShowModal()
	if answer == wx.ID_OK:
		commentchar = dlg.GetValue()
		if len(commentchar) == 0:
			return
		win.pref.last_comment_chars = commentchar
		win.pref.save()
		for i in win.document.getSelectionLines():
			text = win.document.getLineText(i)
			win.document.replaceLineText(i, commentchar + text)
Mixin.setMixin('mainframe', 'OnEditFormatComment', OnEditFormatComment)

def OnFormatComment(win, event):
	win.mainframe.OnEditFormatComment(event)
Mixin.setMixin('editor', 'OnFormatComment', OnFormatComment)

def OnEditFormatUncomment(win, event):
	from modules import Entry

	dlg = Entry.MyTextEntry(win, tr("Comment..."), tr("Comment Char:"), win.pref.last_comment_chars)
	answer = dlg.ShowModal()
	if answer == wx.ID_OK:
		commentchar = dlg.GetValue()
		if len(commentchar) == 0:
			return
		win.pref.last_comment_chars = commentchar
		win.pref.save()
		for i in win.document.getSelectionLines():
			text = win.document.getLineText(i)
			if text.startswith(commentchar):
				win.document.replaceLineText(i, text[len(commentchar):])
Mixin.setMixin('mainframe', 'OnEditFormatUncomment', OnEditFormatUncomment)

def OnFormatUncomment(win, event):
	win.mainframe.OnEditFormatUncomment(event)
Mixin.setMixin('editor', 'OnFormatUncomment', OnFormatUncomment)

def OnEditFormatSpaceToTab(win, event):
	for i in win.document.getSelectionLines():
		tabwidth = win.document.GetTabWidth()
		text = win.document.getLineText(i).expandtabs(tabwidth)
		k = 0
		for ch in text:
			if ch == ' ':
				k += 1
			else:
				break
		n, m = divmod(k, tabwidth)
		newtext = '\t'*n + ' '*m + text[k:]
		win.document.replaceLineText(i, newtext)
Mixin.setMixin('mainframe', 'OnEditFormatSpaceToTab', OnEditFormatSpaceToTab)

def OnFormatSpaceToTab(win, event):
	win.mainframe.OnEditFormatSpaceToTab(event)
Mixin.setMixin('editor', 'OnFormatSpaceToTab', OnFormatSpaceToTab)

def OnEditFormatAllTabToSpace(win, event):
	for i in win.document.getSelectionLines():
		tabwidth = win.document.GetTabWidth()
		text = win.document.getLineText(i).expandtabs(tabwidth)
		win.document.replaceLineText(i, text)
Mixin.setMixin('mainframe', 'OnEditFormatAllTabToSpace', OnEditFormatAllTabToSpace)

def OnFormatAllTabToSpace(win, event):
	win.mainframe.OnEditFormatAllTabToSpace(event)
Mixin.setMixin('editor', 'OnFormatAllTabToSpace', OnFormatAllTabToSpace)

def OnEditFormatTabToSpace(win, event):
	for i in win.document.getSelectionLines():
		tabwidth = win.document.GetTabWidth()
		text = win.document.getLineText(i)
		k = 0
		for j, ch in enumerate(text):
			if ch == '\t':
				k += 1
			else:
				break
		text = ' '*k*tabwidth + text[j:]
		win.document.replaceLineText(i, text)
Mixin.setMixin('mainframe', 'OnEditFormatTabToSpace', OnEditFormatTabToSpace)

def OnFormatTabToSpace(win, event):
	win.mainframe.OnEditFormatTabToSpace(event)
Mixin.setMixin('editor', 'OnFormatTabToSpace', OnFormatTabToSpace)

def init(win):
	win.quote_user = False
	win.quote_index = 0
	win.quote_start = ''
	win.quote_end = ''
	win.quoteresfile = common.unicode_abspath('resources/quotedialog.xrc')
Mixin.setPlugin('mainframe', 'init', init)

def OnEditFormatQuote(win, event):
	from modules import Resource
	import QuoteDialog
	from modules import i18n

	text = win.document.GetSelectedText()
	if len(text) > 0:
		filename = i18n.makefilename(win.quoteresfile, win.app.i18n.lang)
		dlg = Resource.loadfromresfile(filename, win, QuoteDialog.MyQuoteDialog, 'QuoteDialog', win)
		answer = dlg.ShowModal()
		dlg.Destroy()
		if answer == wx.ID_OK:
			if win.quote_user:
				start = win.quote_start
				end = win.quote_end
			else:
				start, end = QuoteDialog.quote_string[win.quote_index]
			win.document.ReplaceSelection(start + text + end)
Mixin.setMixin('mainframe', 'OnEditFormatQuote', OnEditFormatQuote)

def OnEditFormatUnquote(win, event):
	from modules import Resource
	import QuoteDialog
	from modules import i18n

	text = win.document.GetSelectedText()
	if len(text) > 0:
		filename = i18n.makefilename(win.quoteresfile, win.app.i18n.lang)
		dlg = Resource.loadfromresfile(filename, win, QuoteDialog.MyQuoteDialog, 'QuoteDialog', win)
		answer = dlg.ShowModal()
		dlg.Destroy()
		if answer == wx.ID_OK:
			if win.quote_user:
				start = win.quote_start
				end = win.quote_end
			else:
				start, end = QuoteDialog.quote_string[win.quote_index]
			win.document.ReplaceSelection(text[len(start):-len(end)])
Mixin.setMixin('mainframe', 'OnEditFormatUnquote', OnEditFormatUnquote)

def init(win):
	wx.EVT_UPDATE_UI(win, win.IDM_EDIT_FORMAT_QUOTE, win.OnUpdateUI)
	wx.EVT_UPDATE_UI(win, win.IDM_EDIT_FORMAT_UNQUOTE, win.OnUpdateUI)
Mixin.setPlugin('mainframe', 'init', init)

def OnUpdateUI(win, event):
	eid = event.GetId()
	if eid == win.IDM_EDIT_FORMAT_QUOTE:
		event.Enable(win.document.GetSelectedText and len(win.document.GetSelectedText()) > 0)
	elif eid == win.IDM_EDIT_FORMAT_UNQUOTE:
		event.Enable(win.document.GetSelectedText and len(win.document.GetSelectedText()) > 0)
Mixin.setPlugin('mainframe', 'on_update_ui', OnUpdateUI)

def init(win):
	wx.EVT_UPDATE_UI(win, win.IDPM_FORMAT_QUOTE, win.OnUpdateUI)
	wx.EVT_UPDATE_UI(win, win.IDPM_FORMAT_UNQUOTE, win.OnUpdateUI)
Mixin.setPlugin('editor', 'init', init)

def OnUpdateUI(win, event):
	eid = event.GetId()
	if eid == win.IDPM_FORMAT_QUOTE:
		event.Enable(len(win.GetSelectedText()) > 0)
	elif eid == win.IDPM_FORMAT_UNQUOTE:
		event.Enable(len(win.GetSelectedText()) > 0)
Mixin.setPlugin('editor', 'on_update_ui', OnUpdateUI)

