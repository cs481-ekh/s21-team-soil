from django.db import migrations

def create_data(apps, schema_editor):
    Soil = apps.get_model('Soils', 'Soil')
    Soil(lime_or_cement_stabilization="80%", dose_of_lime_or_cement="50%").save()

class Migration(migrations.Migration):

    dependencies = [
        ('Soils', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]