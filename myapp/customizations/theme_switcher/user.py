from frappe.core.doctype.user.user import switch_theme
import frappe

# class Change_Theme(switch_theme):
#     @frappe.whitelist()

def switch_theme(theme,method=None):
    if theme in ["Dark", "Light", "Automatic", "Red", "Brown"]:
        frappe.db.set_value("User", frappe.session.user, "desk_theme", theme)
