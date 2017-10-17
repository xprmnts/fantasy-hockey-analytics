# Open html file
import codecs
from bs4 import BeautifulSoup
import lxml.html
import csv

with open("sched.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

dates = soup.find_all(class_='section-subheader')

for date in dates:
  with open("sched_dates.csv", 'a') as outfile:
    writer = csv.writer(outfile)
    row=[]
    row.append(date.contents[0].split(',')[1])
    writer.writerow(row)


# d = soup.find_all(class_='day-table-horiz-scrollable-wrapper')
# with open("sched_teams.csv", 'a') as outfile:
#     for rec in d:
#       row=[]
#       for team in rec.contents[1].find_all(class_="icon-label"):
#         if team.contents[0] != 'Watch' and team.contents[0] != 'GAMECENTER' and team.contents[0] != 'Preview' and team.contents[0] != 'Buy/Sell' and team.contents[0] != 'Tickets':
#           row.append(team.contents[0])
#       print(row)
#       writer = csv.writer(outfile)
#       writer.writerow(row)

# print(s.find_all(class_="icon-label"))




