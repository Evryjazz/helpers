from datetime import datetime, timedelta


def today():
	today = datetime.strftime(datetime.now(), '%Y-%m-%d')
	return today

def yesterday():
	yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
	return yesterday