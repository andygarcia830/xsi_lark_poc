import frappe
import requests,json

from frappe.model.document import Document


def fetch_token():
    lark_settings = frappe.get_doc('Lark Integration Settings')
    print(lark_settings.app_id)
    body = {'app_id':lark_settings.app_id,'app_secret':lark_settings.app_secret}
    jsonStr = json.dumps(body)
    endpoint = 'https://open.larksuite.com/open-apis/auth/v3/app_access_token/internal'
    x = requests.post(endpoint, data = jsonStr)
    resp = json.loads(x.text)
    # print (f'AUTH RESPONSE {resp}')
    return resp['app_access_token']


def fetch_employee_record(custom_lark_user_id, date):
    endpoint = 'https://open.larksuite.com/open-apis/attendance/v1/user_tasks/query?employee_type=employee_id'
    access_token = fetch_token()
    headers={'Authorization':'Bearer '+access_token,'Content-Type':'application/JSON'}
    body = {'user_ids':[custom_lark_user_id],
            'check_date_from':date,
            'check_date_to':date
            }
    jsonStr = json.dumps(body)
    x = requests.post(endpoint, headers=headers, data = jsonStr)
    resp = json.loads(x.text)
    try:
        results = resp['data']['user_task_results']
        print (f'ATTENDANCE RESPONSE {results}')
        if len(results) > 0:
            for item in results:
                record = item['records'][0]
                print (f'RECORDS {record}')
                if record['check_in_result_supplement'] == 'Leave' or \
                record['check_out_result_supplement'] == 'Leave':
                    return 'On Leave'
                else:
                    return 'Present'

        else:
            frappe.msgprint('No Record for that Day')
    except:
        frappe.msgprint('No Record for that Day')



@frappe.whitelist()
def fetch_entries(employee, date):
    employee = frappe.get_doc('Employee', employee, fields=['name', 'custom_lark_user_id'])
    
    print(f'LARK_ID {employee.custom_lark_user_id}')
    print(date.replace('-',''))
    return fetch_employee_record(employee.custom_lark_user_id, date.replace('-',''))



@frappe.whitelist()
def batch_fetch_entries(date):
    employees = frappe.db.get_list('Employee', fields=['name', 'custom_lark_user_id'])
    
    for employee in employees:
        print(f'LARK_ID {employee.custom_lark_user_id}')
        print(date.replace('-',''))
        result = fetch_employee_record(employee.custom_lark_user_id, date.replace('-',''))
        attendance = frappe.new_doc('Attendance')
        attendance.employee = employee.name
        attendance.attendance_date = date
        attendance.status = result
        if result == 'On Leave':
            attendance.leave_type = 'Sick Leave'
        if not attendance.status == None:
            attendance.save()
            attendance.submit()

