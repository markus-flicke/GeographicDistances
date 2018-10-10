import pandas as pd
import numpy as np
import random


class Point:
    """
    Geographic distances using: https://developers.google.com/public-data/docs/canonical/countries_csv
    """
    max_separation = 19955379

    def __init__(self, country_code = None, lon = None, lat = None, randomise = False):
        if country_code:
            self.country_code = country_code
            self.lon = geo_df.longitude[country_code]
            self.lat = geo_df.latitude[country_code]
        else:
            self.country_code = None
            self.lon = lon
            self.lat = lat
        if randomise:
            self.lon = random.randint(-180,180)
            self.lat = random.randint(-90, 90)

    def dist(self, other):
        lat1 = self.lat
        lon1 = self.lon
        lat2 = other.lat
        lon2 = other.lon

        r = 6371000 #metres mean earth radius
        phi1 = lat1 * np.pi / 180
        phi2 = lat2 * np.pi / 180
        dphi = (lat2 - lat1) * np.pi / 180
        dlambda = (lon2 - lon1) * np.pi / 180
        a = np.sin(dphi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * (np.sin(dlambda / 2) ** 2)
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        d = r * c
        return d

    def norm_dist(self, other):
        return self.dist(other) / self.max_separation

    def __repr__(self):
        return "{}({},{})".format(self.country_code, self.lon, self.lat)

if __name__ == '__main__':
    geo_df = pd.read_msgpack('geography')
    germany = Point('DE')
    uk = Point('GB')
    print(Point(randomise=True))
else:
    geo_df = pd.read_msgpack('GeographicDistances/geography')