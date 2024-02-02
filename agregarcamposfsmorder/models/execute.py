from odoo import models, fields, api


class CustomServiceOrderTwo(models.Model):
    _inherit = 'fsm.order'

    tecexecution = fields.Selection([
        ('1', 'Se puede ejecutar'),
        ('2', 'No se puede ejecutar')],
        string="¿El servicio se puede realizar inmediatamente?")

    resolution = fields.Text(string="Indique la solucion realizada")

    datos_personales = fields.Boolean(string="Datos Personales")

    firma = fields.Binary(string="Firma de analista")
    q_firma = fields.Char(string="Nombre del analista")
    cc_q_firma = fields.Char(string="CC del analista")

    firma2 = fields.Binary(string="Firma Tecnico")
    q_firma2 = fields.Char(string="Nombre del Tecnico")
    cc_q_firma2 = fields.Char(string="CC del Tecnico")

    def aceptacion_datos(self):
        # Aquí puedes realizar las operaciones necesarias al aceptar los datos
        # Por ejemplo, puedes marcar un campo relacionado con la aceptación de datos
        self.datos_personales = True

    def _get_report_values(self, docids, data=None):
        docs = self.env['fsm.order'].browse(docids)
        return {'docs': docs}

    def action_report_custom_order(self):
        return self.env.ref('agregarcamposfsmorder.report_custom_order').report_action(self)