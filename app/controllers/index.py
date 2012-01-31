# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, db, urlfor, redirect

def index():
    visitcount = local.session.get("visitcount", 0) + 1
    local.session["visitcount"] = visitcount
    template_response("/page/index.mako", visitcount=visitcount)

def testpage0():
    template_response("/error/notyet.mako")

def testpage1():
    template_response("/error/notyet.mako")

def testpage2():
    template_response("/error/notyet.mako")

def testpage3():
    template_response("/error/notyet.mako")
