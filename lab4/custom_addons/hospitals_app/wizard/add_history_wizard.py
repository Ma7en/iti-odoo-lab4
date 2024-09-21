from odoo import models, fields

class AddHistory(models.TransientModel):
    _name = 'hsm.add.history'
    _description = 'Add History'

    patient_id = fields.Many2one('hms.patient')
    history = fields.Html()

    def action_add_history(self):
        # self.ensure_one()
        # self.patient_id.history = "a"

        if self.history:
            self.patient_id.write({
                'history': (self.patient_id.history or '') + self.history
            })
        return {'type': 'ir.actions.act_window_close'}






