import pandas as pd
import matplotlib.pyplot as plt 
try:
    old_data= pd.read_csv("starsight_observations.csv")
    nights=old_data["Night"].to_list()
    dates= old_data["Date"].to_list()
    clouds=old_data["CloudCover"].to_list()
    moons=old_data["MoonBrightness"].to_list()
    scores=old_data["Score"].to_list()
    print("Previous Observations:")
    print(old_data.to_string(index=False))
    print()
except FileNotFoundError:
    nights=[]
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

while True:
    night=(len(dates)+1)
    print("Night", night)
    date=input("Enter Date(DD-MM-YYYY):")
    cloud_cover=int(input("Enter cloud cover(%):"))
    moon_brightness=int(input("Enter moon brightness(%):"))
    score=calculate_score(cloud_cover,moon_brightness)
    scores.append(score)
    dates.append(date)
    clouds.append(cloud_cover)
    moons.append(moon_brightness)
    nights.append(night)
    print("Observation score:",score)
    classify_night(score)
    recommend_target(cloud_cover,moon_brightness)
    print()
    answer=input("Stop?(y/n):")
    if answer=="y":
        break
    
    
data = pd.DataFrame({
"Night":nights,
"Date": dates,
"CloudCover": clouds,
"MoonBrightness": moons,
"Score": scores
})
data.to_csv("starsight_observations.csv", index=False)
print()
print("===StarSight Statistics===")
print()
print("Total Nights observed:", len(data))
best_night=data.loc[data["Score"].idxmax()]
print("Best Observation Night: Night", best_night["Night"])
print("Date:", best_night["Date"])
print("Score:", best_night["Score"])
worst_night = data.loc[data["Score"].idxmin()]
print()
print("Worst Observation Night: Night", worst_night["Night"])
print("Date:", worst_night["Date"])
print("Score:", worst_night["Score"])
print()
cloudiest_night = data.loc[data["CloudCover"].idxmax()]
print("Cloudiest Night: Night", cloudiest_night["Night"])
print("Cloud Cover:", cloudiest_night["CloudCover"])
print()
brightest_moon = data.loc[data["MoonBrightness"].idxmax()]
print("Brightest Moon Night: Night", brightest_moon["Night"])
print("Moon Brightness:", brightest_moon["MoonBrightness"])
print()
average_score = data["Score"].mean()
print("Average Observation Score:", round(average_score, 2))

excellent=0
average=0
poor=0
for score in data["Score"]:
    if score>80:
        excellent=excellent+1
    elif score>50:
        average=average+1
    else:
        poor=poor+1

print()
print("Excellent Nights:", excellent)
print("Average Nights:", average)
print("Poor Nights:", poor)


plt.figure()
plt.plot(data["Night"], data["Score"], marker="o")
plt.xlabel("Observation Nights")
plt.ylabel("Observation Score")
plt.title("StarSight Observation Scores")
plt.grid(True)
plt.savefig("ObsScore_LineGraph.png")

plt.figure()
plt.bar(data["Night"], data["Score"])
plt.xlabel("Observation Nights")
plt.ylabel("Observation Score")
plt.title("StarSight Observation Scores")
plt.grid(True)
plt.savefig("Score_BarGraph.png")

plt.figure()
plt.hist(data["Score"])
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Observation Score Distribution")
plt.grid(True)
plt.savefig("ObsScore_Histogram.png")

plt.figure()
plt.plot(data["Night"], data["CloudCover"], marker="o")
plt.xlabel("Observation Nights")
plt.ylabel("Cloud Cover(%)")
plt.title("Cloud Cover at Night")
plt.grid(True)
plt.savefig("CldCver_graph.png")

plt.figure()
plt.plot(data["Night"], data["MoonBrightness"], marker="o")
plt.xlabel("Observation Nights")
plt.ylabel("Moon Brightness(%)")
plt.title("Moon Brightness at Night")
plt.grid(True)
plt.savefig("MnBrght_graph.png")

plt.figure()
plt.plot(data["Night"], data["Score"], marker="o", label="Score")
plt.plot(data["Night"], data["CloudCover"], marker="o", label="CloudCover")
plt.plot(data["Night"], data["MoonBrightness"], marker="o", label="MoonBrightness")
plt.xlabel("Observation Nights")
plt.ylabel("All Data")
plt.title("StarSight Enviornmental Factors v/s Observation Score")
plt.grid(True)
plt.savefig("EnvFctr_grah.png")
plt.show()
