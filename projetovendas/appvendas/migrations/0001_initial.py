# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-12 12:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
            ],
            options={
                'permissions': (('view_cargo', 'Can see cargo'),),
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('email', models.EmailField(max_length=200, verbose_name='E-Mail')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('valorUnitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Unitário')),
            ],
            options={
                'permissions': (('view_produto', 'Can see produto'),),
            },
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('sigla', models.CharField(max_length=5, verbose_name='Sigla')),
            ],
            options={
                'permissions': (('view_unidade', 'Can see unidade'),),
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVenda', models.DateField(verbose_name='Data da Venda')),
            ],
            options={
                'permissions': (('view_venda', 'Can see venda'),),
            },
        ),
        migrations.CreateModel(
            name='VendaProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='O valor deve ser maior do que 0')], verbose_name='Quantidade')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appvendas.Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appvendas.Venda')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appvendas.Pessoa')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
            ],
            options={
                'permissions': (('view_cliente', 'Can see cliente'),),
            },
            bases=('appvendas.pessoa',),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appvendas.Pessoa')),
                ('matricula', models.CharField(max_length=10, unique=True, verbose_name='Matrícula')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appvendas.Cargo', verbose_name='Cargo')),
            ],
            options={
                'permissions': (('view_funcionario', 'Can see funcionario'),),
            },
            bases=('appvendas.pessoa',),
        ),
        migrations.AddField(
            model_name='venda',
            name='produtos',
            field=models.ManyToManyField(through='appvendas.VendaProduto', to='appvendas.Produto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appvendas.Unidade', verbose_name='Unidade'),
        ),
        migrations.AddField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appvendas.Cliente', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='venda',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appvendas.Funcionario', verbose_name='Funcionário'),
        ),
    ]
