frappe.provide('erpx_malaysia_gst.utils');
erpx_malaysia_gst.utils.downloadify = function (data, roles, title) {
	if (roles && roles.length && !has_common(roles, roles)) {
		frappe.msgprint(__("Export not allowed. You need {0} role to export.", [frappe.utils.comma_or(roles)]));
		return;
	}

	var filename = title + ".txt";
	var txt_data = erpx_malaysia_gst.utils.to_txt(data);
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
};

erpx_malaysia_gst.utils.to_csv = function (data) {
	var res = [];
	$.each(data, function (i, row) {
		row = $.map(row, function (col) {
			return typeof col === "string" ? '"' + col.replace(/"/g, '""') + '"' : col;
		});
		res.push(row.join(","));
	});
	return res.join("\n");
};

erpx_malaysia_gst.utils.fill_in_msic_code = function(frm){
    frm.add_fetch('item_code','mygst_msic_code','mygst_msic_code');          	
}

erpx_malaysia_gst.utils.fill_in_purchase_gst_code = function(frm){
    frm.add_fetch('item_code','mygst_item_purchase_tax_code','mygst_purchase_tax_code');          	
}

erpx_malaysia_gst.utils.fill_in_sales_gst_code = function(frm){
    frm.add_fetch('item_code','mygst_item_sales_tax_code','mygst_sales_tax_code');          	
}