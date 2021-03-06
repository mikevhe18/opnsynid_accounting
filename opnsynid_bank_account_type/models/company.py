# -*- encoding: utf-8 -*-
##############################################################################
#    Author : Andhitia Rama, Michael Viriyananda, Nurazmi
#    Copyright (C) 2015 OpenSynergy Indonesia
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models


class Company(models.Model):
    """Company"""
    _inherit = "res.company"

    bank_account_type_ids = fields.Many2many(
        string='Bank Account Type',
        comodel_name='account.account.type',
        rel='rel_company_2_bank_acc_type',
        id1='company_id',
        id2='bank_acc_type_id',
    )
