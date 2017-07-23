# Copyright (c) 2013, Team010 and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
	return _execute(filters)

def _execute(filters=None, additional_table_columns=None, additional_query_columns=None):
	if not filters: filters = {}
	company_currency = frappe.db.get_value("Company", filters.company, "default_currency")
	output_tax = get_data(company_currency, "OutputTax")
	input_tax = get_data(company_currency, "InputTax")
	tax_amount = get_tax_amount(company_currency, input_tax, output_tax)
	add_info = get_data(company_currency, "AddInfo")

	data = []
	data.extend(output_tax or [])
	data.extend(input_tax or [])
	data.extend(tax_amount or [])
	data.extend(add_info or [])

	columns = get_columns(additional_table_columns)
	return columns, data

#Calculate the output value & tax
def get_output_tax(currency):
	data = []
	section_name = _("Output Tax")
	data.append( generate_fields( 0, section_name ) )
	data.append( generate_fields( 1, _("Total Value of Standard Rated Supply"), section_name, currency, 10000 ) )
	data.append( generate_fields( 1, _("Total Output Tax (Inclusive of Tax Value on Bad Debt Recovered & other Adjustments )"), section_name, currency, 0 ) )
	data.append({}) #insert empty row
	return data

#Calculate the input value & tax
def get_input_tax(currency):
	data = []
	section_name = _("Input Tax")
	data.append( generate_fields( 0, section_name ) )
	data.append( generate_fields( 1, _("Total Value of Standard Rate and Flat Rate Acquisitions"), section_name, currency, 10000000 ) )
	data.append( generate_fields( 1, _("Total Input Tax (Inclusive of Tax Value on Bad Debt Relief & other Adjustments)"), section_name, currency, 10 ) )
	data.append({}) #insert empty row
	return data

#Calculate the submit/claim tax amount
def get_tax_amount(currency, input_tax, output_tax):
	
	input_tax_amt = flt(input_tax[-2]['amount'], 3) if input_tax else 0
	output_tax_amt = flt(output_tax[-2]['amount'], 3) if output_tax else 0
	amount_pay = 0
	amount_claim = 0
	amount = flt(output_tax_amt - input_tax_amt, 3)
	# print amount
	if amount > 0:
		amount_pay = amount
	else:
		amount_claim = abs(amount)

	data = []
	data.append( generate_fields( 0, _("GST Amount Payable"), None, currency, amount_pay ) )
	data.append( generate_fields( 0, _("GST Amount Claimable"), None, currency, amount_claim ) )
	data.append({})
	return data

def get_add_info(currency):
	data = []
	section_name = _("Additional Information")
	data.append( generate_fields( 0, section_name ) )
	data.append( generate_fields( 1, _("Total Value of Local Zero-Rated Supplies"), section_name, currency, 10000000 ) )
	data.append( generate_fields( 1, _("Total Value of Export Supplies"), section_name, currency, 10000000 ) )
	data.append( generate_fields( 1, _("Total Value of Exempt Supplies"), section_name, currency, 10000000 ) )
	data.append( generate_fields( 1, _("Total Value of Supplies Granted GST Relief"), section_name, currency, 10000000 ) )
	data.append( generate_fields( 1, _("Total Value of Goods Imported Under Approved Trader Scheme"), section_name, currency, 10000000 ) )
	data.append( generate_fields( 1, _("Total Value of GST Suspended under item 14"), section_name, currency, 10000000 ) )
	data.append( generate_fields( 1, _("Total Value of Capital Goods Acquired"), section_name, currency, 10000000 ) )
	data.append( generate_fields( 1, _("Total Value of Bad Debt Relief Inclusive Tax"), section_name, currency, 10000000 ) )
	data.append( generate_fields( 1, _("Total Value of Bad Debt Recovered Inclusive Tax"), section_name, currency, 10000000 ) )

	return data


def generate_fields(indent, field_label, section_name=None, currency=None, amount=None):
	row = frappe._dict({
		"field_name": field_label,
		"field": field_label, 
		"indent": indent		
	})

	if indent == 0:
		row["bold"] = True

	if section_name:
		row["parent_field"] = section_name

	if currency:
		row["currency"] = currency
		row["amount"] = amount

	return row

def get_data(currency, root_type):
	logicSwitcher = {
        "OutputTax": get_output_tax,
        "InputTax": get_input_tax,
        "AddInfo": get_add_info,
    }
	return logicSwitcher[root_type](currency)


def get_columns(additional_table_columns):
	columns = [{
		"fieldname": "field",
		"label": _("Fields"),
		"fieldtype": "Data",
		"width": 600
	},{
		"fieldname": "amount",
		"label": _("Amount"),
		"fieldtype": "Currency",
		"options": "Currency",
		"width": 300
	}]

	if additional_table_columns:
		columns += additional_table_columns


	return columns
