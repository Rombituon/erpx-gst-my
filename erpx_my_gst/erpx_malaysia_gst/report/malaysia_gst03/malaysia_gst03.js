// Copyright (c) 2016, Team010 and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Malaysia GST03"] = {
    "filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_start_date"),
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company")
		}
	],
	"tree": true,
	"name_field": "field",
	"parent_field": "parent_field",
	"initial_depth": 3,
	formatter: function(row, cell, value, columnDef, dataContext, default_formatter) {
		if (columnDef.df.fieldname=="field") {
			value = dataContext.field_name;
			columnDef.df.is_tree = true;
		}

		value = default_formatter(row, cell, value, columnDef, dataContext);

		if (dataContext.bold) {
			var $value = $(value).css("font-weight", "bold");
			value = $value.wrap("<p></p>").parent().html();
		}

		return value;
	},
	onload: function(report) {
		var me = this;
		report.page.add_inner_button(__("Generate GST03 PDF"), function() {
			var filters = report.get_values();
		})
		report.page.add_inner_button(__("Generate TAP File"), function() {
			var filters = report.get_values();
			me.generate_tap(report);
		})
	},

	generate_tap: function(report) {
		var me = report;
		var that = this;
		//this.title = this.report_name;

		if (!frappe.model.can_export(report.report_doc.ref_doctype)) {
			frappe.msgprint(__("You are not allowed to generate this TAP file"));
			return false;
		}

		frappe.prompt({ fieldtype: "Check", label: __("Do you choose to carry forward refund"), fieldname: "carry_forward", default: false, reqd: 0 }, function (data) {
			var view_data = frappe.slickgrid_tools.get_view_data(me.columns, me.dataView);
			var result = view_data.map(function (row) {
				return row.splice(1);
			});

			var visible_idx = view_data.map(function (row) {
				return row[0];
			}).filter(function (sr_no) {
				return sr_no !== 'Sr No';
			});

			//if (data.file_format_type == "CSV") {
				that.downloadify(result, null, me.report_name);
			//}
		}, __("Generate TAP File"), __("Generate"));

		return false;
	},

	downloadify : function (data, roles, title) {
	if (roles && roles.length && !has_common(roles, roles)) {
		frappe.msgprint(__("Export not allowed. You need {0} role to export.", [frappe.utils.comma_or(roles)]));
		return;
	}

	var filename = title + ".txt";
	var txt_data = this.to_txt(data);
	var a = document.createElement('a');

	if ("download" in a) {
		var blob_object = new Blob([txt_data], { type: 'text/plain;charset=UTF-8' });
		a.href = URL.createObjectURL(blob_object);
		a.download = filename;
	} else {
		a.href = 'data:attachment/txt,' + encodeURIComponent(txt_data);
		a.download = filename;
		a.target = "_blank";
	}

	document.body.appendChild(a);
	a.click();

	document.body.removeChild(a);
},

to_txt : function (data) {
	var res = [];
	$.each(data, function (i, row) {
		// row = $.map(row, function (col) {
		// 	return typeof col === "string" ? '"' + col.replace(/"/g, '""') + '"' : col;
		// });
		res.push(row.join("|"));
	});
	return res.join("\n");
}
}
