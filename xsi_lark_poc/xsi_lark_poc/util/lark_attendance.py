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


# def fetch_employee_record_old(custom_lark_user_id, date):
#     endpoint = 'https://open.larksuite.com/open-apis/attendance/v1/user_approvals/query?employee_type=employee_id'
#     # endpoint = 'https://open.larksuite.com/open-apis/attendance/v1/user_tasks/query?employee_type=employee_id'
#     access_token = fetch_token()
#     headers={'Authorization':'Bearer '+access_token,'Content-Type':'application/JSON'}
#     body = {'user_ids':[custom_lark_user_id],
#             'check_date_from':date,
#             'check_date_to':date
#             }
#     jsonStr = json.dumps(body)
#     x = requests.post(endpoint, headers=headers, data = jsonStr)
#     resp = json.loads(x.text)
#     try:
#         results = resp['data']['user_task_results']
#         print (f'ATTENDANCE RESPONSE {results}')
#         if len(results) > 0:
#             for item in results:
#                 record = item['records'][0]
#                 print (f'RECORDS {record}')
#                 if record['check_in_result_supplement'] == 'Leave' or \
#                 record['check_out_result_supplement'] == 'Leave':
#                     return 'On Leave'
#                 else:
#                     return 'Present'

#         else:
#             frappe.msgprint('No Record for that Day')
#     except:
#         frappe.msgprint('No Record for that Day')

def fetch_employee_record(custom_lark_user_id, date):
    endpoint = 'https://open.larksuite.com/open-apis/attendance/v1/user_approvals/query?employee_type=employee_id'
    # endpoint = 'https://open.larksuite.com/open-apis/attendance/v1/user_tasks/query?employee_type=employee_id'
    access_token = fetch_token()
    headers={'Authorization':'Bearer '+access_token,'Content-Type':'application/JSON'}
    body = {'user_ids':[custom_lark_user_id],
            'check_date_from':date,
            'check_date_to':date
            }
    jsonStr = json.dumps(body)
    x = requests.post(endpoint, headers=headers, data = jsonStr)
    resp = json.loads(x.text)
    print(f'RESP {resp}')
    try:
        results = resp['data']['user_approvals']
        print (f'ATTENDANCE RESPONSE {results}')
        if len(results) > 0:
            for item in results:
                record = item['leaves'][0]['i18n_names']['en']
                print (f'RECORDS {record}')
                return record
        else:
            return 'Present'
    except:
        return 'Present'

def fetch_employee_id(employee):
    if employee.company_email:
        endpoint = 'https://open.larksuite.com/open-apis/contact/v3/users/batch_get_id?user_id_type=user_id'
        access_token = fetch_token()
        headers={'Authorization':'Bearer '+access_token,'Content-Type':'application/JSON'}
        body = {'emails':[employee.company_email], 'include_resigned': 'true'
                }
        jsonStr = json.dumps(body)
        x = requests.post(endpoint, headers=headers, data = jsonStr)
        resp = json.loads(x.text)
        print(f'RESP EMAIL {resp}')
        try:
            results = resp['data']['user_list']
            print (f'USER ID RESPONSE {results}')
            if len(results) > 0:
                for item in results:
                    record = item['user_id']
                    print (f'RECORDS {record}')
                    return record
        except:
            print('Exception')
        
    if employee.cell_number:
        endpoint = 'https://open.larksuite.com/open-apis/contact/v3/users/batch_get_id?user_id_type=user_id'
        access_token = fetch_token()
        headers={'Authorization':'Bearer '+access_token,'Content-Type':'application/JSON'}
        body = {'mobiles':[employee.cell_number], 'include_resigned': 'true'
                }
        jsonStr = json.dumps(body)
        x = requests.post(endpoint, headers=headers, data = jsonStr)
        resp = json.loads(x.text)
        print(f'RESP MOBILE {resp}')
        try:
            results = resp['data']['user_list']
            print (f'USER ID RESPONSE {results}')
            if len(results) > 0:
                for item in results:
                    record = item['user_id']
                    print (f'RECORDS {record}')
                    return record
        except:
            pass
    return None




@frappe.whitelist()
def fetch_entries(employee, date):
    employee = frappe.get_doc('Employee', employee, fields=['name', 'custom_lark_user_id'])
    
    print(f'LARK_ID {employee.custom_lark_user_id}')
    print(date.replace('-',''))
    return fetch_employee_record(employee.custom_lark_user_id, date.replace('-',''))



@frappe.whitelist()
def batch_fetch_entries(date):
    employees = frappe.db.get_list('Employee', filters={'status': 'Active'}, fields=['name', 'custom_lark_user_id', 'company_email', 'cell_number'])
    
    for employee in employees:
        print(f'LARK_ID {employee.name} {employee.custom_lark_user_id}')
        print(date.replace('-',''))
        if (employee.custom_lark_user_id == None) or (len(employee.custom_lark_user_id) == 0):
            employee.custom_lark_user_id = fetch_employee_id(employee)
            if (employee.custom_lark_user_id != None) and (len(employee.custom_lark_user_id) > 0):
                emp = frappe.get_doc('Employee', employee.name)
                emp.custom_lark_user_id = employee.custom_lark_user_id
                emp.save()
                frappe.db.commit()

        if employee.custom_lark_user_id:
            result = fetch_employee_record(employee.custom_lark_user_id, date.replace('-',''))
            attendance = frappe.new_doc('Attendance')
            attendance.employee = employee.name
            attendance.attendance_date = date
            if result.lower().find('leave') > 0:
                attendance.status = 'On Leave'
                attendance.leave_type = result
                # leave = frappe.new_doc('Leave Application')
                # leave.leave_type = result
                # leave.employee = employee.name
                # leave.from_date = date
                # leave.to_date = date

            else:
                attendance.status = result
            if not attendance.status == None:
                try:
                    attendance.save()
                    attendance.submit()
                except:
                    pass
                # frappe.db.commit()

