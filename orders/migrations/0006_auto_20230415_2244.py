# Generated by Django 3.1 on 2023-04-15 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0005_auto_20230415_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
