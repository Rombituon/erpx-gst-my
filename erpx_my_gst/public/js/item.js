frappe.ui.form.on('Item',{
	onload: function(frm){
		frm.add_fetch('mygst_tax_code','rate','tax_rate');   
	}
})