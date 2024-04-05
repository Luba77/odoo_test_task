import base64
import os
from odoo import http, fields
from odoo.http import request


class FileManagerController(http.Controller):

    @http.route('/file_manager_view', auth='public', csrf=False, website=True)
    def file_manager_view(self, **kwargs):
        db_files = request.env['ir.attachment'].sudo().search([])
        current_dir = os.path.dirname(os.path.abspath(__file__))
        disk_files = os.path.join(current_dir, 'files')
        return http.request.render('dev.file_manager_view_template', {
            'db_files': db_files,
            'disk_files': disk_files,
        })

    @http.route('/upload_file', type='http', auth="public", csrf=False, website=True)
    def upload_file(self, **post):
        try:
            file_obj = post.get('file')
            storage_option = post.get('storage_option')  # 'db' or 'disk'

            if file_obj and storage_option:
                file_name = file_obj.filename
                upload_date = fields.Datetime.now()

                if storage_option == 'db':
                    # Save file to database
                    file_manager_obj = request.env['ir.attachment']
                    file_manager = file_manager_obj.create({
                        'name': file_name,
                        'datas': base64.b64encode(file_obj.read()),
                        'res_model': 'ir.attachment',
                        'res_id': 0,
                        'mimetype': file_obj.content_type,
                        'create_date': upload_date,
                        'write_date': upload_date,
                        'public': True,
                        'status': 'done'
                    })
                elif storage_option == 'disk':
                    current_dir = os.path.dirname(os.path.abspath(__file__))
                    upload_folder = os.path.join(current_dir, 'files')
                    file_path = os.path.join(upload_folder, file_name)
                    with open(file_path, 'wb') as f:
                        f.write(file_obj.read())

                    file_manager_obj = request.env['file.manager']
                    file_manager = file_manager_obj.create({
                        'file_name': file_name,
                        'upload_file_path': file_path,
                        'upload_date': upload_date,
                        'status': 'done'
                    })
                else:
                    return "Invalid storage option!"

                return "File uploaded successfully!"
            else:
                return "File or storage option missing!"
        except Exception as e:
            return str(e)

    @http.route('/file_manager_view', auth='public', csrf=False, website=True)
    def file_manager_view(self, **kwargs):

        db_files = request.env['ir.attachment'].sudo().search([])
        current_dir = os.path.dirname(os.path.abspath(__file__))
        disk_files = os.path.join(current_dir, 'files')
        return http.request.render('dev.file_manager_view_template', {
            'db_files': db_files,
            'disk_files': os.listdir(disk_files),
        })

    @http.route('/remove_file/<int:file_manager_id>', type='http', auth='public', website=True)
    def remove_file(self, file_manager_id, **kwargs):
        try:
            file_manager = http.request.env['ir.attachment'].sudo().browse(file_manager_id)
            if file_manager:
                file_manager.unlink()
                return "File removed successfully!"
            else:
                return "File not found!"
        except Exception as e:
            return str(e)

