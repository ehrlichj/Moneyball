import math

from numpy.core.numeric import NaN
class Baseball_Node:

    def __init__(self, team, year, league, rs, ra, w, obp, slg, oobp, oslg, playoff):
        self.team_id = team + str(year)
        self.league = league
        self.rs = rs
        self.ra = ra
        self.w = w
        self.obp = obp
        self.slg = slg
        self.oobp = oobp
        self.oslg = oslg
        self.rdiff = rs-ra
        if(playoff == 0):
            self.playoff = -1
        else:
            self.playoff = 1
        self.pred_playoff = None

    def getEuclideanDistance(self, other):
        ret = math.sqrt((self.slg - other.slg)**2 + (self.oslg - other.oslg)**2)
        return ret



