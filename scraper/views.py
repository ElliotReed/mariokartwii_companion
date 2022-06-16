from django.shortcuts import render, redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from base.models import Character, CharacterBonus, Vehicle, VehicleStat, CTGPCup, CTGPTrack, WiiCup, WiiTrack, GameMode, EngineClass

import json

url_ctgp = "http://wiki.tockdom.com/wiki/CTGP_Revolution"
url_wii = "https://www.mariowiki.com/Mario_Kart_Wii"
position_count = 1


def add_vehicles_to_db(data):
    for vehicle in data:
        stats = vehicle['stats']

        newStats, created = VehicleStat.objects.get_or_create(label=stats['label'], total=stats['total'], speed=stats['speed'], weight=stats['weight'],
                                                              acceleration=stats['acceleration'], handling=stats['handling'], drift=stats['drift'], offroad=stats['offroad'], miniturbo=stats['miniturbo'])

        newStats.save()

        newVehicle, created = Vehicle.objects.get_or_create(
            label=vehicle['label'], stats=newStats, vehicle_class=vehicle['class'], vehicle_type=vehicle['type'], image=vehicle['image'])

        newVehicle.save()

    return


def add_characters_to_db(data):
    for character in data:
        bonus = character['bonus']

        newBonus, created = CharacterBonus.objects.get_or_create(label=bonus['label'], total=bonus['total'], speed=bonus['speed'], weight=bonus['weight'],
                                                                 acceleration=bonus['acceleration'], handling=bonus['handling'], drift=bonus['drift'], offroad=bonus['offroad'], miniturbo=bonus['miniturbo'])

        newBonus.save()

        newCharacter, created = Character.objects.get_or_create(
            label=character['label'], bonus=newBonus, character_class=character['class'], image=character['image'])

        newCharacter.save()

    return


def add_or_update_cup(currentCup, cup_image):
    cup, created = CTGPCup.objects.get_or_create(
        label=currentCup, image=cup_image)
    cup.save()


def add_or_update_track(currentCup, scraped_track, order):
    track, created = CTGPTrack.objects.get_or_create(label=scraped_track)
    track.active = True
    track.order = order
    track.save()
    add_to_default_tracks(currentCup, scraped_track)


def add_to_default_tracks(currentCup, scraped_track):
    track = CTGPTrack.objects.get(label=scraped_track)
    ctgp_cup = CTGPCup.objects.get(label=currentCup)
    ctgp_cup.default_tracks.add(track)
    return


def ctgpScraper():
    html = requests.get(url_ctgp).text
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find_all('table', class_='sortable')
    trackTable = tables[0]
    trackTableBody = trackTable.tbody
    tableRows = trackTableBody.find_all('tr')

    # Clear all cup data
    CTGPCup.objects.all().delete()

    # Clear active status all tracks
    currentTracks = CTGPTrack.objects.all()
    if len(currentTracks) > 0:
        for track in currentTracks:
            track.active = False
            track.save()

    # Variables for adding cup to tracks
    currentCup = None

    def handle_position_count():
        global position_count
        if position_count == 4:
            position_count = 1
        else:
            position_count += 1

    for row in tableRows:
        tds = row.find_all('td')
        if len(tds) > 0:
            isRowSpan = tds[0].has_attr('rowspan')
            if isRowSpan:

                if tds[0]['rowspan'] == '4':  # Regular Cup row
                    currentCup = tds[0]['data-sort-value'].strip()
                    print(tds[0].get_text())
                    cup_image = tds[0].get_text().strip().replace(
                        ' ', '_').replace('?', 'Question') + '.png'
                    add_or_update_cup(currentCup, cup_image)
                    scraped_track = tds[1].a.contents[0].strip()
                    add_or_update_track(
                        currentCup, scraped_track, position_count)

                    handle_position_count()
                elif tds[0]['rowspan'] == '2':  # Hidden Cup row
                    currentCup = tds[0].contents[0].strip()
                    cup_image = 'Hidden_Tracks.png'
                    add_or_update_cup(currentCup, cup_image)
                    scraped_track = tds[1].a.contents[0].strip()
                    add_or_update_track(
                        currentCup, scraped_track, position_count)

                    handle_position_count()
            else:
                scraped_track = tds[0].a.contents[0].strip()
                add_or_update_track(currentCup, scraped_track, position_count)

                handle_position_count()

    return


def wiiScraper():
    html = requests.get(url_wii).text
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find_all('table', class_='wikitable')
    # print(tables[4])


def index(request):
    context = {}
    return render(request, 'scraper/index.html', context)


def ctgp(request):
    ctgpScraper()
    return redirect('/ctgp')


def characters(request):
    # For adding characters
    character_file = open("data/characterData.json", 'r')
    character_json = json.loads(character_file.read())
    add_characters_to_db(character_json)
    return redirect('/characters')


def vehicles(request):
    # For adding vehicles
    vehicle_file = open("data/vehicleData.json", 'r')
    vehicle_json = json.loads(vehicle_file.read())
    add_vehicles_to_db(vehicle_json)
    return redirect('/vehicles')


def gameModes(request):
    mode_file = open("data/gameModeData.json", 'r')
    mode_json = json.loads(mode_file.read())
    for mode in mode_json:
        newMode, created = GameMode.objects.get_or_create(label=mode['label'])
    return redirect('/game-modes')


def engineClasses(request):
    engine_file = open("data/engineClassData.json", 'r')
    engine_json = json.loads(engine_file.read())
    for engine in engine_json:
        new_engine_class, created = EngineClass.objects.get_or_create(
            label=engine['label'])
    return redirect('/engine-classes')


def wii(request):
    WiiCup.objects.all().delete()
    WiiTrack.objects.all().delete()

    trackIndex = 0
    wii_track_file = open("data/wiiTrackData.json", 'r')
    wii_cup_file = open("data/wiiCupData.json", 'r')
    wii_track_json = json.loads(wii_track_file.read())
    wii_cup_json = json.loads(wii_cup_file.read())
    sortIndex = 0
    for track in wii_track_json:
        track, created = WiiTrack.objects.get_or_create(label=track['label'])
        track.order = sortIndex + 1
        track.save()
        sortIndex += 1
    tracks = WiiTrack.objects.all()
    print(tracks)
    for wiicup in wii_cup_json:
        newCup, created = WiiCup.objects.get_or_create(label=wiicup['label'])
        newCup.image = wiicup['image']
        newCup.save()
        for track in tracks:
            newCup.tracks.add(tracks[trackIndex])
            if (trackIndex + 1) % 4 == 0:
                trackIndex += 1
                break
            else:
                trackIndex += 1

    return redirect('/wii')
