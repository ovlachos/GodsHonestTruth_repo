from random import randint
from time import sleep

from POM import MainPage as mpage
from POM import webPage as wp


class InstaBot:
    datetimeStringFormat_day = '%Y_%m_%d'

    def __init__(self, headless=False):
        self.headless = headless
        self.timeUpperBound = 48
        self.timeLowerBound = 34
        self.timeLimitSinceLastLoved = 30
        self.followMana = 100
        self.followManaMax = 100
        self.getBrowser()

        # Game vars
        self.daysBeforeIunFollow = 14 - 1
        self.daysBeforeIunLove = self.daysBeforeIunFollow + 5

    def logIn(self):
        self.mainPage = mpage.MainPage(self.webPage)

    def shutDown(self):
        self.logOut()
        sleep(1)
        self.webPage.instance.writeSessionDataToJSON()
        self.webPage.killBrowser()

    def getBrowser(self):
        self.webPage = wp.WebPage(self.headless)

    def botSleep(self, factor=1):
        sleep(randint(factor * self.timeLowerBound, factor * self.timeUpperBound))

    def getTheInfidels(self):
        self.mainPage.getListOfInfidels()
