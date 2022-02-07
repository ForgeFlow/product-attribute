# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _get_qty_available_for_stock_state(self):
        """
        This method can be overridden to provide the available qty.
        In some cases you could prefer to use the qty_available - outgoing_qty
        to take into account products reserved
        """
        self.ensure_one()
        return self.qty_available_not_res

    @api.depends(
        "qty_available_not_res",
        "qty_available",
        "incoming_qty",
        "stock_state_threshold",
        "company_id.stock_state_threshold",
    )
    def _compute_stock_state(self):
        return super()._compute_stock_state()
