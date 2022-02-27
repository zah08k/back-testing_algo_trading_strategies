import pandas as pd

pd.options.mode.chained_assignment = None

class StartEnd:  # Starting and ending date for every contract
    def __init__(self, symbol):
        self.symbol = symbol

    def zw(self):
        x = self.symbol[-2:]
        y = None
        z = self.symbol[-2:]
        v = None

        if self.symbol[-3] == 'h':
            y = '11-16'
            v = '02-15'
            x = str(int('20' + x) - 1)[-2:]
        elif self.symbol[-3] == 'k':
            y = '02-16'
            v = '04-15'
        elif self.symbol[-3] == 'n':
            y = '04-16'
            v = '06-15'
        elif self.symbol[-3] == 'u':
            y = '06-16'
            v = '08-15'
        elif self.symbol[-3] == 'z':
            y = '08-16'
            v = '11-15'

        start = (lambda x, y: '20' + x + '-' + y)(x, y)
        end = (lambda z, v: '20' + z + '-' + v)(z, v)

        return start, end

    def zc(self):
        x = self.symbol[-2:]
        y = None
        z = self.symbol[-2:]
        v = None

        if self.symbol[-3] == 'h':
            y = '11-16'
            v = '02-15'
            x = str(int('20' + x) - 1)[-2:]
        elif self.symbol[-3] == 'k':
            y = '02-16'
            v = '04-15'
        elif self.symbol[-3] == 'n':
            y = '04-16'
            v = '06-15'
        elif self.symbol[-3] == 'u':
            y = '06-16'
            v = '08-15'
        elif self.symbol[-3] == 'z':
            y = '08-16'
            v = '11-15'

        start = (lambda x, y: '20' + x + '-' + y)(x, y)
        end = (lambda z, v: '20' + z + '-' + v)(z, v)

        return start, end

    def zs(self):
        x = self.symbol[-2:]
        y = None
        z = self.symbol[-2:]
        v = None

        if self.symbol[-3] == 'f':
            y = '10-16'
            v = '12-15'
            x = str(int('20' + x) - 1)[-2:]
        elif self.symbol[-3] == 'h':
            y = '12-16'
            v = '02-15'
            x = str(int('20' + x) - 1)[-2:]
        elif self.symbol[-3] == 'k':
            y = '02-16'
            v = '04-15'
        elif self.symbol[-3] == 'n':
            y = '04-16'
            v = '06-15'
        elif self.symbol[-3] == 'q':
            y = '06-16'
            v = '07-15'
        elif self.symbol[-3] == 'u':
            y = '07-16'
            v = '08-15'
        elif self.symbol[-3] == 'x':
            y = '08-16'
            v = '10-15'

        start = (lambda x, y: '20' + x + '-' + y)(x, y)
        end = (lambda z, v: '20' + z + '-' + v)(z, v)

        return start, end

    def ebm(self):
        x = self.symbol[-2:]
        y = None
        z = self.symbol[-2:]
        v = None

        if self.symbol[-3] == 'h':
            y = '11-16'
            v = '02-15'
            x = str(int('20' + x) - 1)[-2:]
        elif self.symbol[-3] == 'k':
            y = '02-16'
            v = '04-15'
        elif self.symbol[-3] == 'u':
            y = '04-16'
            v = '08-15'
        elif self.symbol[-3] == 'z':
            y = '08-16'
            v = '11-15'

        start = (lambda x, y: '20' + x + '-' + y)(x, y)
        end = (lambda z, v: '20' + z + '-' + v)(z, v)

        return start, end

    def cl(self):
        x = self.symbol[-2:]
        y = None
        z = self.symbol[-2:]
        v = None

        if self.symbol[-3] == 'f':
            y = '11-16'
            v = '12-15'
            x = str(int('20' + x) - 1)[-2:]
        elif self.symbol[-3] == 'g':
            y = '12-16'
            v = '01-15'
            x = str(int('20' + x) - 1)[-2:]
        elif self.symbol[-3] == 'h':
            y = '01-16'
            v = '02-15'
        elif self.symbol[-3] == 'j':
            y = '02-16'
            v = '03-15'
        elif self.symbol[-3] == 'k':
            y = '03-16'
            v = '04-15'
        elif self.symbol[-3] == 'm':
            y = '04-16'
            v = '05-15'
        elif self.symbol[-3] == 'n':
            y = '05-16'
            v = '06-15'
        elif self.symbol[-3] == 'q':
            y = '06-16'
            v = '07-15'
        elif self.symbol[-3] == 'u':
            y = '07-16'
            v = '08-15'
        elif self.symbol[-3] == 'v':
            y = '08-16'
            v = '09-15'
        elif self.symbol[-3] == 'x':
            y = '09-16'
            v = '10-15'
        elif self.symbol[-3] == 'z':
            y = '10-16'
            v = '11-15'

        start = (lambda x, y: '20' + x + '-' + y)(x, y)
        end = (lambda z, v: '20' + z + '-' + v)(z, v)

        return start, end

    def gc(self):
        x = self.symbol[-2:]
        y = None
        z = self.symbol[-2:]
        v = None

        if self.symbol[-3] == 'g':
            y = '11-26'
            v = '01-25'
            x = str(int('20' + x) - 1)[-2:]
        elif self.symbol[-3] == 'j':
            y = '01-26'
            v = '03-25'
        elif self.symbol[-3] == 'm':
            y = '03-26'
            v = '05-25'
        elif self.symbol[-3] == 'q':
            y = '05-26'
            v = '07-25'
        elif self.symbol[-3] == 'z':
            y = '07-26'
            v = '11-25'

        start = (lambda x, y: '20' + x + '-' + y)(x, y)
        end = (lambda z, v: '20' + z + '-' + v)(z, v)

        return start, end

    def es(self):
        x = self.symbol[-2:]
        y = None
        z = self.symbol[-2:]
        v = None

        if self.symbol[-3] == 'h':
            y = '12-08'
            v = '03-07'
            x = str(int('20' + x) - 1)[-2:]
        elif self.symbol[-3] == 'm':
            y = '03-08'
            v = '06-07'
        elif self.symbol[-3] == 'u':
            y = '06-08'
            v = '09-07'
        elif self.symbol[-3] == 'z':
            y = '09-08'
            v = '12-07'

        start = (lambda x, y: '20' + x + '-' + y)(x, y)
        end = (lambda z, v: '20' + z + '-' + v)(z, v)

        return start, end

class TrainTest:  # Train and test arrangement
    def __init__(self):
        pass
    def zw(self):
        tr1 = ['zwh06', 'zwk06', 'zwn06', 'zwu06', 'zwz06',
               'zwh07', 'zwk07', 'zwn07', 'zwu07', 'zwz07',
               'zwh08', 'zwk08', 'zwn08', 'zwu08', 'zwz08',
               'zwh09', 'zwk09', 'zwn09', 'zwu09', 'zwz09',
               'zwh10', 'zwk10', 'zwn10', 'zwu10', 'zwz10']
        te1 = ['zwh11', 'zwk11', 'zwn11', 'zwu11', 'zwz11']

        tr2 = ['zwh07', 'zwk07', 'zwn07', 'zwu07', 'zwz07',
               'zwh08', 'zwk08', 'zwn08', 'zwu08', 'zwz08',
               'zwh09', 'zwk09', 'zwn09', 'zwu09', 'zwz09',
               'zwh10', 'zwk10', 'zwn10', 'zwu10', 'zwz10',
               'zwh11', 'zwk11', 'zwn11', 'zwu11', 'zwz11']
        te2 = ['zwh12', 'zwk12', 'zwn12', 'zwu12', 'zwz12']

        tr3 = ['zwh08', 'zwk08', 'zwn08', 'zwu08', 'zwz08',
               'zwh09', 'zwk09', 'zwn09', 'zwu09', 'zwz09',
               'zwh10', 'zwk10', 'zwn10', 'zwu10', 'zwz10',
               'zwh11', 'zwk11', 'zwn11', 'zwu11', 'zwz11',
               'zwh12', 'zwk12', 'zwn12', 'zwu12', 'zwz12']
        te3 = ['zwh13', 'zwk13', 'zwn13', 'zwu13', 'zwz13']

        tr4 = ['zwh09', 'zwk09', 'zwn09', 'zwu09', 'zwz09',
               'zwh10', 'zwk10', 'zwn10', 'zwu10', 'zwz10',
               'zwh11', 'zwk11', 'zwn11', 'zwu11', 'zwz11',
               'zwh12', 'zwk12', 'zwn12', 'zwu12', 'zwz12',
               'zwh13', 'zwk13', 'zwn13', 'zwu13', 'zwz13']
        te4 = ['zwh14', 'zwk14', 'zwn14', 'zwu14', 'zwz14']

        tr5 = ['zwh10', 'zwk10', 'zwn10', 'zwu10', 'zwz10',
               'zwh11', 'zwk11', 'zwn11', 'zwu11', 'zwz11',
               'zwh12', 'zwk12', 'zwn12', 'zwu12', 'zwz12',
               'zwh13', 'zwk13', 'zwn13', 'zwu13', 'zwz13',
               'zwh14', 'zwk14', 'zwn14', 'zwu14', 'zwz14']
        te5 = ['zwh15', 'zwk15', 'zwn15', 'zwu15', 'zwz15']

        tr6 = ['zwh11', 'zwk11', 'zwn11', 'zwu11', 'zwz11',
               'zwh12', 'zwk12', 'zwn12', 'zwu12', 'zwz12',
               'zwh13', 'zwk13', 'zwn13', 'zwu13', 'zwz13',
               'zwh14', 'zwk14', 'zwn14', 'zwu14', 'zwz14',
               'zwh15', 'zwk15', 'zwn15', 'zwu15', 'zwz15']
        te6 = ['zwh16', 'zwk16', 'zwn16', 'zwu16', 'zwz16']

        tr7 = ['zwh12', 'zwk12', 'zwn12', 'zwu12', 'zwz12',
               'zwh13', 'zwk13', 'zwn13', 'zwu13', 'zwz13',
               'zwh14', 'zwk14', 'zwn14', 'zwu14', 'zwz14',
               'zwh15', 'zwk15', 'zwn15', 'zwu15', 'zwz15',
               'zwh16', 'zwk16', 'zwn16', 'zwu16', 'zwz16']
        te7 = ['zwh17', 'zwk17', 'zwn17', 'zwu17', 'zwz17']

        tr8 = ['zwh13', 'zwk13', 'zwn13', 'zwu13', 'zwz13',
               'zwh14', 'zwk14', 'zwn14', 'zwu14', 'zwz14',
               'zwh15', 'zwk15', 'zwn15', 'zwu15', 'zwz15',
               'zwh16', 'zwk16', 'zwn16', 'zwu16', 'zwz16',
               'zwh17', 'zwk17', 'zwn17', 'zwu17', 'zwz17']
        te8 = ['zwh18', 'zwk18', 'zwn18', 'zwu18', 'zwz18']

        tr9 = ['zwh14', 'zwk14', 'zwn14', 'zwu14', 'zwz14',
               'zwh15', 'zwk15', 'zwn15', 'zwu15', 'zwz15',
               'zwh16', 'zwk16', 'zwn16', 'zwu16', 'zwz16',
               'zwh17', 'zwk17', 'zwn17', 'zwu17', 'zwz17',
               'zwh18', 'zwk18', 'zwn18', 'zwu18', 'zwz18']
        te9 = ['zwh19', 'zwk19', 'zwn19', 'zwu19', 'zwz19']

        tr10 = ['zwh15', 'zwk15', 'zwn15', 'zwu15', 'zwz15',
                'zwh16', 'zwk16', 'zwn16', 'zwu16', 'zwz16',
                'zwh17', 'zwk17', 'zwn17', 'zwu17', 'zwz17',
                'zwh18', 'zwk18', 'zwn18', 'zwu18', 'zwz18',
                'zwh19', 'zwk19', 'zwn19', 'zwu19', 'zwz19']
        te10 = ['zwh20', 'zwk20', 'zwn20', 'zwu20', 'zwz20']

        tr11 = ['zwh16', 'zwk16', 'zwn16', 'zwu16', 'zwz16',
                'zwh17', 'zwk17', 'zwn17', 'zwu17', 'zwz17',
                'zwh18', 'zwk18', 'zwn18', 'zwu18', 'zwz18',
                'zwh19', 'zwk19', 'zwn19', 'zwu19', 'zwz19',
                'zwh20', 'zwk20', 'zwn20', 'zwu20', 'zwz20']
        te11 = ['zwh21', 'zwk21', 'zwn21', 'zwu21', 'zwz21']

        tr12 = ['zwh17', 'zwk17', 'zwn17', 'zwu17', 'zwz17',
                'zwh18', 'zwk18', 'zwn18', 'zwu18', 'zwz18',
                'zwh19', 'zwk19', 'zwn19', 'zwu19', 'zwz19',
                'zwh20', 'zwk20', 'zwn20', 'zwu20', 'zwz20',
                'zwh21', 'zwk21', 'zwn21', 'zwu21', 'zwz21']
        te12 = ['zwh22']

        return tr1, te1, tr2, te2, tr3, te3, tr4, te4, \
               tr5, te5, tr6, te6, tr7, te7, tr8, te8, \
               tr9, te9, tr10, te10, tr11, te11, tr12, te12

    def zc(self):
        tr1 = ['zch06', 'zck06', 'zcn06', 'zcu06', 'zcz06',
               'zch07', 'zck07', 'zcn07', 'zcu07', 'zcz07',
               'zch08', 'zck08', 'zcn08', 'zcu08', 'zcz08',
               'zch09', 'zck09', 'zcn09', 'zcu09', 'zcz09',
               'zch10', 'zck10', 'zcn10', 'zcu10', 'zcz10']
        te1 = ['zch11', 'zck11', 'zcn11', 'zcu11', 'zcz11']

        tr2 = ['zch07', 'zck07', 'zcn07', 'zcu07', 'zcz07',
               'zch08', 'zck08', 'zcn08', 'zcu08', 'zcz08',
               'zch09', 'zck09', 'zcn09', 'zcu09', 'zcz09',
               'zch10', 'zck10', 'zcn10', 'zcu10', 'zcz10',
               'zch11', 'zck11', 'zcn11', 'zcu11', 'zcz11']
        te2 = ['zch12', 'zck12', 'zcn12', 'zcu12', 'zcz12']

        tr3 = ['zch08', 'zck08', 'zcn08', 'zcu08', 'zcz08',
               'zch09', 'zck09', 'zcn09', 'zcu09', 'zcz09',
               'zch10', 'zck10', 'zcn10', 'zcu10', 'zcz10',
               'zch11', 'zck11', 'zcn11', 'zcu11', 'zcz11',
               'zch12', 'zck12', 'zcn12', 'zcu12', 'zcz12']
        te3 = ['zch13', 'zck13', 'zcn13', 'zcu13', 'zcz13']

        tr4 = ['zch09', 'zck09', 'zcn09', 'zcu09', 'zcz09',
               'zch10', 'zck10', 'zcn10', 'zcu10', 'zcz10',
               'zch11', 'zck11', 'zcn11', 'zcu11', 'zcz11',
               'zch12', 'zck12', 'zcn12', 'zcu12', 'zcz12',
               'zch13', 'zck13', 'zcn13', 'zcu13', 'zcz13']
        te4 = ['zch14', 'zck14', 'zcn14', 'zcu14', 'zcz14']

        tr5 = ['zch10', 'zck10', 'zcn10', 'zcu10', 'zcz10',
               'zch11', 'zck11', 'zcn11', 'zcu11', 'zcz11',
               'zch12', 'zck12', 'zcn12', 'zcu12', 'zcz12',
               'zch13', 'zck13', 'zcn13', 'zcu13', 'zcz13',
               'zch14', 'zck14', 'zcn14', 'zcu14', 'zcz14']
        te5 = ['zch15', 'zck15', 'zcn15', 'zcu15', 'zcz15']

        tr6 = ['zch11', 'zck11', 'zcn11', 'zcu11', 'zcz11',
               'zch12', 'zck12', 'zcn12', 'zcu12', 'zcz12',
               'zch13', 'zck13', 'zcn13', 'zcu13', 'zcz13',
               'zch14', 'zck14', 'zcn14', 'zcu14', 'zcz14',
               'zch15', 'zck15', 'zcn15', 'zcu15', 'zcz15']
        te6 = ['zch16', 'zck16', 'zcn16', 'zcu16', 'zcz16']

        tr7 = ['zch12', 'zck12', 'zcn12', 'zcu12', 'zcz12',
               'zch13', 'zck13', 'zcn13', 'zcu13', 'zcz13',
               'zch14', 'zck14', 'zcn14', 'zcu14', 'zcz14',
               'zch15', 'zck15', 'zcn15', 'zcu15', 'zcz15',
               'zch16', 'zck16', 'zcn16', 'zcu16', 'zcz16']
        te7 = ['zch17', 'zck17', 'zcn17', 'zcu17', 'zcz17']

        tr8 = ['zch13', 'zck13', 'zcn13', 'zcu13', 'zcz13',
               'zch14', 'zck14', 'zcn14', 'zcu14', 'zcz14',
               'zch15', 'zck15', 'zcn15', 'zcu15', 'zcz15',
               'zch16', 'zck16', 'zcn16', 'zcu16', 'zcz16',
               'zch17', 'zck17', 'zcn17', 'zcu17', 'zcz17']
        te8 = ['zch18', 'zck18', 'zcn18', 'zcu18', 'zcz18']

        tr9 = ['zch14', 'zck14', 'zcn14', 'zcu14', 'zcz14',
               'zch15', 'zck15', 'zcn15', 'zcu15', 'zcz15',
               'zch16', 'zck16', 'zcn16', 'zcu16', 'zcz16',
               'zch17', 'zck17', 'zcn17', 'zcu17', 'zcz17',
               'zch18', 'zck18', 'zcn18', 'zcu18', 'zcz18']
        te9 = ['zch19', 'zck19', 'zcn19', 'zcu19', 'zcz19']

        tr10 = ['zch15', 'zck15', 'zcn15', 'zcu15', 'zcz15',
                'zch16', 'zck16', 'zcn16', 'zcu16', 'zcz16',
                'zch17', 'zck17', 'zcn17', 'zcu17', 'zcz17',
                'zch18', 'zck18', 'zcn18', 'zcu18', 'zcz18',
                'zch19', 'zck19', 'zcn19', 'zcu19', 'zcz19']
        te10 = ['zch20', 'zck20', 'zcn20', 'zcu20', 'zcz20']

        tr11 = ['zch16', 'zck16', 'zcn16', 'zcu16', 'zcz16',
                'zch17', 'zck17', 'zcn17', 'zcu17', 'zcz17',
                'zch18', 'zck18', 'zcn18', 'zcu18', 'zcz18',
                'zch19', 'zck19', 'zcn19', 'zcu19', 'zcz19',
                'zch20', 'zck20', 'zcn20', 'zcu20', 'zcz20']
        te11 = ['zch21', 'zck21', 'zcn21', 'zcu21', 'zcz21']

        tr12 = ['zch17', 'zck17', 'zcn17', 'zcu17', 'zcz17',
                'zch18', 'zck18', 'zcn18', 'zcu18', 'zcz18',
                'zch19', 'zck19', 'zcn19', 'zcu19', 'zcz19',
                'zch20', 'zck20', 'zcn20', 'zcu20', 'zcz20',
                'zch21', 'zck21', 'zcn21', 'zcu21', 'zcz21']
        te12 = ['zch22']

        return tr1, te1, tr2, te2, tr3, te3, tr4, te4, \
               tr5, te5, tr6, te6, tr7, te7, tr8, te8, \
               tr9, te9, tr10, te10, tr11, te11, tr12, te12

    def zs(self):
        tr1 = ['zsf06', 'zsh06', 'zsk06', 'zsn06', 'zsq06', 'zsu06', 'zsx06',
               'zsf07', 'zsh07', 'zsk07', 'zsn07', 'zsq07', 'zsu07', 'zsx07',
               'zsf08', 'zsh08', 'zsk08', 'zsn08', 'zsq08', 'zsu08', 'zsx08',
               'zsf09', 'zsh09', 'zsk09', 'zsn09', 'zsq09', 'zsu09', 'zsx09',
               'zsf10', 'zsh10', 'zsk10', 'zsn10', 'zsq10', 'zsu10', 'zsx10',]
        te1 = ['zsf11', 'zsh11', 'zsk11', 'zsn11', 'zsq11', 'zsu11', 'zsx11',]

        tr2 = ['zsf07', 'zsh07', 'zsk07', 'zsn07', 'zsq07', 'zsu07', 'zsx07',
               'zsf08', 'zsh08', 'zsk08', 'zsn08', 'zsq08', 'zsu08', 'zsx08',
               'zsf09', 'zsh09', 'zsk09', 'zsn09', 'zsq09', 'zsu09', 'zsx09',
               'zsf10', 'zsh10', 'zsk10', 'zsn10', 'zsq10', 'zsu10', 'zsx10',
               'zsf11', 'zsh11', 'zsk11', 'zsn11', 'zsq11', 'zsu11', 'zsx11', ]
        te2 = ['zsf12', 'zsh12', 'zsk12', 'zsn12', 'zsq12', 'zsu12', 'zsx12', ]

        tr3 = ['zsf08', 'zsh08', 'zsk08', 'zsn08', 'zsq08', 'zsu08', 'zsx08',
               'zsf09', 'zsh09', 'zsk09', 'zsn09', 'zsq09', 'zsu09', 'zsx09',
               'zsf10', 'zsh10', 'zsk10', 'zsn10', 'zsq10', 'zsu10', 'zsx10',
               'zsf11', 'zsh11', 'zsk11', 'zsn11', 'zsq11', 'zsu11', 'zsx11',
               'zsf12', 'zsh12', 'zsk12', 'zsn12', 'zsq12', 'zsu12', 'zsx12', ]
        te3 = ['zsf13', 'zsh13', 'zsk13', 'zsn13', 'zsq13', 'zsu13', 'zsx13', ]

        tr4 = ['zsf09', 'zsh09', 'zsk09', 'zsn09', 'zsq09', 'zsu09', 'zsx09',
               'zsf10', 'zsh10', 'zsk10', 'zsn10', 'zsq10', 'zsu10', 'zsx10',
               'zsf11', 'zsh11', 'zsk11', 'zsn11', 'zsq11', 'zsu11', 'zsx11',
               'zsf12', 'zsh12', 'zsk12', 'zsn12', 'zsq12', 'zsu12', 'zsx12',
               'zsf13', 'zsh13', 'zsk13', 'zsn13', 'zsq13', 'zsu13', 'zsx13', ]
        te4 = ['zsf14', 'zsh14', 'zsk14', 'zsn14', 'zsq14', 'zsu14', 'zsx14', ]

        tr5 = ['zsf10', 'zsh10', 'zsk10', 'zsn10', 'zsq10', 'zsu10', 'zsx10',
               'zsf11', 'zsh11', 'zsk11', 'zsn11', 'zsq11', 'zsu11', 'zsx11',
               'zsf12', 'zsh12', 'zsk12', 'zsn12', 'zsq12', 'zsu12', 'zsx12',
               'zsf13', 'zsh13', 'zsk13', 'zsn13', 'zsq13', 'zsu13', 'zsx13',
               'zsf14', 'zsh14', 'zsk14', 'zsn14', 'zsq14', 'zsu14', 'zsx14', ]
        te5 = ['zsf15', 'zsh15', 'zsk15', 'zsn15', 'zsq15', 'zsu15', 'zsx15', ]

        tr6 = ['zsf11', 'zsh11', 'zsk11', 'zsn11', 'zsq11', 'zsu11', 'zsx11',
               'zsf12', 'zsh12', 'zsk12', 'zsn12', 'zsq12', 'zsu12', 'zsx12',
               'zsf13', 'zsh13', 'zsk13', 'zsn13', 'zsq13', 'zsu13', 'zsx13',
               'zsf14', 'zsh14', 'zsk14', 'zsn14', 'zsq14', 'zsu14', 'zsx14',
               'zsf15', 'zsh15', 'zsk15', 'zsn15', 'zsq15', 'zsu15', 'zsx15', ]
        te6 = ['zsf16', 'zsh16', 'zsk16', 'zsn16', 'zsq16', 'zsu16', 'zsx16', ]

        tr7 = ['zsf12', 'zsh12', 'zsk12', 'zsn12', 'zsq12', 'zsu12', 'zsx12',
               'zsf13', 'zsh13', 'zsk13', 'zsn13', 'zsq13', 'zsu13', 'zsx13',
               'zsf14', 'zsh14', 'zsk14', 'zsn14', 'zsq14', 'zsu14', 'zsx14',
               'zsf15', 'zsh15', 'zsk15', 'zsn15', 'zsq15', 'zsu15', 'zsx15',
               'zsf16', 'zsh16', 'zsk16', 'zsn16', 'zsq16', 'zsu16', 'zsx16', ]
        te7 = ['zsf17', 'zsh17', 'zsk17', 'zsn17', 'zsq17', 'zsu17', 'zsx17', ]

        tr8 = ['zsf13', 'zsh13', 'zsk13', 'zsn13', 'zsq13', 'zsu13', 'zsx13',
               'zsf14', 'zsh14', 'zsk14', 'zsn14', 'zsq14', 'zsu14', 'zsx14',
               'zsf15', 'zsh15', 'zsk15', 'zsn15', 'zsq15', 'zsu15', 'zsx15',
               'zsf16', 'zsh16', 'zsk16', 'zsn16', 'zsq16', 'zsu16', 'zsx16',
               'zsf17', 'zsh17', 'zsk17', 'zsn17', 'zsq17', 'zsu17', 'zsx17', ]
        te8 = ['zsf18', 'zsh18', 'zsk18', 'zsn18', 'zsq18', 'zsu18', 'zsx18', ]

        tr9 = ['zsf14', 'zsh14', 'zsk14', 'zsn14', 'zsq14', 'zsu14', 'zsx14',
               'zsf15', 'zsh15', 'zsk15', 'zsn15', 'zsq15', 'zsu15', 'zsx15',
               'zsf16', 'zsh16', 'zsk16', 'zsn16', 'zsq16', 'zsu16', 'zsx16',
               'zsf17', 'zsh17', 'zsk17', 'zsn17', 'zsq17', 'zsu17', 'zsx17',
               'zsf18', 'zsh18', 'zsk18', 'zsn18', 'zsq18', 'zsu18', 'zsx18', ]
        te9 = ['zsf19', 'zsh19', 'zsk19', 'zsn19', 'zsq19', 'zsu19', 'zsx19', ]

        tr10 = ['zsf15', 'zsh15', 'zsk15', 'zsn15', 'zsq15', 'zsu15', 'zsx15',
                'zsf16', 'zsh16', 'zsk16', 'zsn16', 'zsq16', 'zsu16', 'zsx16',
                'zsf17', 'zsh17', 'zsk17', 'zsn17', 'zsq17', 'zsu17', 'zsx17',
                'zsf18', 'zsh18', 'zsk18', 'zsn18', 'zsq18', 'zsu18', 'zsx18',
                'zsf19', 'zsh19', 'zsk19', 'zsn19', 'zsq19', 'zsu19', 'zsx19', ]
        te10 = ['zsf20', 'zsh20', 'zsk20', 'zsn20', 'zsq20', 'zsu20', 'zsx20', ]

        tr11 = ['zsf16', 'zsh16', 'zsk16', 'zsn16', 'zsq16', 'zsu16', 'zsx16',
                'zsf17', 'zsh17', 'zsk17', 'zsn17', 'zsq17', 'zsu17', 'zsx17',
                'zsf18', 'zsh18', 'zsk18', 'zsn18', 'zsq18', 'zsu18', 'zsx18',
                'zsf19', 'zsh19', 'zsk19', 'zsn19', 'zsq19', 'zsu19', 'zsx19',
                'zsf20', 'zsh20', 'zsk20', 'zsn20', 'zsq20', 'zsu20', 'zsx20', ]
        te11 = ['zsf21', 'zsh21', 'zsk21', 'zsn21', 'zsq21', 'zsu21', 'zsx21', ]

        tr12 = ['zsf17', 'zsh17', 'zsk17', 'zsn17', 'zsq17', 'zsu17', 'zsx17',
                'zsf18', 'zsh18', 'zsk18', 'zsn18', 'zsq18', 'zsu18', 'zsx18',
                'zsf19', 'zsh19', 'zsk19', 'zsn19', 'zsq19', 'zsu19', 'zsx19',
                'zsf20', 'zsh20', 'zsk20', 'zsn20', 'zsq20', 'zsu20', 'zsx20',
                'zsf21', 'zsh21', 'zsk21', 'zsn21', 'zsq21', 'zsu21', 'zsx21', ]
        te12 = ['zsf22', 'zsh22']

        return tr1, te1, tr2, te2, tr3, te3, tr4, te4, \
               tr5, te5, tr6, te6, tr7, te7, tr8, te8, \
               tr9, te9, tr10, te10, tr11, te11, tr12, te12

    def ebm(self):
        tr1 = ['ebmh06', 'ebmk06', 'ebmu06', 'ebmz06',
               'ebmh07', 'ebmk07', 'ebmu07', 'ebmz07',
               'ebmh08', 'ebmk08', 'ebmu08', 'ebmz08',
               'ebmh09', 'ebmk09', 'ebmu09', 'ebmz09',
               'ebmh10', 'ebmk10', 'ebmu10', 'ebmz10']
        te1 = ['ebmh11', 'ebmk11', 'ebmu11', 'ebmz11']

        tr2 = ['ebmh07', 'ebmk07', 'ebmu07', 'ebmz07',
               'ebmh08', 'ebmk08', 'ebmu08', 'ebmz08',
               'ebmh09', 'ebmk09', 'ebmu09', 'ebmz09',
               'ebmh10', 'ebmk10', 'ebmu10', 'ebmz10',
               'ebmh11', 'ebmk11', 'ebmu11', 'ebmz11']
        te2 = ['ebmh12', 'ebmk12', 'ebmu12', 'ebmz12']

        tr3 = ['ebmh08', 'ebmk08', 'ebmu08', 'ebmz08',
               'ebmh09', 'ebmk09', 'ebmu09', 'ebmz09',
               'ebmh10', 'ebmk10', 'ebmu10', 'ebmz10',
               'ebmh11', 'ebmk11', 'ebmu11', 'ebmz11',
               'ebmh12', 'ebmk12', 'ebmu12', 'ebmz12']
        te3 = ['ebmh13', 'ebmk13', 'ebmu13', 'ebmz13']

        tr4 = ['ebmh09', 'ebmk09', 'ebmu09', 'ebmz09',
               'ebmh10', 'ebmk10', 'ebmu10', 'ebmz10',
               'ebmh11', 'ebmk11', 'ebmu11', 'ebmz11',
               'ebmh12', 'ebmk12', 'ebmu12', 'ebmz12',
               'ebmh13', 'ebmk13', 'ebmu13', 'ebmz13']
        te4 = ['ebmh14', 'ebmk14', 'ebmu14', 'ebmz14']

        tr5 = ['ebmh10', 'ebmk10', 'ebmu10', 'ebmz10',
               'ebmh11', 'ebmk11', 'ebmu11', 'ebmz11',
               'ebmh12', 'ebmk12', 'ebmu12', 'ebmz12',
               'ebmh13', 'ebmk13', 'ebmu13', 'ebmz13',
               'ebmh14', 'ebmk14', 'ebmu14', 'ebmz14']
        te5 = ['ebmh15', 'ebmk15', 'ebmu15', 'ebmz15']

        tr6 = ['ebmh11', 'ebmk11', 'ebmu11', 'ebmz11',
               'ebmh12', 'ebmk12', 'ebmu12', 'ebmz12',
               'ebmh13', 'ebmk13', 'ebmu13', 'ebmz13',
               'ebmh14', 'ebmk14', 'ebmu14', 'ebmz14',
               'ebmh15', 'ebmk15', 'ebmu15', 'ebmz15']
        te6 = ['ebmh16', 'ebmk16', 'ebmu16', 'ebmz16']

        tr7 = ['ebmh12', 'ebmk12', 'ebmu12', 'ebmz12',
               'ebmh13', 'ebmk13', 'ebmu13', 'ebmz13',
               'ebmh14', 'ebmk14', 'ebmu14', 'ebmz14',
               'ebmh15', 'ebmk15', 'ebmu15', 'ebmz15',
               'ebmh16', 'ebmk16', 'ebmu16', 'ebmz16']
        te7 = ['ebmh17', 'ebmk17', 'ebmu17', 'ebmz17']

        tr8 = ['ebmh13', 'ebmk13', 'ebmu13', 'ebmz13',
               'ebmh14', 'ebmk14', 'ebmu14', 'ebmz14',
               'ebmh15', 'ebmk15', 'ebmu15', 'ebmz15',
               'ebmh16', 'ebmk16', 'ebmu16', 'ebmz16',
               'ebmh17', 'ebmk17', 'ebmu17', 'ebmz17']
        te8 = ['ebmh18', 'ebmk18', 'ebmu18', 'ebmz18']

        tr9 = ['ebmh14', 'ebmk14', 'ebmu14', 'ebmz14',
               'ebmh15', 'ebmk15', 'ebmu15', 'ebmz15',
               'ebmh16', 'ebmk16', 'ebmu16', 'ebmz16',
               'ebmh17', 'ebmk17', 'ebmu17', 'ebmz17',
               'ebmh18', 'ebmk18', 'ebmu18', 'ebmz18']
        te9 = ['ebmh19', 'ebmk19', 'ebmu19', 'ebmz19']

        tr10 = ['ebmh15', 'ebmk15', 'ebmu15', 'ebmz15',
                'ebmh16', 'ebmk16', 'ebmu16', 'ebmz16',
                'ebmh17', 'ebmk17', 'ebmu17', 'ebmz17',
                'ebmh18', 'ebmk18', 'ebmu18', 'ebmz18',
                'ebmh19', 'ebmk19', 'ebmu19', 'ebmz19']
        te10 = ['ebmh20', 'ebmk20', 'ebmu20', 'ebmz20']

        tr11 = ['ebmh16', 'ebmk16', 'ebmu16', 'ebmz16',
                'ebmh17', 'ebmk17', 'ebmu17', 'ebmz17',
                'ebmh18', 'ebmk18', 'ebmu18', 'ebmz18',
                'ebmh19', 'ebmk19', 'ebmu19', 'ebmz19',
                'ebmh20', 'ebmk20', 'ebmu20', 'ebmz20']
        te11 = ['ebmh21', 'ebmk21', 'ebmu21', 'ebmz21']

        tr12 = ['ebmh17', 'ebmk17', 'ebmu17', 'ebmz17',
                'ebmh18', 'ebmk18', 'ebmu18', 'ebmz18',
                'ebmh19', 'ebmk19', 'ebmu19', 'ebmz19',
                'ebmh20', 'ebmk20', 'ebmu20', 'ebmz20',
                'ebmh21', 'ebmk21', 'ebmu21', 'ebmz21']
        te12 = ['ebmh22']

        return tr1, te1, tr2, te2, tr3, te3, tr4, te4, \
               tr5, te5, tr6, te6, tr7, te7, tr8, te8, \
               tr9, te9, tr10, te10, tr11, te11, tr12, te12

    def cl(self):
        tr1 = ['clf06','clg06','clh06','clj06','clk06','clm06','cln06','clq06','clu06','clv06','clx06','clz06',
               'clf07','clg07','clh07','clj07','clk07','clm07','cln07','clq07','clu07','clv07','clx07','clz07',
               'clf08','clg08','clh08','clj08','clk08','clm08','cln08','clq08','clu08','clv08','clx08','clz08',
               'clf09','clg09','clh09','clj09','clk09','clm09','cln09','clq09','clu09','clv09','clx09','clz09',
               'clf10','clg10','clh10','clj10','clk10','clm10','cln10','clq10','clu10','clv10','clx10','clz10']
        te1 = ['clf11','clg11','clh11','clj11','clk11','clm11','cln11','clq11','clu11','clv11','clx11','clz11']

        tr2 = ['clf07','clg07','clh07','clj07','clk07','clm07','cln07','clq07','clu07','clv07','clx07','clz07',
               'clf08','clg08','clh08','clj08','clk08','clm08','cln08','clq08','clu08','clv08','clx08','clz08',
               'clf09','clg09','clh09','clj09','clk09','clm09','cln09','clq09','clu09','clv09','clx09','clz09',
               'clf10','clg10','clh10','clj10','clk10','clm10','cln10','clq10','clu10','clv10','clx10','clz10',
               'clf11','clg11','clh11','clj11','clk11','clm11','cln11','clq11','clu11','clv11','clx11','clz11']
        te2 = ['clf12','clg12','clh12','clj12','clk12','clm12','cln12','clq12','clu12','clv12','clx12','clz12']

        tr3 = ['clf08','clg08','clh08','clj08','clk08','clm08','cln08','clq08','clu08','clv08','clx08','clz08',
               'clf09','clg09','clh09','clj09','clk09','clm09','cln09','clq09','clu09','clv09','clx09','clz09',
               'clf10','clg10','clh10','clj10','clk10','clm10','cln10','clq10','clu10','clv10','clx10','clz10',
               'clf11','clg11','clh11','clj11','clk11','clm11','cln11','clq11','clu11','clv11','clx11','clz11',
               'clf12','clg12','clh12','clj12','clk12','clm12','cln12','clq12','clu12','clv12','clx12','clz12']
        te3 = ['clf13','clg13','clh13','clj13','clk13','clm13','cln13','clq13','clu13','clv13','clx13','clz13']

        tr4 = ['clf09','clg09','clh09','clj09','clk09','clm09','cln09','clq09','clu09','clv09','clx09','clz09',
               'clf10','clg10','clh10','clj10','clk10','clm10','cln10','clq10','clu10','clv10','clx10','clz10',
               'clf11','clg11','clh11','clj11','clk11','clm11','cln11','clq11','clu11','clv11','clx11','clz11',
               'clf12','clg12','clh12','clj12','clk12','clm12','cln12','clq12','clu12','clv12','clx12','clz12',
               'clf13','clg13','clh13','clj13','clk13','clm13','cln13','clq13','clu13','clv13','clx13','clz13']
        te4 = ['clf14','clg14','clh14','clj14','clk14','clm14','cln14','clq14','clu14','clv14','clx14','clz14']

        tr5 = ['clf10','clg10','clh10','clj10','clk10','clm10','cln10','clq10','clu10','clv10','clx10','clz10',
               'clf11','clg11','clh11','clj11','clk11','clm11','cln11','clq11','clu11','clv11','clx11','clz11',
               'clf12','clg12','clh12','clj12','clk12','clm12','cln12','clq12','clu12','clv12','clx12','clz12',
               'clf13','clg13','clh13','clj13','clk13','clm13','cln13','clq13','clu13','clv13','clx13','clz13',
               'clf14','clg14','clh14','clj14','clk14','clm14','cln14','clq14','clu14','clv14','clx14','clz14']
        te5 = ['clf15','clg15','clh15','clj15','clk15','clm15','cln15','clq15','clu15','clv15','clx15','clz15']

        tr6 = ['clf11','clg11','clh11','clj11','clk11','clm11','cln11','clq11','clu11','clv11','clx11','clz11',
               'clf12','clg12','clh12','clj12','clk12','clm12','cln12','clq12','clu12','clv12','clx12','clz12',
               'clf13','clg13','clh13','clj13','clk13','clm13','cln13','clq13','clu13','clv13','clx13','clz13',
               'clf14','clg14','clh14','clj14','clk14','clm14','cln14','clq14','clu14','clv14','clx14','clz14',
               'clf15','clg15','clh15','clj15','clk15','clm15','cln15','clq15','clu15','clv15','clx15','clz15']
        te6 = ['clf16','clg16','clh16','clj16','clk16','clm16','cln16','clq16','clu16','clv16','clx16','clz16']

        tr7 = ['clf12','clg12','clh12','clj12','clk12','clm12','cln12','clq12','clu12','clv12','clx12','clz12',
               'clf13','clg13','clh13','clj13','clk13','clm13','cln13','clq13','clu13','clv13','clx13','clz13',
               'clf14','clg14','clh14','clj14','clk14','clm14','cln14','clq14','clu14','clv14','clx14','clz14',
               'clf15','clg15','clh15','clj15','clk15','clm15','cln15','clq15','clu15','clv15','clx15','clz15',
               'clf16','clg16','clh16','clj16','clk16','clm16','cln16','clq16','clu16','clv16','clx16','clz16']
        te7 = ['clf17','clg17','clh17','clj17','clk17','clm17','cln17','clq17','clu17','clv17','clx17','clz17']

        tr8 = ['clf13','clg13','clh13','clj13','clk13','clm13','cln13','clq13','clu13','clv13','clx13','clz13',
               'clf14','clg14','clh14','clj14','clk14','clm14','cln14','clq14','clu14','clv14','clx14','clz14',
               'clf15','clg15','clh15','clj15','clk15','clm15','cln15','clq15','clu15','clv15','clx15','clz15',
               'clf16','clg16','clh16','clj16','clk16','clm16','cln16','clq16','clu16','clv16','clx16','clz16',
               'clf17','clg17','clh17','clj17','clk17','clm17','cln17','clq17','clu17','clv17','clx17','clz17']
        te8 = ['clf18','clg18','clh18','clj18','clk18','clm18','cln18','clq18','clu18','clv18','clx18','clz18']

        tr9 = ['clf14','clg14','clh14','clj14','clk14','clm14','cln14','clq14','clu14','clv14','clx14','clz14',
               'clf15','clg15','clh15','clj15','clk15','clm15','cln15','clq15','clu15','clv15','clx15','clz15',
               'clf16','clg16','clh16','clj16','clk16','clm16','cln16','clq16','clu16','clv16','clx16','clz16',
               'clf17','clg17','clh17','clj17','clk17','clm17','cln17','clq17','clu17','clv17','clx17','clz17',
               'clf18','clg18','clh18','clj18','clk18','clm18','cln18','clq18','clu18','clv18','clx18','clz18']
        te9 = ['clf19','clg19','clh19','clj19','clk19','clm19','cln19','clq19','clu19','clv19','clx19','clz19']

        tr10 = ['clf15','clg15','clh15','clj15','clk15','clm15','cln15','clq15','clu15','clv15','clx15','clz15',
               'clf16','clg16','clh16','clj16','clk16','clm16','cln16','clq16','clu16','clv16','clx16','clz16',
               'clf17','clg17','clh17','clj17','clk17','clm17','cln17','clq17','clu17','clv17','clx17','clz17',
               'clf18','clg18','clh18','clj18','clk18','clm18','cln18','clq18','clu18','clv18','clx18','clz18',
               'clf19','clg19','clh19','clj19','clk19','clm19','cln19','clq19','clu19','clv19','clx19','clz19']
        te10 = ['clf20','clg20','clh20','clj20','clk20','clm20','cln20','clq20','clu20','clv20','clx20','clz20']

        tr11 = ['clf16','clg16','clh16','clj16','clk16','clm16','cln16','clq16','clu16','clv16','clx16','clz16',
               'clf17','clg17','clh17','clj17','clk17','clm17','cln17','clq17','clu17','clv17','clx17','clz17',
               'clf18','clg18','clh18','clj18','clk18','clm18','cln18','clq18','clu18','clv18','clx18','clz18',
               'clf19','clg19','clh19','clj19','clk19','clm19','cln19','clq19','clu19','clv19','clx19','clz19',
               'clf20','clg20','clh20','clj20','clk20','clm20','cln20','clq20','clu20','clv20','clx20','clz20']
        te11 = ['clf21','clg21','clh21','clj21','clk21','clm21','cln21','clq21','clu21','clv21','clx21','clz21']

        tr12 = ['clf17','clg17','clh17','clj17','clk17','clm17','cln17','clq17','clu17','clv17','clx17','clz17',
               'clf18','clg18','clh18','clj18','clk18','clm18','cln18','clq18','clu18','clv18','clx18','clz18',
               'clf19','clg19','clh19','clj19','clk19','clm19','cln19','clq19','clu19','clv19','clx19','clz19',
               'clf20','clg20','clh20','clj20','clk20','clm20','cln20','clq20','clu20','clv20','clx20','clz20',
               'clf21','clg21','clh21','clj21','clk21','clm21','cln21','clq21','clu21','clv21','clx21','clz21']
        te12 = ['clf22','clg22','clh22']

        return tr1, te1, tr2, te2, tr3, te3, tr4, te4, \
               tr5, te5, tr6, te6, tr7, te7, tr8, te8, \
               tr9, te9, tr10, te10, tr11, te11, tr12, te12

    def gc(self):
        tr1 = ['gcg06', 'gcj06', 'gcm06', 'gcq06', 'gcz06',
               'gcg07', 'gcj07', 'gcm07', 'gcq07', 'gcz07',
               'gcg08', 'gcj08', 'gcm08', 'gcq08', 'gcz08',
               'gcg09', 'gcj09', 'gcm09', 'gcq09', 'gcz09',
               'gcg10', 'gcj10', 'gcm10', 'gcq10', 'gcz10']
        te1 = ['gcg11', 'gcj11', 'gcm11', 'gcq11', 'gcz11']

        tr2 = ['gcg07', 'gcj07', 'gcm07', 'gcq07', 'gcz07',
               'gcg08', 'gcj08', 'gcm08', 'gcq08', 'gcz08',
               'gcg09', 'gcj09', 'gcm09', 'gcq09', 'gcz09',
               'gcg10', 'gcj10', 'gcm10', 'gcq10', 'gcz10',
               'gcg11', 'gcj11', 'gcm11', 'gcq11', 'gcz11']
        te2 = ['gcg12', 'gcj12', 'gcm12', 'gcq12', 'gcz12']

        tr3 = ['gcg08', 'gcj08', 'gcm08', 'gcq08', 'gcz08',
               'gcg09', 'gcj09', 'gcm09', 'gcq09', 'gcz09',
               'gcg10', 'gcj10', 'gcm10', 'gcq10', 'gcz10',
               'gcg11', 'gcj11', 'gcm11', 'gcq11', 'gcz11',
               'gcg12', 'gcj12', 'gcm12', 'gcq12', 'gcz12']
        te3 = ['gcg13', 'gcj13', 'gcm13', 'gcq13', 'gcz13']

        tr4 = ['gcg09', 'gcj09', 'gcm09', 'gcq09', 'gcz09',
               'gcg10', 'gcj10', 'gcm10', 'gcq10', 'gcz10',
               'gcg11', 'gcj11', 'gcm11', 'gcq11', 'gcz11',
               'gcg12', 'gcj12', 'gcm12', 'gcq12', 'gcz12',
               'gcg13', 'gcj13', 'gcm13', 'gcq13', 'gcz13']
        te4 = ['gcg14', 'gcj14', 'gcm14', 'gcq14', 'gcz14']

        tr5 = ['gcg10', 'gcj10', 'gcm10', 'gcq10', 'gcz10',
               'gcg11', 'gcj11', 'gcm11', 'gcq11', 'gcz11',
               'gcg12', 'gcj12', 'gcm12', 'gcq12', 'gcz12',
               'gcg13', 'gcj13', 'gcm13', 'gcq13', 'gcz13',
               'gcg14', 'gcj14', 'gcm14', 'gcq14', 'gcz14']
        te5 = ['gcg15', 'gcj15', 'gcm15', 'gcq15', 'gcz15']

        tr6 = ['gcg11', 'gcj11', 'gcm11', 'gcq11', 'gcz11',
               'gcg12', 'gcj12', 'gcm12', 'gcq12', 'gcz12',
               'gcg13', 'gcj13', 'gcm13', 'gcq13', 'gcz13',
               'gcg14', 'gcj14', 'gcm14', 'gcq14', 'gcz14',
               'gcg15', 'gcj15', 'gcm15', 'gcq15', 'gcz15']
        te6 = ['gcg16', 'gcj16', 'gcm16', 'gcq16', 'gcz16']

        tr7 = ['gcg12', 'gcj12', 'gcm12', 'gcq12', 'gcz12',
               'gcg13', 'gcj13', 'gcm13', 'gcq13', 'gcz13',
               'gcg14', 'gcj14', 'gcm14', 'gcq14', 'gcz14',
               'gcg15', 'gcj15', 'gcm15', 'gcq15', 'gcz15',
               'gcg16', 'gcj16', 'gcm16', 'gcq16', 'gcz16']
        te7 = ['gcg17', 'gcj17', 'gcm17', 'gcq17', 'gcz17']

        tr8 = ['gcg13', 'gcj13', 'gcm13', 'gcq13', 'gcz13',
               'gcg14', 'gcj14', 'gcm14', 'gcq14', 'gcz14',
               'gcg15', 'gcj15', 'gcm15', 'gcq15', 'gcz15',
               'gcg16', 'gcj16', 'gcm16', 'gcq16', 'gcz16',
               'gcg17', 'gcj17', 'gcm17', 'gcq17', 'gcz17']
        te8 = ['gcg18', 'gcj18', 'gcm18', 'gcq18', 'gcz18']

        tr9 = ['gcg14', 'gcj14', 'gcm14', 'gcq14', 'gcz14',
               'gcg15', 'gcj15', 'gcm15', 'gcq15', 'gcz15',
               'gcg16', 'gcj16', 'gcm16', 'gcq16', 'gcz16',
               'gcg17', 'gcj17', 'gcm17', 'gcq17', 'gcz17',
               'gcg18', 'gcj18', 'gcm18', 'gcq18', 'gcz18']
        te9 = ['gcg19', 'gcj19', 'gcm19', 'gcq19', 'gcz19']

        tr10 = ['gcg15', 'gcj15', 'gcm15', 'gcq15', 'gcz15',
                'gcg16', 'gcj16', 'gcm16', 'gcq16', 'gcz16',
                'gcg17', 'gcj17', 'gcm17', 'gcq17', 'gcz17',
                'gcg18', 'gcj18', 'gcm18', 'gcq18', 'gcz18',
                'gcg19', 'gcj19', 'gcm19', 'gcq19', 'gcz19']
        te10 = ['gcg20', 'gcj20', 'gcm20', 'gcq20', 'gcz20']

        tr11 = ['gcg16', 'gcj16', 'gcm16', 'gcq16', 'gcz16',
                'gcg17', 'gcj17', 'gcm17', 'gcq17', 'gcz17',
                'gcg18', 'gcj18', 'gcm18', 'gcq18', 'gcz18',
                'gcg19', 'gcj19', 'gcm19', 'gcq19', 'gcz19',
                'gcg20', 'gcj20', 'gcm20', 'gcq20', 'gcz20']
        te11 = ['gcg21', 'gcj21', 'gcm21', 'gcq21', 'gcz21']

        tr12 = ['gcg17', 'gcj17', 'gcm17', 'gcq17', 'gcz17',
                'gcg18', 'gcj18', 'gcm18', 'gcq18', 'gcz18',
                'gcg19', 'gcj19', 'gcm19', 'gcq19', 'gcz19',
                'gcg20', 'gcj20', 'gcm20', 'gcq20', 'gcz20',
                'gcg21', 'gcj21', 'gcm21', 'gcq21', 'gcz21']
        te12 = ['gcg22']

        return tr1, te1, tr2, te2, tr3, te3, tr4, te4, \
               tr5, te5, tr6, te6, tr7, te7, tr8, te8, \
               tr9, te9, tr10, te10, tr11, te11, tr12, te12

    def es(self):
        tr1 = ['esh06', 'esm06', 'esu06', 'esz06',
               'esh07', 'esm07', 'esu07', 'esz07',
               'esh08', 'esm08', 'esu08', 'esz08',
               'esh09', 'esm09', 'esu09', 'esz09',
               'esh10', 'esm10', 'esu10', 'esz10']
        te1 = ['esh11', 'esm11', 'esu11', 'esz11']

        tr2 = ['esh07', 'esm07', 'esu07', 'esz07',
               'esh08', 'esm08', 'esu08', 'esz08',
               'esh09', 'esm09', 'esu09', 'esz09',
               'esh10', 'esm10', 'esu10', 'esz10',
               'esh11', 'esm11', 'esu11', 'esz11']
        te2 = ['esh12', 'esm12', 'esu12', 'esz12']

        tr3 = ['esh08', 'esm08', 'esu08', 'esz08',
               'esh09', 'esm09', 'esu09', 'esz09',
               'esh10', 'esm10', 'esu10', 'esz10',
               'esh11', 'esm11', 'esu11', 'esz11',
               'esh12', 'esm12', 'esu12', 'esz12']
        te3 = ['esh13', 'esm13', 'esu13', 'esz13']

        tr4 = ['esh09', 'esm09', 'esu09', 'esz09',
               'esh10', 'esm10', 'esu10', 'esz10',
               'esh11', 'esm11', 'esu11', 'esz11',
               'esh12', 'esm12', 'esu12', 'esz12',
               'esh13', 'esm13', 'esu13', 'esz13']
        te4 = ['esh14', 'esm14', 'esu14', 'esz14']

        tr5 = ['esh10', 'esm10', 'esu10', 'esz10',
               'esh11', 'esm11', 'esu11', 'esz11',
               'esh12', 'esm12', 'esu12', 'esz12',
               'esh13', 'esm13', 'esu13', 'esz13',
               'esh14', 'esm14', 'esu14', 'esz14']
        te5 = ['esh15', 'esm15', 'esu15', 'esz15']

        tr6 = ['esh11', 'esm11', 'esu11', 'esz11',
               'esh12', 'esm12', 'esu12', 'esz12',
               'esh13', 'esm13', 'esu13', 'esz13',
               'esh14', 'esm14', 'esu14', 'esz14',
               'esh15', 'esm15', 'esu15', 'esz15']
        te6 = ['esh16', 'esm16', 'esu16', 'esz16']

        tr7 = ['esh12', 'esm12', 'esu12', 'esz12',
               'esh13', 'esm13', 'esu13', 'esz13',
               'esh14', 'esm14', 'esu14', 'esz14',
               'esh15', 'esm15', 'esu15', 'esz15',
               'esh16', 'esm16', 'esu16', 'esz16']
        te7 = ['esh17', 'esm17', 'esu17', 'esz17']

        tr8 = ['esh13', 'esm13', 'esu13', 'esz13',
               'esh14', 'esm14', 'esu14', 'esz14',
               'esh15', 'esm15', 'esu15', 'esz15',
               'esh16', 'esm16', 'esu16', 'esz16',
               'esh17', 'esm17', 'esu17', 'esz17']
        te8 = ['esh18', 'esm18', 'esu18', 'esz18']

        tr9 = ['esh14', 'esm14', 'esu14', 'esz14',
               'esh15', 'esm15', 'esu15', 'esz15',
               'esh16', 'esm16', 'esu16', 'esz16',
               'esh17', 'esm17', 'esu17', 'esz17',
               'esh18', 'esm18', 'esu18', 'esz18']
        te9 = ['esh19', 'esm19', 'esu19', 'esz19']

        tr10 = ['esh15', 'esm15', 'esu15', 'esz15',
                'esh16', 'esm16', 'esu16', 'esz16',
                'esh17', 'esm17', 'esu17', 'esz17',
                'esh18', 'esm18', 'esu18', 'esz18',
                'esh19', 'esm19', 'esu19', 'esz19']
        te10 = ['esh20', 'esm20', 'esu20', 'esz20']

        tr11 = ['esh16', 'esm16', 'esu16', 'esz16',
                'esh17', 'esm17', 'esu17', 'esz17',
                'esh18', 'esm18', 'esu18', 'esz18',
                'esh19', 'esm19', 'esu19', 'esz19',
                'esh20', 'esm20', 'esu20', 'esz20']
        te11 = ['esh21', 'esm21', 'esu21', 'esz21']

        tr12 = ['esh17', 'esm17', 'esu17', 'esz17',
                'esh18', 'esm18', 'esu18', 'esz18',
                'esh19', 'esm19', 'esu19', 'esz19',
                'esh20', 'esm20', 'esu20', 'esz20',
                'esh21', 'esm21', 'esu21', 'esz21']
        te12 = ['esh22']

        return tr1, te1, tr2, te2, tr3, te3, tr4, te4, \
               tr5, te5, tr6, te6, tr7, te7, tr8, te8, \
               tr9, te9, tr10, te10, tr11, te11, tr12, te12
