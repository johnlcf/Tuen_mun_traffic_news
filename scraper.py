#!/usr/bin/python
# vim: set fileencoding=utf-8 :

# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import feedparser
import re
import smtplib

from email.mime.text import MIMEText

def send_email(content):

    msg = MIMEText(content, "plain", "utf-8")
    me = 'johnlcf.forward@gmail.com'
    you = 'johnlcf@gmail.com'
    msg['Subject'] = 'Tuen mun traffic news'
    msg['From'] = me
    msg['To'] = you

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("johnlcf.forward@gmail.com", "Good2ForwardDay")
    s.sendmail(me, [you], msg.as_string())
    s.quit()

p = re.compile(u'.*赤柱.*')

d = feedparser.parse('http://www.td.gov.hk/tc/special_news/spnews_rss.xml')
for post in d.entries:
    print post.title + ": " + post.link + "\n"
    if p.match(post.title):
        print "*** send email ***"
        send_email(post.title)
        
    
