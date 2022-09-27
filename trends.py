from pytrends.request import TrendReq
import pandas

pt = TrendReq(hl='en-US', tz=-400, backoff_factor = 0.1)

###################################################

def hourTrend(terms = ["one","two","three"], place = '', slp = 0, Ystart = 2020, Mstart = 1,Dstart = 1, Hstart = 0,
        Yend = 2020, Mend = 2, Dend = 1, Hend = 0):
    """
    Creates an hourly search trend with an arbitrary number of terms. default worldwide 2020-01-01 00:00 to 2020-02-01 00:00

    """
    terms = turn2d(terms)
    dfLis=[]
    
    for subset in terms:
        df = pt.get_historical_interest(subset, geo=place, sleep=slp, year_start=Ystart, month_start=Mstart, day_start=Dstart, hour_start=Hstart, year_end=Yend, month_end=Mend, day_end=Dend, hour_end=Hend)
        df.index.name = 'date'
        df.reset_index(inplace=True)
        df = df.drop("isPartial",axis="columns")
        dfLis.append(df)
    return dfLis
  
#########################################################

def interestOverTime(terms, place = '', Tstart = "2020-01-01", Tend = "2021-01-01"):
  """
  Creates a search trend. default worldwide 2020-01-01 to 2021-01-01
  """
  terms = turn2d(terms)
  dfLis=[]
  
  for subset in terms:
    pt.build_payload(subset, geo=place, timeframe=Tstart+" "+Tend)
    df = pt.interest_over_time()
    df.index.name = 'date'
    df.reset_index(inplace=True)
    df = df.drop("isPartial",axis="columns")
    dfLis.append(df)
  return dfLis
    
###################################################

def turn2d(terms):
    """
    Turns a str or str array into a 2d array for pytrends (can only accept in groups of <5)
    """
    if(type(terms) != list):
        return [[terms]]
    else:
        root = terms[0]
        lis = [[root]]
        lisI = 0
        for i in range(1, len(terms)):
            if(len(lis[lisI]) == 5):
                lisI += 1
                lis.append([root])
            lis[lisI].append(terms[i])
        return lis
