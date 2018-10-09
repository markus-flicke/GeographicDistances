import pandas as pd
import numpy as np

class Geo:
    """
    Geographic distances using: https://developers.google.com/public-data/docs/canonical/countries_csv
    """
    max_separation = 19955379

    def __init__(self):
        self.df = pd.read_msgpack('geography')

    def dist(self, country_code_a, country_code_b):
        lat1 = self.df.loc[country_code_a].latitude
        lon1 = self.df.loc[country_code_a].longitude
        lat2 = self.df.loc[country_code_b].latitude
        lon2 = self.df.loc[country_code_b].longitude

        r = 6371000 #metres
        phi1 = lat1 * np.pi / 180
        phi2 = lat2 * np.pi / 180
        dphi = (lat2 - lat1) * np.pi / 180
        dlambda = (lon2 - lon1) * np.pi / 180
        a = np.sin(dphi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * (np.sin(dlambda / 2) ** 2)
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        d = r * c
        try:
            return int(d)
        except:
            print(country_code_b)
            raise

    def norm_dist(self, country_code_a, country_code_b):
        return self.dist(country_code_a, country_code_b) / self.max_separation

if __name__ == '__main__':
    g = Geo()
    print(g.norm_dist('US','DE'))
