from flask import Flask, render_template, url_for, request, abort
import json

dojolist   = []
supporters = []
topbar = []
hashtaglist = []

app = Flask(__name__)

class TopBarLink(object):
	def __init__(self, page, title):
		self.page = "/" + page
		self.title = title

class Supporter(object):
	def __init__(self, img, alt, link, job, hashtag):
		self.img  = img
		self.alt  = alt
		self.link = link
		self.job  = job
		self.hashtag = hashtag
		hashtaglist.append(hashtag)

class Dojo(object):
	def __init__(self, loc, com, time, day, zen, cap, started, group, git, twitter, e):
		self.location    = loc
		self.company     = com
		self.time        = time
		self.days        = day
		self.zenid       = zen
		self.cap   	     = cap
		self.start       = started
		self.googlegroup = group
		self.git         = git
		self.acronym     = "UNUSED_DATA" #= splitted[0][0] + splitted[1][0]
		self.twitter = twitter
		self.email = e

facebook="""
<p class="aligncenter comicsans">Wouldn\'t it be great if we had a Facebook page?</p>
<p class="aligncenter"><img src="/static/sadyinyanglogo.png"/></p>
<p class="aligncenter comicsans">Come and help us make one!</p>
<p class="aligncenter"><a href="mailto:siliconvalley@coderdojo.com">Contact Us</a></p>
"""		

@app.route("/")
def index():
	return render_template("index.html", news="CoderDojo Silicon Valley is starting up a San Jose dojo at the IIC.", topbar=topbar, sups=supporters[1:len(supporters)], supone=supporters[0], hashlist=str(hashtaglist), facebook=facebook)
	
@app.route("/dojos")
@app.route("/dojos/")
def dojos():
	return render_template("dojos.html", dojos=dojolist, topbar=topbar)
	
#@app.route("/attend")
#def attend():
#	return render_template("attend.html", dojo=request.args.get("dojo"), zen=request.args.get("zen"), topbar=topbar)
	
@app.route("/get_involved")
@app.route("/get_involved/")
def get_involved():
	return render_template("signup.html", topbar=topbar, dojos=dojolist)
	
@app.route("/sponsors")
@app.route("/sponsors/")
def supporterspage():
	return render_template("sup.html", sups=supporters, topbar=topbar)
	
@app.route("/faqs")
@app.route("/faqs/")
def faqs():
	return render_template("faqs.html", topbar=topbar)
	
#@app.route("/subscribe")
#def mail_chimp():
#	return render_template("mailchimp.html", topbar=topbar)

@app.route("/get_involved/signup")
@app.route("/get_involved/signup/")
def mentor_monkey():
	return render_template("msignup.html", topbar=topbar)
	
@app.route("/test/jquery/windows")
def windows():
	return render_template("windows.html")
	
@app.route("/ajax/supporters")	
@app.route("/ajax/supporters/")
def get_hashlist():
	return json.dumps(hashtaglist)

	
@app.route("/check")
def htmlfive():
	return """
	<style>
	.pee:last-child {
		display: block;
		position: absolute;
		left: 0;
		top: 0;
		z-index: 10;
	}
	.pee {
		display: none;
		background-color: green;
		color: white;
	}
	#poo {
		background-color: red;
		color: white;
		position: absolute;
		left: 0;
		top: 0;
	}
	</style>
	<p class='pee'>HTML5 browser?</p>
	<p id='poo'>You are using an outdated browser.</p>
	<p class='pee'>You are using an HTML5 browser.</p>
	"""

@app.route("/dojos/<name>")	
@app.route("/dojos/<name>/")
def dojo(name):
	try:
		thedojo = None
		for i in dojolist:
			if i.location == name:
				thedojo = i
		if thedojo is None:
			abort(500)
		else:
			try:
				render_template("hero." + name + ".html", dojo=thedojo, topbar=topbar)
				hasheroes = "true"
			except:
				hasheroes = "false"
			return render_template("dojo." + name + ".html", dojo=thedojo, hasheroes=hasheroes, topbar=topbar)
	except:
		return render_template("cantfind.html", dojo=name, topbar=topbar)
		
@app.route("/dojos/<name>/heroes")
@app.route("/dojos/<name>/heroes/")
def heroes(name):
	try:
		thedojo = None
		for i in dojolist:
			if i.location == name:
				thedojo = i
		if thedojo is None:
			abort(500)
		else:
			return render_template("hero." + name + ".html", dojo=thedojo, topbar=topbar)
	except:
		dojostrings = []
		for i in dojolist:
			dojostrings.append(i.location)
		if name in dojostrings:
			return render_template("comingsoon.html", topbar=topbar, dojo=name)
		else:
			return render_template("cantfind.html", topbar=topbar, dojo=name)
		
@app.route("/bootstrap")
def btest():
	return render_template("bootstraptest.html")
	
@app.route("/about")
@app.route("/about/")
def about():
	return render_template("about.html", topbar=topbar)
	
@app.route("/press")
@app.route("/press/")
def press():
	return render_template("press.html", topbar=topbar)
	
@app.route("/resources")
@app.route("/resources/")
def resources():
	return render_template("resources.html", topbar=topbar, dojos=dojolist)

@app.route("/calendar")
@app.route("/calendar/")
def calendar():
	return render_template("cal.html", topbar=topbar)

dojolist.append(Dojo("San Francisco", "GitHub", "check here for details", "Times and dates vary", "http://zen.coderdojo.com/dojo/25", "40", "February 2012", "coderdojo-sanfran", "http://www.github.com/CoderDojoSF", "CoderDojoSF", "sanfran@coderdojo.com"))
dojolist[0].time = "<a target='_blank' href='" + dojolist[0].zenid + "'>" + dojolist[0].time + "</a>"

dojolist.append(Dojo("Mountain View", "Microsoft", "7:00-8:30 pm", "Third Wednesday of every month", "http://zen.coderdojo.com/dojo/159", "40", "August 2012", "siliconvalleycoderdojo", "disabled", "SVCoderDojo", "siliconvalley@coderdojo.com"))

dojolist.append(Dojo("Tri-Valley", "Dublin Library", "7:00-8:30 pm", "First Wednesday of every month", "http://zen.coderdojo.com/dojo/428", "40", "October 2013", "trivalleycoderdojo", "disabled", "TrivCoderDojo", "trivalleycoderdojo@gmail.com"))

dojolist.append(Dojo("San Jose", "The Irish Innovation Center", "TBD", "TBD", "http://zen.coderdojo.com/dojo/138", "25", "June 2013", "san-jose-coderdojo", "disabled", "SJCoderDojo", "siliconvalley@coderdojo.com"))

supporters.append(Supporter("/static/Microsoft-Logo.png", "Microsoft", "http://microsoft.com", "Provides space for Mountain View CoderDojo", "micro"))
supporters.append(Supporter("/static/boutmentors.png", "Breakout Mentors", "http://breakoutmentors.com", "Founder is lead technology champion of CoderDojo Mountain View", "bkm"))

supporters.append(Supporter("/static/dublinLogo.png", "The City of Dublin", "http://dublinca.gov", "Provides space for Tri-Valley CoderDojo at the Dublin Library", "dublin"))

supporters.append(Supporter("/static/GitHub-Logo.png", "GitHub", "http://github.com", "Provides space for San Fransisco CoderDojo", "gh"))
supporters.append(Supporter("/static/Symantec_logo.png", "Symantec", "http://symantec.com", "Provides refreshments for Mountain View CoderDojo", "syn"))
supporters.append(Supporter("/static/iic.png", "Irish Innovation Center", "http://svgpartners.com/", "Provides space for San Jose CoderDojo", "iic"))
supporters.append(Supporter("/static/mountainmikes.png", "Mountain Mike's Pizza", "http://mountainmikes.com", "Mountain View CoderDojo discount pizza offers", "mm"))
	
topbar.append(TopBarLink("", "Home"))
topbar.append(TopBarLink("dojos", "Dojos"))
topbar.append(TopBarLink("get_involved", "Get Involved"))
topbar.append(TopBarLink("sponsors", "Sponsors"))
topbar.append(TopBarLink("resources", "Resources"))
topbar.append(TopBarLink("badges", "Badges & Belts"))

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=3050)
