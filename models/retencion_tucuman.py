from odoo import fields,models,api

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    es_retencion_tucuman = fields.Boolean('Retención Tucumán?',default=False)
    c_m = fields.Float('CM')


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    tucuman_alicuota = fields.Float('Alicuota')
    tucuman_cf = fields.Float('Coeficiente', digits=(16, 4),default = 0.0447)
    tucuman_c_m = fields.Float('C.M.',default=0.5)
    es_retencion_tucuman = fields.Boolean('Renteción Tucumán',related ='partner_id.x_studio_retencin_tucuman')

class PaymentGroup(models.Model):
    _inherit = 'account.payment.multiplemethods'
    tucuman_alicuota = fields.Float('Alicuota')
    tucuman_cf = fields.Float('Coeficiente', digits=(16, 4),default = 0.0447)
    tucuman_c_m = fields.Float('C.M.',default=0.5)
    es_retencion_tucuman = fields.Boolean('Renteción Tucumán',related ='partner_id.x_studio_retencin_tucuman')