cloud_cover= int(input("Enter cloud cover(%):"))
moon_brightness= int(input("Enter moon brightness(%):"))
score=100-cloud_cover-(moon_brightness*0.3)
print("Observation socre:",score)
if score>80:
    print("Exellent Observation Night")
elif score>50:
    print("Average Observation Night")
else:
    print("Poor Observation Night") 

if cloud_cover>70:
    print("High cloud cover may block celestial objects.")
if moon_brightness>80:
    print("Bright moonlight may reduce visibility of faint objects")
if cloud_cover<20:
    print("Sky conditions are very clear")
if cloud_cover<20 and moon_brightness<40:
    print("Recommended Target: Deep-Sky Objects")
elif cloud_cover<30:
    print("Recommended Target: Planets and the Moon")
else:
    print("Recommended Target: Casual Observation")
