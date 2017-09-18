# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpx_my_gst"
app_title = "ERPX Malaysia GST"
app_publisher = "Team010"
app_description = "Malaysia GST Module for ERP-X"
app_icon = "octicon octicon-repo"
app_color = "red"
app_email = "gentiger@gmail.com"
app_license = "UNLICENSED"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpx_my_gst/css/erpx_my_gst.css"
app_include_js = "/assets/js/erpx_my_gst.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpx_my_gst/css/erpx_my_gst.css"
# web_include_js = "/assets/erpx_my_gst/js/erpx_my_gst.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doctype_js = {
    "Company": ["public/js/company.js"],
    "Item": ["public/js/item.js"],
    "Quotation": ["public/js/msiccodehandler.js"],
    "Sales Order": ["public/js/msiccodehandler.js"],
    "Delivery Note" : ["public/js/msiccodehandler.js"],
    "Sales Invoice" : ["public/js/msiccodehandler.js"],
    "Purchase Order" : ["public/js/msiccodehandler.js"],
    "Purchase Receipt" : ["public/js/msiccodehandler.js"],
    "Purchase Invoice" : ["public/js/msiccodehandler.js"]
}

#fixtures = ["Custom Field"]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpx_my_gst.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpx_my_gst.setup.after_install.initial_setup"
after_install = "erpx_my_gst.setup.after_install.initial_setup"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpx_my_gst.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpx_my_gst.tasks.all"
# 	],
# 	"daily": [
# 		"erpx_my_gst.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpx_my_gst.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpx_my_gst.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpx_my_gst.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpx_my_gst.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpx_my_gst.event.get_events"
# }

