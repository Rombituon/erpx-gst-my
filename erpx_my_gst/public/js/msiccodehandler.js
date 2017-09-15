frappe.ui.form.on('Sales Order',{
	onload: function(frm){
		fill_in_msic_code(frm);
	}
})

frappe.ui.form.on('Delivery Note',{
	onload: function(frm){
		fill_in_msic_code(frm);
	}
})


frappe.ui.form.on('Sales Invoice',{
	onload: function(frm){
		fill_in_msic_code(frm);
	}
})

frappe.ui.form.on('Purchase Order',{
	onload: function(frm){
		fill_in_msic_code(frm);
	}
})

frappe.ui.form.on('Purchase Receipt',{
	onload: function(frm){
		fill_in_msic_code(frm);
	}
})

frappe.ui.form.on('Purchase Invoice',{
	onload: function(frm){
		fill_in_msic_code(frm);
	}
})



// frappe.ui.form.on("Sales Order", "onload", function(frm, cdt, cdn) {
// 	debugger;
// 	frm.add_fetch("item_code", "my_gst_msic_code", "my_gst_msic_code");
// })

var fill_in_msic_code = function(frm){
	debugger;
    frm.add_fetch('item_code','mygst_msic_code','mygst_msic_code');          	
}