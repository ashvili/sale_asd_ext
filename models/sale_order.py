# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import random
import string

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    responsible_give_goods_id = fields.Many2one(
        comodel_name='res.users',
        string="Responsible for issuing goods",
        readonly=False,
        required=True,
        )

    test = fields.Char(
        string='Info',
        default=lambda self: ''.join([random.choice(string.ascii_letters) for n in range(10)]),
        store=True,
        readonly=False,
        compute='_compute_test',
        inverse='_inverse_test',
        )

    @api.depends('order_line', 'date_order')
    def _compute_test(self):
        for order in self:
            if order.amount_total != 0:
                order.test = f'Total: {order.amount_total}, Date: {order.date_order}'
            elif order.state == 'draft' and order.test == '':
                order.test = ''.join([random.choice(string.ascii_letters) for n in range(10)])

    def _inverse_test(self):
        pass

    @api.constrains('test')
    def _check_text(self):
        for order in self:
            if order.state == 'draft' and isinstance(order.test, str) and len(order.test.strip()) > 50:
                raise ValidationError('The length of the field "Info" have to be less when 50 simbols.')