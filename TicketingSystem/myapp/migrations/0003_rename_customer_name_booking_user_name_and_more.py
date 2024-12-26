import django.db.models.deletion
from django.db import migrations, models


def set_default_event(apps, schema_editor):
    Event = apps.get_model('myapp', 'Event')
    Booking = apps.get_model('myapp', 'Booking')
    default_event = Event.objects.first()  # Get the first event or create one if necessary
    if default_event:
        Booking.objects.update(event=default_event)


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_event_ticketcategory_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='customer_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='customer_email',
        ),
        migrations.AddField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='bookings',
                to='myapp.event',
            ),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ticket_category',
            field=models.CharField(max_length=100),
        ),
        migrations.RunPython(set_default_event),  # Apply default setting logic
    ]
