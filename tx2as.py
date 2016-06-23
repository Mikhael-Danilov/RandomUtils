#!/usr/bin/env python
import os
import shutil
import string

xml_ext = '.xml'
translations_dir = 'translations/'

locale_remap = {'de_DE':'de', 'es_ES':'es', 'fr_FR':'fr', 'pl_PL':'pl', 'nl_NL':'nl', 'ro_RO':'ro', 'ru_RU':'ru','uk_UA':'uk'}

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
            shutil.copyfile(translations_dir+dir_name+"/"+file_name,resource_dir+"/"+resource_name)
            