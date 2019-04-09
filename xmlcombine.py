#!/usr/bin/env python
import sys
import os
import string
import pprint
from xml.etree import ElementTree

path = "/media/mike/BigData/Nyrds/pixel-dungeon-remix/RemixedDungeon/src/main/res"

combined = None

ignored_files = {"strings_not_translate.xml","strings_not_translate.xml","strings_api_signature.xml","strings_all.xml","strings-all-xml--mas.xml"}

for dir in os.listdir(path):
    langPath = path + "/" + dir
    combined = None
    for filename in os.listdir(langPath):
        if filename.endswith(".xml") and filename.startswith("str") and filename not in ignored_files:
            fullPath = langPath + "/" + filename
            print (fullPath)
            if combined is None:
                combined = ElementTree.parse(fullPath).getroot()
            else:
                combined.extend(ElementTree.parse(fullPath).getroot())
    if combined is not None:
        ElementTree.ElementTree(combined).write("strings_"+dir+".xml","utf-8",xml_declaration=True)
