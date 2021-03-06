# Generated by Django 3.2.5 on 2021-07-14 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('picture', models.BinaryField(editable=True, null=True)),
                ('content_type', models.CharField(help_text='The MIMEType of the file', max_length=256, null=True)),
                ('preco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laco.preco')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laco.tema')),
            ],
        ),
    ]
