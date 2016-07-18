import codecs
from xml.dom import minidom
import os
import net.trans_tool as transTool

class XmlData:
	'解析数据类'
	def __init__(self, path):
		self.path = path
		self.domTree = minidom.parse(self.path)
		self.collection = self.domTree.documentElement
		self.m_rowList = self.collection.getElementsByTagName("row")

	def saveToDataList(self):
		self.m_dataList = []
		for row in self.m_rowList:
			rowKeyItem = row.getElementsByTagName('value')[0]
			rowKey = rowKeyItem.childNodes[0].data
			rowValueItem = row.getElementsByTagName('value')[1]
			rowValue = rowValueItem.childNodes[0].data

			tempList = []
			tempList.append(rowKey)
			tempList.append(rowValue)
			self.m_dataList.append(tempList)
		return self.m_dataList

	# def transToDataList(self):
	# 	countLimit = 50
	# 	curIndex = 0
	# 	transStr = ""
	# 	transTotalStr = ""
	# 	for index in range(len(self.m_dataList)):
	# 		curIndex = curIndex + 1
	# 		transStr = transStr + "\n" + self.m_dataList[index][1]
	# 		if curIndex == countLimit:
	# 			curIndex = 0
	# 			temStr = transTool.transToZh(transStr)
	# 			transTotalStr = transTotalStr + temStr
	# 			transStr = ""
	# 	temStr = transTool.transToZh(transStr)
	# 	transTotalStr = transTotalStr + temStr

	def transToDataList(self, lang_index):
		for index in range(len(self.m_dataList)):
			transStr = self.m_dataList[index][1]
			temStr = self.transToByIndex(transStr, lang_index)
			self.m_dataList[index].append(temStr)


	def transToByIndex(self, transStr, index):
		temStr = ""
		if index == 1:
			temStr = transTool.transToZh(transStr)
		elif index == 2:
			temStr = transTool.transToEn(transStr)
		elif index == 3:
			temStr = transTool.transToJp(transStr)
		return temStr
