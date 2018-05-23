import frappe

def execute():
	frappe.reload_doc("core", "doctype", "docfield", force=True)
	frappe.reload_doc("custom", "doctype", "custom_field", force=True)
	frappe.reload_doc("custom", "doctype", "customize_form_field", force=True)
	frappe.reload_doc("custom", "doctype", "property_setter", force=True)

	frappe.db.sql('''
		update `tabDocField`
		set fetch_from = options, options=''
		where options like '%.%' and (fetch_from is NULL OR fetch_from='')
 		and fieldtype in ('Data', 'Read Only', 'Text', 'Small Text', 'Text Editor', 'Code', 'Link')
 		and fieldname!='naming_series'
	''')

	frappe.db.sql('''
		update `tabCustom Field`
		set fetch_from = options, options=''
		where options like '%.%' and (fetch_from is NULL OR fetch_from='')
 		and fieldtype in ('Data', 'Read Only', 'Text', 'Small Text', 'Text Editor', 'Code', 'Link')
 		and fieldname!='naming_series'
	''')

	frappe.db.sql('''
		update `tabProperty Setter`
		set property="fetch_from"
		where property="options" and value like '%.%'
		and property_type in ('Data', 'Read Only', 'Text', 'Small Text', 'Text Editor', 'Code', 'Link')
	''')
