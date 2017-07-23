frappe.ui.form.on('Sales Taxes and Charges Template',{
	onload: function(frm){
		set_my_tax_id_mandatory(frm);
	}, 
	company: function(frm) {
        set_my_tax_id_mandatory(frm);
    }
})

frappe.ui.form.on('Purchase Taxes and Charges Template',{
    onload: function(frm){
        set_my_tax_id_mandatory(frm);
    }, 
    company: function(frm) {
        set_my_tax_id_mandatory(frm);
    }
})

var set_my_tax_id_mandatory = function(frm){
    debugger;
    frm.add_fetch('company','country','country');

    if(frm.doc.country == "Malaysia"){
        frm.set_df_property("my_tax_code", "reqd", true);
    } else {
        frm.set_df_property("my_tax_code", "reqd", false);
    }            	
	frm.refresh();
}