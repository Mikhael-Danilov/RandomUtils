#!/usr/bin/env python
import sys
from xml.etree import ElementTree

def run(files):
    first = None
    for filename in files:
        data = ElementTree.parse(filename).getroot()
        if first is None:
            first = data
        else:
            first.extend(data)
            
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
      
    if first is not None:
        print ElementTree.tostring(first)
        ElementTree.ElementTree(first).write("out.xml","utf-8")

if __name__ == "__main__":
    run(sys.argv[1:])