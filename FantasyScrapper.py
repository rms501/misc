import requests
from bs4 import BeautifulSoup
import csv

class fantasyScrapper(object):

	players = []
	teams = []
	writer = None

	def getPlayers(self, url):
		response = requests.get(url)

		soup = BeautifulSoup(response.content, 'html.parser')

		tags = soup.find_all('div', 'ysf-player-name Nowrap Grid-u Relative Lh-xs Ta-start')
		
		response.close()

		self.players = [[i.a.get_text().strip(), [teamPositionList.strip() for teamPositionList in i.span.get_text().split('-')]] for i in tags]

		return self.players

	def getTeams(self, url):
		response = requests.get(url)

		soup = BeautifulSoup(response.content, 'html.parser')

		table = soup.find_all('table', id='standingstable')

		response.close()

		self.teams = []

		for i in table:
			for j in i.find_all('tr'):
				teamData = None
				nName = j.find('a', 'Grid-u F-reset Ell Mawpx-250')
				nRecord = j.find('td', 'Nowrap Ta-c Px-sm Tst-wlt')
				if 'get_text' in dir(nName) and 'get_text' in dir(nRecord):
					teamData = [nName.get_text(), nName['href'].split('/')[3], nRecord.get_text()]
				if teamData:
					self.teams.append(teamData)

		return self.teams

	def dumpTeams(self, file):
		writer = csv.writer(file)

		for i in self.teams:
			writer.writerow(i)

	def dumpPlayers(self, file):
		writer = csv.writer(file)

		dumpSet = []
		for i in self.players:
			dumpRecord = []
			for j in i:
				if not isinstance(j, list):
					dumpRecord.append(j)
				else:
					for k in j:
						dumpRecord.append(k)
			dumpSet.append(dumpRecord)

		for i in dumpSet:
			writer.writerow(i)		