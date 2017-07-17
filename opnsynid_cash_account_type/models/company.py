# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class Company(models.Model):
    _inherit = "res.company"

    cash_account_type_ids = fields.Many2many(
        string='Cash Account Type',
        comodel_name='account.account.type',
        rel='rel_company_2_acc_type',
        id1='company_id',
        id2='account_type_id',
    )
