from math import pi as pi 
side_of_garden = float(input("Enter the length of side of the final garden: "))
space_btw_plants = float(input("Enter the spacing between the plants in the garden: "))
depth_of_flowerbed = float(input("Enter the depth of flower bed: "))
depth_of_fill= float(input("Enter the depth of the fill: "))

radius = side_of_garden / 4
area_of_garden = (side_of_garden ** 2)
area_of_semicircle = 0.5 * pi * (radius**2)
total_plants_under_semicircle = area_of_semicircle / space_btw_plants**2
total_plants_under_circle = total_plants_under_semicircle * 2
soil_for_semicircle_garden = (0.333**3) * depth_of_flowerbed * area_of_semicircle 
soil_for_circle_garden = 2 * soil_for_semicircle_garden
total_soil = soil_for_circle_garden + 4 * soil_for_semicircle_garden
area_under_fill =  area_of_garden - 6 * area_of_semicircle
total_fill = round(area_under_fill * depth_of_fill * (0.333 **3 ),1)

print("Total plants under each semicircle: ", round(total_plants_under_semicircle))
print("Total plants under each circle: ", round(total_plants_under_circle))
print("Total plants: ", round(6 * round(total_plants_under_semicircle)))
print("Total soil under semicricle: ", round(soil_for_semicircle_garden,1))
print("Total soil under circle: ", round(soil_for_circle_garden,1))
print("Total soil: ", round(total_soil,1))
print("Total fill: ", total_fill)