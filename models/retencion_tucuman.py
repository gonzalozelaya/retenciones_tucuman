from odoo import fields,models,api

class AccountJournal(models.Model):
    _inherit = 'account.journal'
       
    """
    Calculo de retención
    # withholdable_base_amount
    # payment: account.payment.group object
    # partner: res.partner object (commercial partner of payment group)
    # withholding_tax: account.tax.withholding object

    if partner.x_studio_retencin_tucuman:
        result = withholdable_base_amount * payment.tucuman_alicuota/100 * payment.tucuman_cf * payment.tucuman_c_m
    else:
        result = 0
    """
    es_retencion_tucuman = fields.Boolean('Retención Tucumán?',default=False)
    c_m = fields.Float('CM')


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    tucuman_alicuota = fields.Float('Alicuota')
    tucuman_cf = fields.Float('Coeficiente', digits=(16, 4),default = 0.0447)
    tucuman_c_m = fields.Float('C.M.',default=0.5)
    es_retencion_tucuman = fields.Boolean('Renteción Tucumán',related ='partner_id.x_studio_retencion_tucuman')

class PaymentGroup(models.Model):
    _inherit = 'account.payment.multiplemethods'
    tucuman_alicuota = fields.Float('Alicuota')
    tucuman_cf = fields.Float('Coeficiente', digits=(16, 4),default = 0.0447)
    tucuman_c_m = fields.Float('C.M.',default=0.5)
    es_retencion_tucuman = fields.Boolean('Renteción Tucumán',related ='partner_id.x_studio_retencion_tucuman')
 