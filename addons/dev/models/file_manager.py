from odoo import api, fields, models

STATUS = [
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('error', 'Error')
    ]

class FileManager(models.Model):
    _name = "file.manager"
    _description = "File manager"

    file_name = fields.Char(string="File name")
    upload_file = fields.Binary(string="Upload file")
    upload_date = fields.Datetime(string="Upload Date")
    status = fields.Selection(STATUS,  string='Status', default='pending')

    def action_save_to_db(self):
        self.status = 'done'

    def action_save_to_disk(self):
        self.status = 'done'


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    status = fields.Selection(STATUS, string='Status', default='pending')
