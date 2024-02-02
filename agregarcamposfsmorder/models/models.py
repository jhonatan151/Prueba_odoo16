from odoo import models, fields


class CustomServiceOrder(models.Model):
    _inherit = 'fsm.order'

    material_requests = fields.One2many('custom.service.order.material', 'order_id', string='Material Requests')


class CustomServiceOrderMaterial(models.Model):
    _name = 'custom.service.order.material'
    _description = 'Custom Service Order Material'

    order_id = fields.Many2one('fsm.order', string='Order')
    product_id = fields.Many2one('product.product', string='Producto', domain="[('type','=','product')]")
    quantity = fields.Float(string='Cantidad')
    uom_id = fields.Many2one('uom.uom', string='Unidad de medida')


class CustomServiceOrderTipoSis(models.Model):
    _inherit = 'fsm.order'

    tipo_sistema = fields.Selection([
        ('alarma', 'ALARMA'),
        ('video', 'VIDEO'),
        ('control_acceso', 'CONTROL DE ACCSESO'),
        ('eps', 'EPS'),
        ('els', 'ELS'),
        ('preventivo', 'PREVENTIVO'),
        ('automatizacion', 'AUTOMATIZACION'),
        ('instalacion_alarma_y_video', 'INSTALACION ALARMA Y VIDEO'),
        ('desmonte_alarma_y_video', 'DESMONTE ALARMA Y VIDEO'),
    ], string='Tipo de Sistema')


class CustomServiceOrderTipoUni(models.Model):
    _inherit = 'fsm.order'

    tipo_unidad = fields.Selection([
        ('n/a', 'N/A'),
        ('atm', 'ATM'),
        ('edf', 'EDF'),
        ('ofc', 'OFC'),
    ], string='Tipo de Unidad')
