# -*- coding: utf-8 -*-
from xml.dom.minidom import parse
import codecs
from xml.dom import minidom
import os

# ==由于minidom默认的writexml()函数在读取一个xml文件后，修改后重新写入如果加了newl='\n',会将原有的xml中写入多余的行
#　 ==因此使用下面这个函数来代替
def fixed_writexml(self, writer, indent="", addindent="", newl=""):
	# indent = current indentation
	# addindent = indentation to add to higher levels
	# newl = newline string
	writer.write(indent+"<" + self.tagName)

	attrs = self._get_attributes()
	a_names = sorted(attrs.keys())

	for a_name in a_names:
		writer.write(" %s=\"" % a_name)
		minidom._write_data(writer, attrs[a_name].value)
		writer.write("\"")
	if self.childNodes:
		if len(self.childNodes) == 1 and self.childNodes[0].nodeType == minidom.Node.TEXT_NODE:
			writer.write(">")
			self.childNodes[0].writexml(writer, "", "", "")
			writer.write("</%s>%s" % (self.tagName, newl))
			return
		writer.write(">%s"%(newl))
		for node in self.childNodes:
			if node.nodeType is not minidom.Node.TEXT_NODE:
				node.writexml(writer,indent+addindent,addindent,newl)
		writer.write("%s</%s>%s" % (indent,self.tagName,newl))
	else:
		writer.write("/>%s"%(newl))

minidom.Element.writexml = fixed_writexml

class XmlData:
	'解析数据类'
	def __init__(self, path):
		self.path = path
		self.DOMTree = minidom.parse(self.path)
		self.collection = self.DOMTree.documentElement

	def insert_data(self, key, value):
		tool_item = self.DOMTree.createElement("row")
		value0 = self.DOMTree.createElement("value")
		value0.setAttribute('column','0')
		value0_str = self.DOMTree.createTextNode(str(key))
		value0.appendChild(value0_str)
		value1 = self.DOMTree.createElement("value")
		value1.setAttribute('column','1')
		value1_str = self.DOMTree.createTextNode(value)
		value1.appendChild(value1_str)
		tool_item.appendChild(value0)
		tool_item.appendChild(value1)
		rows = self.collection.getElementsByTagName("rows")[0]
		rows.appendChild(tool_item)

	#存储数据
	def sava_data(self):
		f= codecs.open(self.path, 'w', 'utf-8')
		self.DOMTree.writexml(f,addindent="	",newl="\n",encoding = "utf-8")
		f.close()
		print("回刷完成")




