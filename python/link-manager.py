import re
import types

linkManagerFeed = open('./link-manager-src/link-manager-feed.txt')
linkList = linkManagerFeed.readlines()
count = 0
finalFile = open('finalFile.txt', 'w')
for line in linkList:
  count = count + 1
  p = re.compile('.*? -')
  linkTitle = p.search(line)
  if linkTitle:
    title = linkTitle.group(0)[:-2]
    q = re.compile('https://.*')
    linkUrl = q.search(line)
    if linkUrl:
      aTag = '<a href="' + linkUrl.group(0) + '">' + title + '</a>\n'
      print aTag
      finalFile.write(aTag)