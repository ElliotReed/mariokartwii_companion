import datetime
from django.core.exceptions import ValidationError
from django import forms
# from django.forms import ModelForm
from base.models import Character, Vehicle, GameMode, EngineClass
from .models import WiiTrack


def is_time_set(minutes, seconds, milliseconds):
    minutes_set = minutes > 0
    seconds_set = seconds > 0
    return minutes_set or seconds_set


def get_time_string(minutes, seconds, milliseconds):
    return f'00:{minutes}:{seconds}:{milliseconds}000'


class RecordTimeForm(forms.Form):
    time = forms.HiddenInput()
    numbers = forms.CharField(
        label="Quick entry", max_length=6, required=False, help_text='Enter 6 digits: 1 m, 2 s, 3ms')
    minutes = forms.IntegerField(
        label='Min', min_value=0, max_value=59, required=False, initial=0)
    seconds = forms.IntegerField(
        label='Sec', min_value=0, max_value=59, required=False, initial=0)
    milliseconds = forms.IntegerField(
        label='Milli', min_value=0, max_value=999, required=False, initial=0)
    track = forms.ModelChoiceField(
        queryset=WiiTrack.objects.all(), initial=WiiTrack(label='Luigi Circuit'))
    character = forms.ModelChoiceField(
        queryset=Character.objects.all(), initial=Character(label='Mario'))
    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.all(), initial=Vehicle(label='Standard Kart M'))
    engine_class = forms.ModelChoiceField(
        queryset=EngineClass.objects.all(), initial=EngineClass(label='100cc')
    )
    game_mode = forms.ModelChoiceField(
        queryset=GameMode.objects.all(), initial=GameMode(label='Time Trials'))

    def clean(self):
        cd = self.cleaned_data

        minutes = cd.get('minutes')
        seconds = cd.get('seconds')
        milliseconds = cd.get('milliseconds')

        numbers = cd.get('numbers')

        time_is_set = is_time_set(minutes, seconds, milliseconds)

        if time_is_set:
            # time_string = get_time_string(minutes, seconds, milliseconds)
            # cd['time'] = time_string
            time_delta = datetime.timedelta(
                minutes=minutes, seconds=seconds, milliseconds=milliseconds)
            cd['time'] = time_delta
            return cd

        elif numbers:
            if not numbers.isnumeric():
                raise ValidationError('Must consist of numbers')

            if len(numbers) < 4:
                raise ValidationError('Race must be at least 1 second')

            m = int(numbers[0])
            s = int(numbers[-5:-3])
            ms = int(numbers[-3:])
            mcs = ms * 1000
            # time_string = get_time_string(m, s, ms)
            # cd['time'] = time_string
            time_delta = datetime.timedelta(
                minutes=m, seconds=s, milliseconds=ms)
            cd['time'] = time_delta
            print('cleaning data')
            print(time_delta)
            return cd

        else:
            raise ValidationError(
                'Time or quick entry is required', code='invalid')

        return cd
