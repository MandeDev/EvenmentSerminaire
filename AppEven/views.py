from django.shortcuts import render
from django.http import HttpResponse
from icalendar import Calendar, Event
from datetime import datetime

def generer_ics(request):
    # Initialisez directement les données dans les variables
    event_name = "L'optimisation de la disponibilité des services informatiques avec VCENTER"
    event_description = "Seminaire de cloture"
    event_localisation = "HTTI est situé au Mfoundi mall, 3e étage. Infoline : 695 87 35 42 | 676 42 27 04"
    event_contact = "695 87 35 42,676 42 27 04"
    event_start = datetime(2023, 11, 4, 9, 0, 0)
    event_end = datetime(2023, 11, 4, 12, 0, 0)
    organizer_email = "HiGH-TECH TRAINING INSTITUTE"

    # Créez un objet de calendrier
    cal = Calendar()
    event = Event()

    event['uid'] = '1234567890'
    event['dtstamp'] = datetime(2023, 11, 3, 12, 0, 0)
    event['dtstart'] = event_start
    event['dtend'] = event_end
    event['summary'] = event_name
    event['description'] = event_description
    event['localisation'] = event_localisation
    event['contact'] = event_contact
    event['organizer'] = f"mailto:{organizer_email}"

    cal.add_component(event)

    response = HttpResponse(cal.to_ical(), content_type='text/calendar')
    response['Content-Disposition'] = 'inline; filename="evenement.ics"'

    return response
