import pyshorteners
import urllib.request

link = input("Enter Link: ")

if "tinyurl" in link:
    orginal = urllib.request.urlopen(link)
    main_link = orginal.url
    print("This is the original link: {}".format(main_link))
else:
    shortener = pyshorteners.Shortener()
    x = shortener.tinyurl.short(link)
    print("This is the short link: {}".format(x))