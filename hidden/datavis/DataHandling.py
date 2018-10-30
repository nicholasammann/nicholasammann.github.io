import os
import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from xml.dom import minidom
from lxml import etree

def formatXML(elem):
  rough_string = ElementTree.tostring(elem, 'utf-8')
  reparsed = minidom.parseString(rough_string)
  return reparsed.toprettyxml(indent="  ")

class DataItem:
  def __init_(self):
    self.key = ""
    self.values = []

class DataSet:
  def __init__(self):
    self.title = "DataSetName"
    self.items = {}

# returns a data set
def LoadCSV(path):
  if not os.path.exists(path):
    return False

  with open(path, 'r') as csvfile:
    readValues = csv.reader(csvfile)
    data = DataSet()
    for row in readValues:
      item = DataItem()
      item.key = row[0]
      row.remove(row[0])
      item.values = row
      data.items[item.key] = item
    return data

def SaveAsCSV(dataSet, outDir):
  return True

# returns a data set
def LoadXML(path):
  if not os.path.exists(path):
    return False

def SaveAsXML(dataSet, outDir):
  root = etree.Element(dataSet.title)

  for item in dataSet.items.items():
    subElem = etree.SubElement(root, item[1].key)
    for val in item[1].values:
      valueElem = etree.SubElement(subElem, 'value')
      valueElem.set('num', val)

  xml_obj = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8')
  with open(dataSet.title + ".xml", "wb") as writer:
    writer.write(xml_obj)

class DataCenter:
  def StoreData(self, key, dataSet):
    self.dataSets[key] = dataSet

  def GetData(self, key):
    return self.dataSets[key]

  def __init__(self):
    self.dataSets = {}
