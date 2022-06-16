from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import WiiTrackTime
from .forms import RecordTimeForm
from user.models import User


def get_initial_wii(request):
    user = request.user
    lastEntryList = WiiTrackTime.objects.filter(
        user=user).order_by('-created_at')[:1]
    if not lastEntryList:
        initial = None
    else:
        lastEntry = lastEntryList[0]
        initial = {
            'track': lastEntry.track,
            'character': lastEntry.character,
            'vehicle': lastEntry.vehicle,
            'engine_class': lastEntry.engine_class,
            'game_mode': lastEntry.game_mode,
        }
    return initial


def index(request):
    user_tracks = WiiTrackTime.objects.all().order_by('time')
    context = {'tracks': user_tracks}
    return render(request, 'timetracker/index.html', context)


def wii(request):
    context = {}
    return render(request, 'timetracker/index.html', context)


@login_required(login_url='user/login')
def wiiRecord(request):

    if request.method == 'POST':
        print('posted')
        form = RecordTimeForm(request.POST)
        if form.is_valid():
            best_track = None
            reply = {
                'message': '',
                'is_new': False,
            }
            cd = form.cleaned_data
            time = cd.get('time')
            user = request.user
            track = cd.get('track')
            character = cd.get('character')
            vehicle = cd.get('vehicle')
            engine_class = cd.get('engine_class')
            game_mode = cd.get('game_mode')
            track_record, created = WiiTrackTime.objects.get_or_create(
                user=user, track=track, character=character, vehicle=vehicle, engine_class=engine_class, game_mode=game_mode)
            if created:
                track_record.time = time
                track_record.save()
                best_track = track_record
                reply['message'] = 'A new record was created!'
                reply['is_new'] = True
            else:
                if track_record.time <= time:
                    best_track = track_record
                    reply['message'] = 'Current record stands..keep trying!'
                    reply['is_new'] = False
                else:
                    track_record.time = time
                    track_record.save()
                    best_track = track_record
                    reply['message'] = 'A new record!'
                    reply['is_new'] = True

            new_form = RecordTimeForm(initial=get_initial_wii(request))
            context = {'form': new_form, 'track': best_track, 'reply': reply}
            return render(request, 'timetracker/record.html', context)
            print(track_record)

    else:
        form = RecordTimeForm(initial=get_initial_wii(request))
        # form = RecordTimeForm()
    context = {'form': form}
    return render(request, 'timetracker/record.html', context)
