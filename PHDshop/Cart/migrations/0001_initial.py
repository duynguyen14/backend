# Generated by Django 5.0.6 on 2024-11-14 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0006_alter_user_email'),
        ('good', '0003_alter_good_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='customer.user')),
            ],
        ),
        migrations.CreateModel(
            name='CartGood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_Goods', to='Cart.cart')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_Goods', to='good.good')),
            ],
            options={
                'unique_together': {('cart', 'good')},
            },
        ),
    ]
