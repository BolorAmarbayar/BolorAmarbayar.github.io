from bike import Bike
from road import Road

bike_a = Bike(1,2, 39)
bike_b = Bike(11,11,80)
bike_c = Bike(9,10,45)

road = Road("paved", 3)

if road.terrain_type == "paved" and road_obstacles < 4:
    if bike_a.speed > bike_b.speed and bike_a.speed > bike_c.speed:
        bike_a.add_points(5)
        if bike_a.size > bike_b.size and bike_a.size > bike_c.size:
            bike_a.add_points(3)
    if bike_b.speed > bike_a.speed and bike_b.speed > bike_c.speed:
        bike_b.add_points(5)  
        if bike_b.size > bike_c.size and bike_b.size > bike_c.size:
            bike_b.add_points(3)        
    if bike_c.speed > bike_a.speed and bike_c.speed > bike_b.speed:
        bike_c.add_points(5)  
        if bike_c.size > bike_b.size and bike_c.size > bike_a.size:
            bike_c.add_points(3)    
            
print(bike_a.score)
print(bike_b.score)
print(bike_c.score)