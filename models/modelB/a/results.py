import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
from sklearn.metrics import r2_score, mean_squared_error, make_scorer

titles = ["NU_BBCH45", "NU_BBCH25", "NCT_BBCH99", "BT_BBCH25", "BSL_BBCH99", "NCT_BBCH45", "NCT_BBCH45", "NU_BBCH99"]

a = [0.921406754337554,0.871157756559378,0.697033590677288,0.7697999499623,0.876883252968772,0.910741926696878,
    0.784406888510471,0.908457602954056,0.900975149123671,0.949942631616182]

b = [0.741622506726051,0.356706640163534,0.728554145835911,0.213672697219693,0.794595294564355,0.715091121015586,
    0.539629886193248,0.446984927445491,0.103649790537682,0.336921185957767]

c = [0.578507694998862,0.694419769600624,0.562771252591803,0.75868415553369,0.802909710857015,0.711976876941095,
    0.736937624672442,0.58833072016384,0.773221899105283,0.725266639610835]

d = [0.888040061425376,0.704054507433796,0.815905860445904,0.801325046034972,0.919093163433395,0.573240188058745,
    0.850055123298697,0.673459021622991,0.694360167612403,0.756357035635644]

e = [0.620848761345464,0.564461948506443,0.678644046408305,-0.044931395714837,0.452886262357626,0.401269014224604,
    0.72022011674191,0.195735464823187,0.446839613538855,0.330718378599541]

f = [0.673170007449799,0.598681487564777,0.772259557335278,0.514905876635678,0.796407361640063,0.655400000855423,
    0.857305097076855,0.672423014957817,0.697442262060355,0.630797634648951]

g = [0.736433373569104,0.693393588533839,0.710026472183247,0.746543369020376,0.679731466594411,0.672766211520072,
    0.602257150294339,0.553348969675412,0.774020649890401,0.391752612963473]

h = [0.788839474295623,0.493456364800144,0.503230427354607,0.655024681715286,0.743955723670074,0.888535715139904,
    0.577165774983653,0.802540722835215,0.871970592007797,0.738736801265623]


data = [a]
data.append(b)
data.append(c)
data.append(d)
data.append(e)
data.append(f)
data.append(g)
data.append(h)
repeats = 10
idx = 0
for set in data:
    plt.plot(set, marker='o', linestyle='dashed')
    plt.xlabel('Repeat')
    plt.ylabel('Rsquarred')
    plt.title(titles[idx])
    plt.savefig(str(idx)+".jpeg")
    plt.clf()
    idx = idx + 1
