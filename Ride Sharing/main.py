from ride import *
from vehicle import *
from users import *

niye_jao = RideSharing("Hanif")
rahim = Rider("Rahim", "rahim@gmail.com", 12234, "Mohakali", 12000)
kahim = Driver("Kahim", "kahim@gmail.com", 1223, "New Market")
niye_jao.add_rider(rahim)
niye_jao.add_driver(kahim)
rahim.request_ride(niye_jao, 'Uttara', 'car')
kahim.reach_destination(rahim.current_ride)
rahim.show_current_ride()
print(niye_jao)

