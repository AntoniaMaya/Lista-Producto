from odoo import models, fields, api

class ReportProductList(models.AbstractModel):
    _name = 'report.product_list_report.report_product_list_template'
    _description = 'Reporte de Lista de Productos'

    @api.model
    def _get_report_values(self, docids, data=None):
        wizard = self.env['product.list.wizard'].browse(docids)
        product_prices = []
        for product in wizard.product_ids:
            if wizard.price_list_id:
                # Obtener el precio del producto según la lista de precios
                price = wizard.price_list_id.get_product_price(product, 1.0, self.env.user.partner_id)
            else:
                # Si no hay lista de precios seleccionada, usar el precio de lista predeterminado
                price = product.list_price
            product_prices.append({
                'product': product,
                'price': price,
            })
        return {
            'doc_ids': docids,
            'doc_model': 'product.list.wizard',
            'doc': wizard,  # Pasar el wizard como 'doc'
            'company': self.env.company,  # Pasar la empresa
            'product_prices': product_prices,  # Lista de productos con precios
        }
