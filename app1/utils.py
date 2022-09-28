import json

from .models import itemtable

def porder_data_validator(porder_data):
    
    # Validate Invoice Info ----------

    # invoice-number
    try:
        puchaseorder_no = int(porder_data['puchaseorder_no'])
    except:
        print("Error: Incorrect Purchase Order Number")
        return "Error: Incorrect Purchase Order Number"