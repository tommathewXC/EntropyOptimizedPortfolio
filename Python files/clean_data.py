import os;
import csv;


class GoogleFinance(object):
    CLOSE = float();
    HIGH  = float();
    OPEN  = float();
    LOW   = float();
    AVG_P = float();
    DATE  = str();
    VOL   = long();
    KEYS  = ['Volume', 'High', 'Low', '\xef\xbb\xbfDate', 'Close', 'Open'];
    def __init__(self, _date, _close, _high, _low, _open, _vol):
        self.CLOSE = _close;
        self.HIGH = _high;
        self.OPEN = _open;
        self.LOW  = _low;
        self.VOL  = _vol;
        self.DATE = _date;
        try:
            den = 0;
            try:
                self.CLOSE = float(_close);
                den = den + 1;
            except:
                self.CLOSE = float(0);
            try:
                self.HIGH = float(_high);
                den = den + 1;
            except:
                self.HIGH = float(0);
            try:
                self.OPEN = float(_open);
                den = den + 1;
            except:
                self.OPEN = float(0);
            try:
                self.LOW = float(_low);
                den = den + 1;
            except:
                self.LOW = float(0);
            
            if (den == 0):
                den = 1;
            self.AVG_P = round((float(1) / float(den)) * (self.CLOSE + self.HIGH + self.LOW + self.OPEN ) ,2);
        except:
            self.AVG_P = 0;
    def printRow(self, DICT):
        try:
            for i in range(0,len(self.KEYS)):
                print self.KEYS[ i] +": "+ DICT[self.KEYS[ i]];
        except:
            print "x";

class Stock():
    avg  = dict();
    vol  = dict();
    day = dict();
    month = dict();
    year = dict();
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];
    def add(self,date, av, v, b = False):
        self.avg[date] = av;
        self.vol[date] = v;
        self.day[date] = self.getDay(date);
        self.month[date] = self.getMonth(date);
        self.year[date] = self.getYear(date);
        if b:
            print str(av) + ": " + str(v);
            
    def getDay(self, _date):
        return int(_date.split('-')[0]);
    def getMonth(self, _date):
        return self.months.index(_date.split('-')[1].lower()) + 1;
    def getYear(self, _date):
        return int(_date.split('-')[2]);

def CleanData(setting):
    f =  r"project folder";
    final_Dir = f +"\\"+setting;
    files_in_dir =  os.listdir(final_Dir);
    print files_in_dir
    V = object();
    X = Stock();    
    ls = []    
    for a in range(0, len(files_in_dir)):
        dataformat = (("_TABLE_" in files_in_dir[a]) or ("_PDF_" in files_in_dir[a]) or ( ".txt" in files_in_dir[a])or ( "portfolio.csv" in files_in_dir[a]) or ( "averageprice.csv" in files_in_dir[a]));
        if not dataformat:
            fn = final_Dir + "\\"+files_in_dir[a];
            print "fn______________" + fn;
            with open(fn, 'r') as cfile:
                sreader = csv.DictReader(cfile);
                for row in sreader:
                    V = row;
                    G = GoogleFinance(V['Date'], V['Close'],V['High'],V['Low'],V['Open'],V['Volume']);
                    X.add(G.DATE, G.AVG_P, G.VOL);
        #    
            on = final_Dir + "\\" + setting +"_TABLE_" +files_in_dir[a];
            
            with open(on, 'wb') as c:
                w = csv.writer(c);
                w.writerow(["Date","Day", "Month", "Year","Average", "Volume"])
                for S in X.avg.keys():
                    w.writerow([S,X.day[S], X.month[S],X.year[S], X.avg[S], X.vol[S]]) ;
        ls.append( on );
#        print "on______________" + on;
    return ls;


def generateTableList(fn = "trainingfolder"):
    _files = os.listdir(fn);
    tables = [];
    for i in range(0, len(_files)):
        s = _files[i];
        if "TABLE" in s and "PDF" not in s:
            tables.append(s);
    f = fn + "tables.txt";
    U = open(f, "w");
    for j in range(0, len(tables)):
        U.write(tables[j]+"\n");
    U.close();
    return fn;
    
def CLEAN(fn, settin = 'training'):
    CleanData(settin)
    generateTableList(fn);
    print "__________________Data Cleaning complete_______________________";


f = "testing folder";
CLEAN(f, 'testing');