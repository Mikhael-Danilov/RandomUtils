#!/usr/bin/env python
import os
import shutil
import string

from xml.etree import ElementTree

xml_ext = '.xml'
translations_dir = 'translations/'

locale_remap = {'de_DE':'de', 'es_ES':'es', 'fr_FR':'fr', 'pl_PL':'pl', 'nl_NL':'nl', 'ro_RO':'ro', 'ru_RU':'ru','uk_UA':'uk','pt_BR':'pt-rBR','pt_PT':'pt-rPT','es_MX':'es-rMX'}

class CommentedTreeBuilder ( ElementTree.XMLTreeBuilder ):
   def __init__ ( self, html = 0, target = None ):
      ElementTree.XMLTreeBuilder.__init__( self, html, target )
      self._parser.CommentHandler = self.handle_comment

   def handle_comment ( self, data ):
      self._target.start( ElementTree.Comment, {} )
      self._target.data( data )
      self._target.end( ElementTree.Comment )

for _, dirs, _ in os.walk(translations_dir):
    for dir_name in dirs:
      resource_name = string.split(dir_name,'.')[1][:-3]+xml_ext
      print "Processing:", resource_name
      for _, _, files in os.walk(translations_dir+dir_name):
         for file_name in files:
            locale_code = file_name[:-4]
            if locale_code in locale_remap:
               locale_code = locale_remap[locale_code]
            resource_dir = "android/values-"+locale_code
            if not os.path.isdir(resource_dir):
               os.makedirs(resource_dir)
            
            transifexData = ElementTree.parse(translations_dir+dir_name+"/"+file_name, parser = CommentedTreeBuilder() ).getroot()
            
            for entry in transifexData:
               if entry.text is not None and "\\\\" in entry.text:
                  entry.text=entry.text.replace("\\\\","\\")
            
            ElementTree.ElementTree(transifexData).write(resource_dir+"/"+resource_name,"utf-8",xml_declaration=True)