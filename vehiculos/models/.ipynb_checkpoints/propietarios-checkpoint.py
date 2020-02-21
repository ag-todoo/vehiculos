# -*- coding: utf-8 -*-

from odoo import models, fields

class propietarios(models.Model):
     _name = 'propietarios.usuarios'
     _description = 'propietarios de los vehiculos'

     nombrepropietario = fields.Char()
     cedula = fields.Integer()
     vehiculo = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
