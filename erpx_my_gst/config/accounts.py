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
					"name": "GST Tax Code",
					"description": _("GST Tax Code")
				},
				{
					"type": "report",
					"name": "Malaysia GST03",
					"is_query_report": True
				}
			]
		}
	]
