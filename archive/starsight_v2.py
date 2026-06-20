def calcutlate_score(cloud_cover,moon_brightness):
    score=100-cloud_cover - (moon_brightness*0.3)
    return score
cloud_cover= int(input("Enter cloud cover(%):"))
moon_brightness=int(input("Enter moon brightness(%):"))
score= calcutlate_score(cloud_cover, moon_brightness)
print("Observation Score:", score)
def classify_night(score):
    if score>80:
        print("Excellent Observation Night")
    elif score>50:
        print("Average Observation Night")
    else:
        print("Poor Observation Night")
classify_night(score)
def recommend_target(cloud_cover, moon_brightness):
    if cloud_cover<20 and moon_brightness<40:
        print("Recommended Target: Deep-Sky Objects")
    elif cloud_cover<30:
        print("Recommended Target: Planets and the Moon")
    else:
        print("Recommended Target: Casual Obseravtion")
recommend_target(cloud_cover, moon_brightness)
