# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# License URL : https://store.webkul.com/license.html/
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
from odoo import api, fields, models
from collections import defaultdict

import logging
_logger = logging.getLogger(__name__)

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    access_token = fields.Char('Access Token', groups="base.group_user,odoo_marketplace.marketplace_draft_seller_group")

    @api.model
    def check(self, mode, values=None):
        """ Restricts the access to an ir.attachment, according to referred mode """
        if not self.env.user.is_marketplace_user():
            return super(IrAttachment, self).check(mode, values=values)
        else:
            # collect the records to check (by model)
            model_ids = defaultdict(set)            # {model_name: set(ids)}
            if self:
                # DLE P173: `test_01_portal_attachment`
                # self.env['ir.attachment'].flush(['res_model', 'res_id', 'create_uid', 'public', 'res_field'])
                self.env['ir.attachment'].flush_model(['res_model', 'res_id', 'create_uid', 'public', 'res_field'])
                self._cr.execute('SELECT res_model, res_id, create_uid, public, res_field FROM ir_attachment WHERE id IN %s', [tuple(self.ids)])
                for res_model, res_id, create_uid, public, res_field in self._cr.fetchall():
                    if not self.env.is_system() and res_field:
                        raise AccessError(_("Sorry, you are not allowed to access this document."))
                    if public and mode == 'read':
                        continue
                    if not (res_model and res_id):
                        continue
                    model_ids[res_model].add(res_id)
            if values and values.get('res_model') and values.get('res_id'):
                model_ids[values['res_model']].add(values['res_id'])

            # check access rights on the records
            for res_model, res_ids in model_ids.items():
                # ignore attachments that are not attached to a resource anymore
                # when checking access rights (resource was deleted but attachment
                # was not)
                if res_model not in self.env:
                    continue
                if res_model == 'res.users' and len(res_ids) == 1 and self.env.uid == list(res_ids)[0]:
                    # by default a user cannot write on itself, despite the list of writeable fields
                    # e.g. in the case of a user inserting an image into his image signature
                    # we need to bypass this check which would needlessly throw us away
                    continue
                records = self.env[res_model].browse(res_ids).exists()
                # For related models, check if we can write to the model, as unlinking
                # and creating attachments can be seen as an update to the model
                access_mode = 'write' if mode in ('create', 'unlink') else mode
                records.check_access_rights(access_mode)
                records.check_access_rule(access_mode)
