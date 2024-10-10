{
    'name': 'Generar Lista de Productos',
    'version': '1.0',
    'summary': 'Permite generar y imprimir una lista de productos con precios seleccionables',
    'description': """
    """,
    'author': '',
    'depends': ['base', 'stock'],
    'data': [
        'security/ir.model.access.csv', 
        'views/product_list_wizard_views.xml',
        'reports/report_product_list.xml',
        #'reports/product_list_report_template.xml',    
        
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
