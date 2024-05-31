from odoo import models, fields, api

class LibreriaLibros(models.Model):
    _name = 'libreria.libros'
    _description = 'Libro'

    # Campos
    titulo = fields.Char('Título', size=30, required=True, help='Nombre del libro')
    imagen = fields.Image('Imagen del libro')
    prestado = fields.Boolean('Está prestado')
    autor_id = fields.Many2one('libreria.autores', string="Autor")  # Relación Many2one con el modelo de autores
    clasificacion = fields.Boolean('Clasificación 18+', help='Si es mayor de 18 años')
    fecha_lanzamiento = fields.Date('Fecha de lanzamiento')
    ventas = fields.Integer('Ventas', default=0)
    best_seller = fields.Boolean('Best Seller', compute='_compute_best_seller', store=True)

    # Campos relacionados
    categoria_id = fields.Many2one('libreria.categorias', string="Categoría")
    #editorial_id = fields.Many2one('libreria.editorial', string="Editorial")

    @api.depends('ventas')
    def _compute_best_seller(self):
        for record in self:
            record.best_seller = record.ventas > 10000

class LibreriaCategorias(models.Model):
    _name = 'libreria.categorias'
    _description = 'Categoría de los Libros'

    name = fields.Char('Nombre', required=True)
    descripcion = fields.Text('Descripción')
    libros_ids = fields.One2many('libreria.libros', 'categoria_id', string="Libros")
    
class LibreriaAutores(models.Model):
    _name = 'libreria.autores'
    _description = 'Autor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Nombre', required=True, tracking=True)
    biografia = fields.Text('Biografía', tracking=True)
    fecha_nacimiento = fields.Date('Fecha de Nacimiento', tracking=True)
    nacionalidad = fields.Char('Nacionalidad', tracking=True)
    libros_ids = fields.One2many('libreria.libros', 'autor_id', string="Libros Publicados", tracking=True)

#class LibreriaEditorial(models.Model):
    #_inherit = 'res.partner'

    #is_editorial = fields.Boolean('Es una editorial', default=False)
    #libros_ids = fields.One2many('libreria.libros', 'editorial_id', string="Libros publicados")