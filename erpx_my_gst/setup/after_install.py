from __future__ import unicode_literals

import frappe, os, json

def initial_setup():
	update_address_template()
	add_msic_codes()
	add_gst_tax_codes()

def update_address_template():
	with open(os.path.join(os.path.dirname(__file__), "address_template.html")) as f:
		html = f.read()
	print "Updating Malaysia Address"
	address_template = frappe.db.get_value('Address Template', 'Malaysia')
	if address_template:
		frappe.db.set_value('Address Template', 'Malaysia', 'template', html)
	else:
		# make new html template for Malaysia
		frappe.get_doc(dict(
			doctype='Address Template',
			country='Malaysia',
			template=html
		)).insert()

def add_msic_codes():
	if frappe.db.count('MSIC Code') > 100:
		return
	print "Updating MISC Code"
	with open(os.path.join(os.path.dirname(__file__), 'malaysia_msic.json'), 'r') as f:
		msic_codes = json.loads(f.read())

	frappe.db.commit()
	frappe.db.sql('truncate `tabMSIC Code`')

	for d in msic_codes:
		msic_code = frappe.new_doc('MSIC Code')
		msic_code.update(d)
		msic_code.name = msic_code.misc_code
		msic_code.db_insert()

	frappe.db.commit()

def add_gst_tax_codes():
	if frappe.db.count('GST Tax Code') > 100:
		return
	print "Updating GST Tax Code"
	with open(os.path.join(os.path.dirname(__file__), 'gst_tax_code.json'), 'r') as f:
		gst_tax_codes = json.loads(f.read())

	frappe.db.commit()
	frappe.db.sql('truncate `tabGST Tax Code`')

	for d in gst_tax_codes:
		gst_tax_code = frappe.new_doc('GST Tax Code')
		gst_tax_code.update(d)
		gst_tax_code.name = gst_tax_code.tax_code
		gst_tax_code.db_insert()

	frappe.db.commit()