#! python3
# OSINT Scraper
# This python file will crawl the Baltimore City Government Web Portal
# To gather property values from the tax portal
# Jason Hammett
# Baltimore OSINT Criminal Analysis
# https://automatetheboringstuff.com/chapter11/

import requests
import bs4

portalUrl = "https://cityservices.baltimorecity.gov/RealProperty/default.aspx"
portalRes = requests.get(portalUrl)
portalRes.raise_for_status()