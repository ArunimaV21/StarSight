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

def get_percentage(promt):
    while True:
        try:
            value=int(input(promt))
            if 0<=value<=100:
                return value
            else: 
                print("Invalid Input")
                print("Please enter a value between 0 and 100") 
        except ValueError:
            print("Invalid Input")
            print("Please enter a number, not text")
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
        print("Recommended Target: Casual Observation")

while True:
    night=(len(dates)+1)
    print("Night", night)
    date=input("Enter Date(DD-MM-YYYY):")
    cloud_cover=get_percentage("Enter cloud cover(%):")
    moon_brightness=get_percentage("Enter moon brightness(%):")
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
def display_statistics(data):
    excellent=0
    average=0
    poor=0
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
    for score in data["Score"]:
        if score>80:
            excellent=excellent+1
        elif score>50:
            average=average+1
        else:
            poor=poor+1
    print("Excellent Nights:", excellent)
    print("Average Nights:", average)
    print("Poor Nights:", poor)
    excellent_percent = (excellent / len(data)) * 100
    average_percent = (average / len(data)) * 100
    poor_percent = (poor / len(data)) * 100
    print()
    print("Observation Quality Breakdown")
    print("Excellent:",round(excellent_percent, 1),"%")
    print("Average:",round(average_percent, 1),"%")
    print("Poor:",round(poor_percent, 1),"%")
    if excellent > average and excellent > poor:
        print("Most Common Observation Quality: Excellent")
    elif average > excellent and average > poor:
        print("Most Common Observation Quality: Average")
    else:
        print("Most Common Observation Quality: Poor")
    best_environment = data.loc[data["Score"].idxmax()]
    print()
    print("Best Environmental Conditions:")
    print("Night:", best_environment["Night"])
    print("Date:", best_environment["Date"])
    print("Cloud Cover:", best_environment["CloudCover"], "%")
    print("Moon Brightness:", best_environment["MoonBrightness"], "%")
    print("Score:", best_environment["Score"])

display_statistics(data)

def create_line_graph(data, y_data, y_label, title, filename):
    plt.figure()
    plt.plot( data["Night"], y_data, marker="o")
    plt.xlabel("Observation Nights")
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)

create_line_graph(data, data["Score"], "Observation Score", "StarSight Observation Scores", "ObsScore_LG.png")
create_line_graph(data, data["CloudCover"], "Cloud Cover (%)", "Cloud Cover Graph", "CldCver_LG.png")
create_line_graph(data, data["MoonBrightness"], "Moon Brightness (%)", "Moon Brightness Graph", "MnBrght_LG.png")

def create_comparison_graph(data):
    plt.figure()
    plt.plot(data["Night"], data["Score"], marker="o",label="Score")

    plt.plot(data["Night"],data["CloudCover"], marker="o",label="Cloud Cover")

    plt.plot(data["Night"], data["MoonBrightness"], marker="o", label="Moon Brightness")
    plt.xlabel("Observation Nights")
    plt.ylabel("Value")
    plt.title("StarSight Enviornmental Factors v/s Observation Score")
    plt.legend()
    plt.grid(True)
    plt.savefig("EnvFctr_LG.png")

create_comparison_graph(data)

def create_bar_graph(data, y_data, y_label, title, filename):
    plt.figure()
    plt.bar( data["Night"], y_data)
    plt.xlabel("Observation Nights")
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)

create_bar_graph(data, data["Score"],"Observation Score","StarSight Observation Scores", "ObsScore_BG.png")
def create_histogram(x_data, x_label, title, filename):
    plt.figure()
    plt.hist( x_data)
    plt.xlabel(x_label)
    plt.ylabel("Frequency")
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)

create_histogram(data["Score"],"Score",  "Observation Score Distribution", "ObsScore_HIST.png" )
plt.show()
