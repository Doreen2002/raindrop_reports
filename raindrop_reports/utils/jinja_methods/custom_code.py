import frappe 

@frappe.whitelist()
def get_account(parent):
    return frappe.db.get_all ( "Journal Entry Account",  filters={"parent": parent}, fields=['*])
