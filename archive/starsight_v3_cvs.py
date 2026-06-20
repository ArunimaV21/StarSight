import pandas as pd
dates=[]
clouds=[]
moons=[]
scores=[]
def calculate_score(cloud_cover, moon_brightness):
    score=100-cloud_cover - (moon_brightness*0.3)
    return score
def classify_night(score):
    if score>80:
        print("Excellent Observation Night")
    elif score>50:
        print("Average Observation Night")
    else:
        print("Poor Observation Night")
def recommend_target(cloud_cover, moon_brightness):
    if cloud_cover<20 and moon_brightness<40:
        print("Recommended Target: Deep-Sky Objects")
    elif cloud_cover<30:
        print("Recommended Target: Planets and the Moon")
    else:
        print("Recommended Target: Casual Obseravtion")
scores=[]
for i in range(3):
    print("Night",i+1)
    date=input("Enter Date(DD-MM-YYYY):")
    cloud_cover=int(input("Enter cloud cover(%):"))
    moon_brightness=int(input("Enter moon brightness(%):"))
    score=calculate_score(cloud_cover,moon_brightness)
    scores.append(score)
    dates.append(date)
    clouds.append(cloud_cover)
    moons.append(moon_brightness)
    print("Observation score:",score)
    classify_night(score)
    recommend_target(cloud_cover,moon_brightness)
    print()
data = pd.DataFrame({
"Date": dates,
"CloudCover": clouds,
"MoonBrightness": moons,
"Score": scores
})

data.to_csv("starsight_observations.csv", index=False)
