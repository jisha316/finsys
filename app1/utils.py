import json

from .models import itemtable

def update_item_from_purchase(invoice_data_processed, request):
    for item in invoice_data_processed['items']:
        new_product = False
        if itemtable.objects.filter(user=request.user,
                                  product_name=item['invoice_product'],
                                  product_hsn=item['invoice_hsn'],
                                  product_unit=item['invoice_unit'],
                                  product_gst_percentage=item['invoice_gst_percentage']).exists():
            product = itemtable.objects.get(user=request.user,
                                          product_name=item['invoice_product'],
                                          product_hsn=item['invoice_hsn'],
                                          product_unit=item['invoice_unit'],
                                          product_gst_percentage=item['invoice_gst_percentage'])
        else:
            new_product = True
            product = itemtable(user=request.user,
                              product_name=item['invoice_product'],
                              product_hsn=item['invoice_hsn'],
                              product_unit=item['invoice_unit'],
                              product_gst_percentage=item['invoice_gst_percentage'])
        product.product_rate_with_gst = item['invoice_rate_with_gst']
        product.save()