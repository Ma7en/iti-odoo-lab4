from pkg_resources import require

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Customer(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient')


    @api.constrains('vat')
    def _check_tax(self):
        for rec in self:
            if not rec.vat:
                raise ValidationError('Tax id is required')

    @api.constrains('email')
    def _check_email(self):
        for rec in self:
            if rec.email:
                patient_mails = self.env['hms.patient'].search([]).mapped('email')
                if rec.email in patient_mails:
                    raise ValidationError('this email already exist in patients')


    def unlink(self):
        for record in self:
            if record.related_patient_id:
                raise ValidationError('can\'t delete this record')