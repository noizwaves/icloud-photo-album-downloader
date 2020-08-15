from pyicloud import PyiCloudService
from tzlocal import get_localzone
import json
import os
import sys

SMART_FOLDERS = ['All Photos', 'Time-lapse', 'Videos', 'Slo-mo', 'Bursts', 'Favorites', 'Panoramas', 'Screenshots', 'Live', 'Recently Deleted', 'Hidden']

print(f'Downloading albums for {sys.argv[1]}')
api = PyiCloudService(sys.argv[1])

def photo_to_path(photo):
    date = photo.asset_date.astimezone(get_localzone())
    path = f'{str(date.year)}/{str(date.month).zfill(2)}/{str(date.day).zfill(2)}/{photo.filename}'
    return path

for name, album in api.photos.albums.items():
    if name in SMART_FOLDERS:
        continue

    print(f'Downloading "{name}"')

    name = album.title
    photos = list(map(photo_to_path, album.photos))

    path = '/'.join(['albums'] + album.lineage + [album.name + '.json'])
    dir = '/'.join(['albums'] + album.lineage)
    os.makedirs(dir, exist_ok=True)

    f = open(path, 'w')
    json.dump({'name': name, 'photos': photos}, f, indent=2)
    f.close()
