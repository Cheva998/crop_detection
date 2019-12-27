import requests
from gmaps_settings import Settings

class GoogleMapImage(object):

    def __init__(self, lat, lon, img_name, folder, settings):
        self.lat = lat
        self.lon = lon
        self.img_name = img_name
        self.settings = settings
        self.url = ''
        self.folder = folder

    def make_image_url(self):
        self.url += self.settings.maps_url
        self.url += 'center=' + f'"{self.lat},{self.lon}"'
        self.url += '&zoom=' + f'{self.settings.zoom}'
        self.url += "&size=" + f'{self.settings.size}'
        self.url += "&scale=" + f'{self.settings.scale}'
        self.url += "&key=" + f'{self.settings.api_key}'
        self.url += "&sensor=true"
        self.url += "&style=feature:all|element:labels|visibility:off"
        self.url += "&maptype=satellite"

    def save(self):
        r = requests.get(self.url)
        with open(f'{self.folder}/{self.img_name}.png', 'wb') as f:
            f.write(r.content)

# settings = Settings()
# gmap_img = GoogleMapImage(70, 0.5, 'imagen.png', 'carpeta', settings)
# gmap_img.make_image_url()
# gmap_img.save()