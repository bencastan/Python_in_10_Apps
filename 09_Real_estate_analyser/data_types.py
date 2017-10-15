
class Purchase:
    def __init__(
            self, street, city, zipcode, state, beds,
            baths, sq__ft, home_type, sale_date, price,
            lattitude, longtitude):
        self.longituse = longtitude
        self.latitude = lattitude
        self.price = price
        self.sale_data = sale_date
        self.type = home_type
        self.sq__ft = sq__ft
        self.baths = baths
        self.beds = beds
        self.state = state
        self.zip =zipcode
        self.city = city
        self.street = street


    @staticmethod
    def create_from_dict(lookup):
        return Purchase(
            lookup['city'],
            lookup['zip'],
            lookup['state'],
            int(lookup['beds']),
            int(lookup['baths']),
            int(lookup['sq__ft']),
            lookup['type'],
            lookup['sale_data'],
            float(lookup['price']),
            float(lookup['latitude']),
            float(lookup['logtitude'])
        )