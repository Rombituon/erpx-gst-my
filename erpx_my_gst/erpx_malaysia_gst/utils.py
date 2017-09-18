from __future__ import unicode_literals

import frappe
from frappe import _, msgprint
from frappe.model.utils import get_fetch_values
from frappe.contacts.doctype.address.address import get_address_display, get_default_address

@frappe.whitelist()
def get_party_country(party=None, party_type="Customer", company=None,doctype=None, ignore_permissions=False):

	if not party:
		return {}

	if not frappe.db.exists(party_type, party):
		frappe.throw(_("{0}: {1} does not exists").format(party_type, party))

	return _get_party_country(party, party_type, company, doctype)

def _get_party_country(party=None, party_type="Customer", company=None, doctype=None, ignore_permissions=False):

	out = { party_type.lower(): party }

	party = out[party_type.lower()]

	if not ignore_permissions and not frappe.has_permission(party_type, "read", party):
		frappe.throw(_("Not permitted for {0}").format(party), frappe.PermissionError)

	party = frappe.get_doc(party_type, party)

	if party_type in ["Company"]:
		get_company_country(out, party)
	else:
		get_address_country(out, party, party_type, doctype, company)

	return out

def get_company_country(out, party):
	out["company_country"] = party.country


def get_address_country(out, party, party_type, doctype=None, company=None):
	billing_address_field = "customer_address" if party_type == "Lead" \
		else party_type.lower() + "_address"
	out[billing_address_field] = get_default_address(party_type, party.name)
	out.update(get_fetch_values(doctype, billing_address_field, out[billing_address_field]))

	# # address display
	# out.address_display = get_address_display(out[billing_address_field])

	# address country
	address_dict = frappe.db.get_value("Address", out[billing_address_field], "*", as_dict=True) or {}
	billing_country_field = "customer_country" if party_type == "Lead" \
		else party_type.lower() + "_country"
	out[billing_country_field] = address_dict.country
	out.update(get_fetch_values(doctype, billing_country_field, out[billing_country_field]))


	# # shipping address
	# if party_type in ["Customer", "Lead"]:
	# 	out.shipping_address_name = get_default_address(party_type, party.name, 'is_shipping_address')
	# 	out.shipping_address = get_address_display(out["shipping_address_name"])
	# 	out.update(get_fetch_values(doctype, 'shipping_address_name', out.shipping_address_name))

	# if doctype and doctype in ['Sales Invoice']:
	# 	out.company_address = get_default_address('Company', company)
	# 	out.update(get_fetch_values(doctype, 'company_address', out.company_address))