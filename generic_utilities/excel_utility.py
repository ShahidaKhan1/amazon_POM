import xlrd

path = r'/Users/shahidakhan/Desktop/amazon_project/external_files/amazon_data.xlsx'

def excel_data(sheet):
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name(sheet)
    rows = worksheet.get_rows()
    header = next(rows)


    data = {}
    for ele in rows:
        data[ele[0].value] = ele[1].value

    return data