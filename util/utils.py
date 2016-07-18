import xlrd

#--Excel操作相关
class TableInfo:
    def __init__(self):
        self.table_name = ""
        self.table_name_cn = ""
        self.col_names = []
        self.row_datas = []
        self.row_lists = []
        self.table_info = ""

# 读取excel文件
def read_excel(file_name):
    sheet_list = [] #存放excel中的表名
    file_data = xlrd.open_workbook(file_name)
    for sheet_name in file_data.sheet_names():
        table_info = file_data.sheet_by_name(sheet_name) # 通过名称获取
        get_sheet(table_info, sheet_name, file_name, sheet_list)
    return sheet_list

def get_sheet(table_info, sheet_name, file_name, sheet_list):
    #记录符合规定的表的数据
    item = []
    item.append(table_info)
    item.append(sheet_name)
    item.append(file_name)
    sheet_list.append(item)

#读取表数据
def read_sheet(item):
    table_info = item[0]
    sheet_name = item[1]
    file_name = item[2]

    if table_info.nrows > 0 and table_info.ncols > 0:
        table_info_obj = TableInfo()
        table_info_obj.table_name = sheet_name

        for col in range(0, table_info.ncols):
            col_name = str(table_info.cell(0,col).value).strip().lower()
            table_info_obj.col_names.append(col_name)

        for row in range(0, table_info.nrows):
            row_data = {}
            for col in range(0, table_info.ncols):
                if str(table_info.cell(row,col).value).strip() != '':
                    col_name = str(table_info.cell(0,col).value).strip().lower()
                    value = table_info.cell(row,col).value
                    if ( type(value) == float ):
                        if ( value == int(value) ):
                            value = int(value)
                    row_data[col_name] = value
            table_info_obj.row_datas.append(row_data)
            table_info_obj.table_info = table_info

        for row in range(0, table_info.nrows):
            row_list = []
            for col in range(0, table_info.ncols):
                if str(table_info.cell(row,col).value).strip() != '':
                    col_name = str(table_info.cell(0,col).value).strip().lower()
                    value = table_info.cell(row,col).value
                    if ( type(value) == float ):
                        if ( value == int(value) ):
                            value = int(value)
                    row_list.append(value)
            table_info_obj.row_lists.append(row_list)
    return table_info_obj



#-----------------------------------------------------------------------------------------------------------------------
import shutil
import xlrd
import os

#两目录拷贝
def copyFilesDir(sourceDir, targetDir):
    for f in os.listdir(sourceDir):
        sourceF = os.path.join(sourceDir, f)
        targetF = os.path.join(targetDir, f)

        if os.path.isfile(sourceF):
            #创建目录
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            shutil.copy(sourceF, targetF)
        if os.path.isdir(sourceF):
            copyFiles(sourceF, targetF)

#任意拷贝
def copyFiles(sourceDir, targetDir):
    if os.path.isfile(sourceDir) == False and os.path.isfile(targetDir) == False:
        copyFilesDir(sourceDir, targetDir)
    elif os.path.isfile(sourceDir) == True and os.path.isfile(targetDir) == True:
        shutil.copy(sourceDir, targetDir)
    elif os.path.isfile(sourceDir) == True and os.path.isfile(targetDir) == False:
        shutil.copy(sourceDir, targetDir)
    else:
        print("错误!源路径是目录,目标路径是文件!")