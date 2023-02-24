from time import sleep
import pandas as pd

import Logger as logg
from POM import Locators as loc


class ItemVideo:
    def __init__(self, webPage, webElem):
        self.name = ''
        self.url = ''
        self.webElement = webElem
        self.page = webPage


class MainPage:
    def __init__(self, webPage):
        self.page = webPage
        self.driver = self.page.driver
        self.followers = []
        self.following = []
        self.infidels = []

        sleep(1)

    def getListOfFollowers(self):
        self.page.driver.get(loc.urls.get('followers'))

        folowersWebElem = self.page.getPageElements_tryHard(loc.userPage_XPath.get('userName'))
        folowers = [i.accessible_name for i in folowersWebElem]
        if folowers:
            self.followers = folowers
            logg.logSmth("\n\n*** FOLLOWERS ***")
            for user in self.followers:
                logg.logSmth(user)

    def getListOfFollowing(self):
        self.page.driver.get(loc.urls.get('following'))

        folowingWebElem = self.page.getPageElements_tryHard(loc.userPage_XPath.get('userName'))
        folowing = [i.accessible_name for i in folowingWebElem]
        if folowing:
            self.following = folowing
            logg.logSmth("\n\n*** FOLLOWERS ***")
            for user in self.following:
                logg.logSmth(user)

    def printInfidelsToCSV(self):
        self.infidels = 0

        # file = self.getFileFromFilename(filename)
        # frame.to_csv(file['filepath'], index=False, encoding='utf-8')

    def getListOfInfidels(self):
        self.getListOfFollowers()
        self.getListOfFollowing()

        if len(self.following) > 0 and len(self.followers) > 0:
            self.infidels = [x for x in self.following if x not in self.followers]
            if self.infidels:
                print(self.infidels)
                logg.logSmth(self.infidels)
                logg.logSmth("\n***\n\n*** Infidels ***")
                for user in self.infidels:
                    logg.logSmth(user)

            logg.logSmth(
                f"***************************\n***************************\n Followers: {len(self.followers)} \n Following: {len(self.following)} \n Infidels: {len(self.infidels)}")
