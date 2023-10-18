import json

class SdkTracker:
    inclusion_list = [
        'create_p12_keys_request', 
        'delete_bulk_p12_keys_request',
        'capture_payment_request',
        'create_credit_request',
        'add_negative_list_request',
        'create_bundled_decision_manager_case_request',
        'fraud_marking_action_request',
        'check_payer_auth_enrollment_request',
        'payer_auth_setup_request',
        'validate_request',
        'create_payment_request',
        'increment_auth_request',
        'create_plan_request',
        'refund_capture_request',
        'refund_payment_request',
        'auth_reversal_request',
        'mit_reversal_request',
        'create_subscription_request',
        'update_subscription',
        'create_shared_secret_keys_request',
        'create_shared_secret_keys_verifi_request',
        'delete_bulk_symmetric_keys_request',
        'tax_request',
        'void_tax_request',
        'validate_export_compliance_request',
        'verify_customer_address_request',
        'mit_void_request',
        'void_capture_request',
        'void_credit_request',
        'void_payment_request',
        'void_refund_request'
    ]

    def __init__(self):
        pass

    def insert_developer_id_tracker(self, request_obj, request_class, run_environment):
        request_obj = request_obj.replace('\"_', '\"')
        if request_class in self.inclusion_list:
            developer_id_value = ''
            tester = json.loads(request_obj)

            if 'apitest.cybersource.com' in run_environment:
                developer_id_value = 'J0TV2I9S'
            else:
                developer_id_value = 'KZUR4KZ4'

            if 'client_reference_information' not in tester:
                tester['client_reference_information'] = {}
            if 'partner' not in tester['client_reference_information']:
                tester['client_reference_information']['partner'] = {}
            if 'developer_id' not in tester['client_reference_information']['partner'] or not tester['client_reference_information']['partner']['developer_id']:
                tester['client_reference_information']['partner']['developer_id'] = developer_id_value
                
            request_with_tracker = json.dumps(tester)
            return request_with_tracker
        return request_obj