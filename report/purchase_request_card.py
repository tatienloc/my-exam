from odoo import models

class PurchaseCard(models.AbstractModel):
    _name = "purchase_request_card"
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self , workbook , data , lines):
        format1 = workbook.add_format({'font_size' : 14 , 'align' : 'vcenter' , 'bold' : True})
        format2 = workbook.add_format({'font_size' : 10 , 'algin' : 'vcenter'})
        sheet = workbook.add_worksheet('Purchase request card')
        sheet.set_column(3,3,50)
        sheet.set_column(2,2,30)
        sheet.write(2,2,'Name',format1)
        sheet.write(2,3,lines.department_id,format2)
        sheet.write(2, 2, 'Age', format1)
        sheet.write(2, 3, lines.request_id, format2)