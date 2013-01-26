import xlwt

class excel():
    def __init__(self, name):
        self.name = name
        self.sheetInfo = {}
        self.sheetRow = {}
        
        pass
    
    @staticmethod
    def open(name):
        obj = excel(name)
        obj.wbk = xlwt.Workbook()
        return obj
    

    def __addSheet__(self, name):
        sheet = self.wbk.add_sheet(name)
        self.sheetInfo[name] = sheet
        self.sheetRow[name] = 0
        return sheet
    
    def __getSheet__(self, name):
        if not self.sheetInfo.has_key(name):
            sheet = self.__addSheet__(name)
        else:
            sheet = self.sheetInfo[name]
        return sheet
    
    @staticmethod
    def write(obj, sheet_name, datas, styles = None):
        
        sheet = obj.__getSheet__(sheet_name)
        row = obj.sheetRow[sheet_name]
        obj.sheetRow[sheet_name] = row + 1
        
        
        if styles != None:
            if (isinstance(styles, list)):
                for col in range(len(datas)):    
                    sheet.write(row, col, datas[col], styles[col])
            else:
                for col in range(len(datas)):   
                    sheet.write(row, col, datas[col], styles)
        else:
            sheet.write(row, col, datas[col])
        
    
    @staticmethod   
    def setColWidth(obj, sheet_name, widths):
        sheet = obj.__getSheet__(sheet_name)
        
        for col in range(len(widths)):
            sheet.col(col).width = widths[col] * 450
    
    @staticmethod
    def createSytle(fore_color, bold = False):
        styleString = 'colour_index ' + fore_color
        
        if (bold == True):
            styleString = styleString + ',' + 'bold on'
        
        style = xlwt.easyxf('font: ' + styleString);
        return style
    
    @staticmethod
    def close(obj):
        obj.wbk.save(obj.name)
        pass
        
        
    
    
if __name__ == "__main__":
    efile = excel.open('file.xls')
    sytleR = excel.createSytle('red', True)
    sytleY = excel.createSytle('yellow', True)
    for i in range(10000):
        excel.write(efile, 'sheet', ['NAME', 'DATE'], [sytleR, sytleY])
    excel.setColWidth(efile, 'sheet', [4, 4, 4, 4])
    
    excel.close(efile)
    
    print 'success'

    
