# -*- coding: utf-8 -*-
from odoo import models, fields, api

class videoclub_pelis(models.Model):
    #atributos
    _name = 'videoclub.pelis'
    _description = 'Película'
    #campos
    titulo = fields.Char('Titulo', size=30, required=True, help='Nombre de la peli')
    director = fields.Char('Director', size=30, required=False, help='Director de la peli', default='')
    clasificacion = fields.Selection([('TP','Todos los Públicos'),('men12','Menores de12 años'),('may18','Mayores 18 años')], string='Clasificación', default='TP')
    presupuesto = fields.Integer()
    fechaestreno = fields.Date()

     # Se subvenciona el 30% de la película
    subvencionado = fields.Integer(compute='_valor_subvencion')
    invertido = fields.Integer(compute='_valor_inversion', store=False)  # queremos verlo de modo inmediato
    
    # Campo calculado para determinar si es millonario
    millonario = fields.Boolean(compute='_es_millonario', store=False, readonly=True)

    # Nuevo campo de imagen
    imagen = fields.Image("imagen")

    @api.depends('presupuesto')
    def _valor_subvencion(self):
        for record in self:
            record.subvencionado = record.presupuesto * 0.3
    
    @api.depends('presupuesto')
    def _valor_inversion(self):
        for record in self:
            record.invertido = record.presupuesto * 0.7
            
    @api.depends('presupuesto')
    def _es_millonario(self):
        for record in self:
            record.millonario = record.presupuesto > 1000000