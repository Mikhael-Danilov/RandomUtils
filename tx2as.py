#!/usr/bin/env python
import os
import shutil
import string
import pprint
from xml.etree import ElementTree

dstDir = "/media/mike/BigData/Nyrds/Remixed Pixel Dungeon/PixelDungeon/src/main/res/"

xml_ext = '.xml'
translations_dir = 'translations/'

locale_remap = {'de_DE':'de', 'es_ES':'es', 'fr_FR':'fr', 'pl_PL':'pl', 'nl_NL':'nl', 'ro_RO':'ro', 'ru_RU':'ru','uk_UA':'uk','pt_BR':'pt-rBR','pt_PT':'pt-rPT','es_MX':'es-rMX',"ms_MY":"ms"}

used_locales = {'de','es','fr','it','ja','pl','pt-rBR','ru','tr','uk','zh','ko',"ms"}

counters = {}
totalCounter = {}

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
      
      counters[resource_name] = {}
      
      for _, _, files in os.walk(translations_dir+dir_name):
         for file_name in files:
            locale_code = file_name[:-4]
            
            if locale_code in locale_remap:
               locale_code = locale_remap[locale_code]
            
            if not locale_code in used_locales:
               continue
            
            if locale_code not in totalCounter:
               totalCounter[locale_code] = 0
               
            counters[resource_name][locale_code] = 0
            
            resource_dir = dstDir + "values-"+locale_code
            if not os.path.isdir(resource_dir):
               os.makedirs(resource_dir)
            
            
            currentFilePath = translations_dir+dir_name+"/"+file_name
            
            #print currentFilePath
            try:
               transifexData = ElementTree.parse(currentFilePath, parser = CommentedTreeBuilder() ).getroot()
               
               for entry in transifexData:
                  counters[resource_name][locale_code]+=1
                  totalCounter[locale_code]+=1
                  if entry.text is not None and "\\\\" in entry.text:
                     entry.text=entry.text.replace("\\\\","\\")
               
               ElementTree.ElementTree(transifexData).write(resource_dir+"/"+resource_name,"utf-8",xml_declaration=True)
               
            except ElementTree.ParseError:
               print "shit happens with " + currentFilePath
            
pprint.pprint(totalCounter)
