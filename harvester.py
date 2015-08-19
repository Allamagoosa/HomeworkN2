#!/usr/bin/python
# -*- coding: utf-8 -*-
""" This module collect docstrings from root folder """
import sys
import importlib
import os
from jinja2 import Template
import imp

command = '0'
if len(sys.argv) > 1: command = sys.argv[1]

class Harvester(object):
    """ Common base class for collect docstrings """
    def __init__(self, dir = "/home/pm/work/x/"):
        self.dir_path = dir
        if command != '0': self.dir_path = command
        print ("dir_path=" + self.dir_path)
       
    def list_files(self):
        list_of_files = os.listdir(self.dir_path)
        return list_of_files

    def harvest(self):
        """ Result Function """
        # jinja-----------------------------------
        tmpl = Template(u'''\
<html>
<head><title>{{ variable|escape }}</title></head>
<body>
{{ item }}
</body>
</html>''')
        # ----------------------------------------                                                                             
        for file_item in self.list_files():
            fullname = os.path.splitext(file_item)
            filename = fullname[0]
            if fullname[1] ==".py":                
                string_write = self.trim(filename)
                file_write = filename
                # jinja
                string_write = tmpl.render(variable= str(filename), item=string_write)
                self.write(file_write+".html", string_write)
                 
                 
    def write(self, fw, sw):
        """ Write to script working directory """
        self.file_w = fw
        self.string_w = sw
        f = open(self.file_w, "w")
        # Working print for user
        print ("file to write: "+os.getcwd()+'/'+f.name)
        f.write(self.string_w);
        f.close()
        
    def trim(self, tfile):
        """ Take docstring from file and format to more clear view. Result is a string """ 
        
        # import from chosen directory, see Harvester.__init__(dir_path)
        # ***todo may be need seperataly function
        module = imp.load_source(tfile, self.dir_path+tfile+".py")
        docstring = module.__doc__
        
        # Using code from example :) https://www.python.org/dev/peps/pep-0257/ 
        if not docstring:
            return ''
        # Convert tabs to spaces (following the normal Python rules)
        # and split into a list of lines:
        lines = docstring.expandtabs().splitlines()
        # Determine minimum indentation (first line doesn't count):
        indent = sys.maxint
        for line in lines[1:]:
            stripped = line.lstrip()
            if stripped:
                indent = min(indent, len(line) - len(stripped))
        # Remove indentation (first line is special):
        trimmed = [lines[0].strip()]
        if indent < sys.maxint:
            for line in lines[1:]:
                trimmed.append(line[indent:].rstrip())
        # Strip off trailing and leading blank lines:
        while trimmed and not trimmed[-1]:
            trimmed.pop()
        while trimmed and not trimmed[0]:
            trimmed.pop(0)
        # Return a single string:
        return '\n'.join(trimmed)

#h1 = Harvester()
