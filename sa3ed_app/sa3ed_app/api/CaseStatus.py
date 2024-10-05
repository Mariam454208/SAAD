import frappe

@frappe.whitelist()  
def check_case_status(case_id):
    
    lost_person = frappe.db.get_value('lost_person', {'name': case_id}, ['status'], as_dict=True)
    
    if lost_person:
        return {'status': lost_person['status']}
    
   
    founded_person = frappe.db.get_value('founded_person', {'name': case_id}, ['status'], as_dict=True)
    
    if founded_person:
        return {'status': founded_person['status']}

    return None
