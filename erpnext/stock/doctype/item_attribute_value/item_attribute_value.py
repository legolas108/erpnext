# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class ItemAttributeValue(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		abbr: DF.Data
		attribute_value: DF.Data
		num_pots_per_flat: DF.Int
		num_seeds_per_flat: DF.Int
		num_tags_per_flat: DF.Int
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		potsize: DF.Link | None
	# end: auto-generated types

	pass
