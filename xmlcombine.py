#!/usr/bin/env python
import sys
import os
from xml.etree import ElementTree

def combine(resource_name):
    first = ElementTree.parse("master/"+resource_name).getroot()
    
    if os.path.isfile("slave/"+resource_name):
       first.extend(ElementTree.parse("slave/"+resource_name).getroot())
       
       entries_already_seen = {}
       entries_to_remove = []
       for entry in first:
         entry_name = entry.attrib['name']
         if entry_name in entries_already_seen:
            entries_to_remove.append(entry)
         else:
            entries_already_seen[entry_name] = True
         
       for entry in entries_to_remove:
          first.remove(entry)
    
    ElementTree.ElementTree(first).write("combined/"+resource_name,"utf-8",xml_declaration=True)


for filename in os.listdir("master"):
    if filename.endswith(".xml"):
      combine(filename)
