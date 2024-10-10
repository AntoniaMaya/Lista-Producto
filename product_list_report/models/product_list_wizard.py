from odoo import models, fields, api

class ProductListWizard(models.TransientModel):
    _name = 'product.list.wizard'
    _description = 'Wizard para generar lista de productos'

    report_name = fields.Char(string='Nombre del Reporte', required=True)
    price_list_id = fields.Many2one('product.pricelist', string='Lista de Precios', required=True)
    product_ids = fields.Many2many('product.product', string='Productos')

    @api.model
    def default_get(self, fields):
        res = super(ProductListWizard, self).default_get(fields)
        default_price_list = self.env['product.pricelist'].search([], limit=1)
        if default_price_list:
            res.update({'price_list_id': default_price_list.id})
        return res

    def print_report(self):
        return self.env.ref('product_list_report.report_product_list').report_action(self)



