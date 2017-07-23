frappe.ui.form.on('Company', 'validate', function(frm) {
        set_my_gst_field_mandatory(frm);
    }
)

frappe.ui.form.on('Company', 'country', function(frm, cdt, cdn) {
        set_my_gst_field_mandatory(frm);
    }
)

var set_my_gst_field_mandatory = function(frm){
    if(frm.doc.country == "Malaysia"){
        frm.set_df_property("business_registration_number", "reqd", true);
	    frm.set_df_property("gst_id", "reqd", true);
    } else {
        frm.set_df_property("business_registration_number", "reqd", false);
	    frm.set_df_property("gst_id", "reqd", false);
    }            	
    frm.refresh();
}