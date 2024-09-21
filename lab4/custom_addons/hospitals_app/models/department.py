from odoo import models, fields

class Department(models.Model):
    _name = 'hms.department'
    _description = 'Department'

    name = fields.Char(required=True)
    capacity = fields.Integer(required=True)
    is_opened = fields.Boolean(default=True)
    patient_ids = fields.One2many('hms.patient', 'department_id')
    doctor_ids = fields.Many2many('hms.doctor')

    _sql_constraints = [
        ('unique_department_name',
         'unique(name)',
         'Department name must be unique!')
    ]
