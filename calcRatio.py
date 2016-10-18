#!/usr/bin/env python

import requests
import json

class StockRatio:
	def __init__( self ):
		self.numerator = ''
		self.denominator = ''

	def setNumerator( self, value ):
		self.numerator = value
		print self.numerator
	def setDenominator( self, value ):
		self.denominator = value
		print self.denominator

	def getRatio( self ):
		if len( self.numerator ) > 0:
			print self.numerator
		else:
			print "no good!"
			return
		if len( self.denominator ) > 0:
			print self.denominator
		else:
			print "denom no good!"
			return

		lastNumer = requests.get( "http://localhost:32768/quote/" + self.numerator + "/last")
		lastDenom = requests.get( "http://localhost:32768/quote/" + self.denominator + "/last" )
		ratio = float( json.loads(lastNumer.text)['last price'] )/float( json.loads(lastDenom.text)['last price'] )
		return '{:06.4f}'.format( ratio )	
			
	



"""
@app.route("/", methods=['GET'])
def hello():
	return nice_json({
		"uri": "/",
		"subresource_uris": {
			"quote": "/quote/<TICKER>",
			"last price": "/quote/<TICKER>/last"
		}
	})

@app.route("/quote/<ticker>", methods=['GET'])
def get_quote( ticker ):
	try:
		jsonObj =  get_raw_quote( ticker )
		return nice_json( jsonObj )
	except NotFound:
		raise NotFound
	

@app.route("/quote/<ticker>/last", methods=['GET'])
def get_last_price( ticker ):
	try:
		jsonObj = get_raw_quote( ticker )
		lastValue = jsonObj[0]['l']
		return nice_json( {
			"last price": lastValue,
			}
		)
	except NotFound:
		raise NotFound

def get_raw_quote( ticker ):
        quoteUrl = "http://finance.google.com/finance/info?client=ig&q=" + ticker
        response = requests.get( quoteUrl )
        if response.status_code == 200:
                quote = response.text.split("//")
                return json.loads( quote[1] )
	else:
		raise NotFound


def nice_json(arg):
	response = make_response(json.dumps( arg, sort_keys = True, indent=4 ))
	response.headers['Content-type'] = "application/json"
	return response

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001, debug=True)

"""
