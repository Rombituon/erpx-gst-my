from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Goods and Services Tax (GST Malaysia)"),
			"items": [
				{
					"type": "doctype",
					"name": "MSIC Code",
					"description": _("MSIC Code")
				},
				{
					"type": "doctype",
					"name": "Sales GST Tax Code",
					"description": _("Sales GST Tax Code")
				},
				{
					"type": "doctype",
					"name": "Purchase GST Tax Code",
					"description": _("Purchase GST Tax Code")
				},
				{
					"type": "report",
					"name": "Malaysia GST03",
					"is_query_report": True
				}
			]
		}
	]
