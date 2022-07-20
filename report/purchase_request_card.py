from odoo import models

class Purchaserequestxls(models.AbstractModel):
    _name = 'report.managerpurchase.report_purchase_card_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size' : 14 , 'align' : 'vcenter' , 'bold' : True})
        format2 = workbook.add_format({'font_size' : 10 , 'align' : 'vcenter' , })
        sheet = workbook.add_worksheet('Purchase card')
        sheet.write(2 , 2 , 'Name' , format1)
        sheet.write(2, 3 , lines.name ,format2)
        # sheet.write(3, 4, 'Department', format1)
        # sheet.write(3, 5, lines.department_id, format2)
        # sheet.write(3, 4, 'Requester', format1)
        # sheet.write(3, 5, lines.request_id, format2)
        # sheet.write(3, 4, 'Approver', format1)
        # sheet.write(3, 5, lines.approver_id, format2)
        sheet.write(3, 4, 'Date', format1)
        sheet.write(3, 5, lines.date, format2)
        # sheet.write(2, 2, 'Date approve', format1)
        # sheet.write(2, 3, lines.date_approve, format2)


