
{
    'name': 'File Manager',
    'version': '1.0',
    'summary': 'Manage files and their upload dates',
    'description': """
        This module allows users to manage files and their upload dates.
    """,
    'author': 'Liubov Rudn',
    'website': 'www.filesystem.com',
    'category': 'Uncategorized',
    "license": "AGPL-3",
    'depends': ['website'],
    'data': [
    'views/file_manager_view.xml',
    'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}