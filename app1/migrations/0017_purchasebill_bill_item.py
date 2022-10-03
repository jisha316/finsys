# Generated by Django 4.0.4 on 2022-09-30 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_rename_contact_address_purchaseorder_contact_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchasebill',
            fields=[
                ('billid', models.AutoField(primary_key=True, serialize=False, verbose_name='bid')),
                ('vendor_name', models.CharField(max_length=100)),
                ('billing_address', models.TextField()),
                ('bill_no', models.IntegerField(default=1000)),
                ('sourceofsupply', models.CharField(max_length=100, null=True)),
                ('destiofsupply', models.CharField(max_length=100, null=True)),
                ('branch', models.CharField(max_length=100, null=True)),
                ('reference', models.CharField(max_length=100, null=True)),
                ('contact_name', models.CharField(max_length=255, null=True)),
                ('deliverto', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
                ('deliver_date', models.DateField(null=True)),
                ('credit_period', models.CharField(max_length=100, null=True)),
                ('due_date', models.CharField(max_length=100, null=True)),
                ('sub_total', models.CharField(max_length=100, null=True)),
                ('sgst', models.CharField(max_length=100, null=True)),
                ('cgst', models.CharField(max_length=100, null=True)),
                ('igst', models.CharField(max_length=100, null=True)),
                ('discount', models.CharField(default=0, max_length=100)),
                ('tcs', models.CharField(max_length=100, null=True)),
                ('tcs_amount', models.CharField(max_length=100, null=True)),
                ('round_off', models.CharField(max_length=100, null=True)),
                ('tax_amount', models.CharField(max_length=100, null=True)),
                ('grand_total', models.CharField(max_length=100, null=True)),
                ('note', models.CharField(max_length=255, null=True)),
                ('file', models.FileField(default=None, upload_to='purchaseorder')),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Approved', 'Approved'), ('Billed', 'Billed')], default='Draft', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='bill_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('amount', models.CharField(max_length=100, null=True)),
                ('bid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchaseorder')),
            ],
        ),
    ]
