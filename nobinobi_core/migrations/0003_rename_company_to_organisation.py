# Generated by Django 3.1.2 on 2020-10-08 12:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_core', '0002_add_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationClosure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('from_date', models.DateField(verbose_name='From date')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Organisation closure',
                'verbose_name_plural': 'Organisation closures',
                'ordering': ('from_date', 'end_date'),
            },
        ),
        migrations.AlterModelOptions(
            name='organisation',
            options={'ordering': ('name', 'short_code'), 'verbose_name': 'Organisation', 'verbose_name_plural': 'Organisations'},
        ),
        migrations.RenameModel(
            old_name='Company',
            new_name='Organisation',
        ),
        migrations.DeleteModel(
            name='CompanyClosure',
        ),
        migrations.AddField(
            model_name='organisationclosure',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nobinobi_core.organisation', verbose_name='Organisation'),
        ),
    ]
