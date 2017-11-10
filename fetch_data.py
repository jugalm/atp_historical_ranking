import pandas as pd
from highcharts import Highchart
H = Highchart(width=750, height=600)

df = pd.read_html('http://www.atpworldtour.com/en/rankings/singles?rankDate=2017-09-25&rankRange=0-1000')

ranking_with_dob = df[0]

ranking_with_dob.columns = ranking_with_dob.columns.str.replace("\n\t\t\n\t\t\t\n\t\t\t\t", "")

ranking_with_dob.columns = ranking_with_dob.columns.str.replace("\n\t\t\t\n\t\t\t\n\t\t\n\t", "")

print ranking_with_dob.head(10)

print ranking_with_dob.head(1000)['Age'].mean()

