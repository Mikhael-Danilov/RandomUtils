#!/usr/bin/env python
import os
import shutil
import string
import pprint
from xml.etree import ElementTree

import json

dstDir = "/media/mike/BigData/Nyrds/pixel-dungeon-remix/RemixedDungeon/src/main/res/"

xml_ext = '.xml'
translations_dir = 'translations/'

locale_remap = {'de_DE':'de', 'es_ES':'es', 'fr_FR':'fr', 'pl_PL':'pl', 'nl_NL':'nl', 'ro_RO':'ro', 'ru_RU':'ru','uk_UA':'uk','pt_BR':'pt-rBR','pt_PT':'pt-rPT','es_MX':'es-rMX',"ms_MY":"ms"}

used_locales = {'de','es','fr','it','pl','pt-rBR','ru','tr','uk','zh','ko',"ms"}

counters = {}
totalCounter = {}

dir_name = "remixed-dungeon.strings-all-xml--master"
resource_name = "strings_all.xml"

print ("Processing:", dir_name,resource_name)

counters[resource_name] = {}

def unescape(str):
    return str.replace("\\\\","\\").replace("\\\\","\\")

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

        print ("file:", currentFilePath)
        try:
           transifexData = ElementTree.parse(currentFilePath).getroot()

           jsonData = open("strings_"+locale_code+".json","w", encoding='utf8')

           for entry in transifexData:
            counters[resource_name][locale_code]+=1
            totalCounter[locale_code]+=1

            if entry.tag == "string":
                jsonData.write(unescape(json.dumps([entry.get("name"), entry.text],ensure_ascii=False)))
                jsonData.write("\n")

            if entry.tag == "string-array":
                arrayDesc = [entry.get("name")]
                for arrayItem in entry:
                    arrayDesc.append(arrayItem.text)

                jsonData.write(unescape(json.dumps(arrayDesc, ensure_ascii = False)))
                jsonData.write("\n")

            if entry.text is not None and "\\\\" in entry.text:
                entry.text=entry.text.replace("\\\\","\\")

           ElementTree.ElementTree(transifexData).write(resource_dir+"/"+resource_name,"utf-8",xml_declaration=True)
           jsonData.close()
        except ElementTree.ParseError as error:
           print ("shit happens with " + currentFilePath)
           print (error)
            
pprint.pprint(totalCounter)
