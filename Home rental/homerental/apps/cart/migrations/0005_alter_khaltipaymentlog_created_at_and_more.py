# Generated by Django 5.2.1 on 2025-05-12 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0004_remove_khaltipaymentlog_property_info_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="khaltipaymentlog",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="khaltipaymentlog",
            name="mobile",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="khaltipaymentlog",
            name="pidx",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="khaltipaymentlog",
            name="purchase_order_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="khaltipaymentlog",
            name="status",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="khaltipaymentlog",
            name="total_amount",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="khaltipaymentlog",
            name="transaction_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
