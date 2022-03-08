import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
#
def f(True):
#def f(mass, channel):
    obsName='mass4l'
    acceptance={}
    _temp = __import__('accUnc_'+obsName, globals(), locals(), ['acc','pdfUncert','qcdUncert'], -1)
    _temp2 = __import__('accUnc_'+obsName+'_PAS', globals(), locals(), ['acc','pdfUncert','qcdUncert'], -1)
    acc_ggH_powheg = _temp.acc
    acc_ggH_powheg2 = _temp2.acc
    print acc_ggH_powheg
    print acc_ggH_powheg['ggH_powheg_JHUgen_125_2e2mu_mass4l_genbin0']
   # print acc_ggH_powheg['ggH_powheg_JHUgen_'+mass+'_'+channel+'_mass4l_genbin0']
    pdfunc_ggH_powheg = _temp.pdfUncert
    qcdunc_ggH_powheg = _temp.qcdUncert
    points=['o',',','v','s']
    x_points = ['124', '125', '125.38','126']
    channels=['4mu','2e2mu','4e','4l']
    for channel in channels:
        #y_points = [acc_ggH_powheg['ggH_powheg_JHUgen_124_'+channel+'_mass4l_genbin0'],acc_ggH_powheg['ggH_powheg_JHUgen_125_'+channel+'_mass4l_genbin0'],acc_ggH_powheg['ggH_powheg_JHUgen_126_'+channel+'_mass4l_genbin0']]   #  [12,14,22,39,58,77]
        y_points = [acc_ggH_powheg['ggH_powheg_JHUgen_124_'+channel+'_mass4l_genbin0'],acc_ggH_powheg['ggH_powheg_JHUgen_125_'+channel+'_mass4l_genbin0'],acc_ggH_powheg['ggH_powheg_JHUgen_125.38_'+channel+'_mass4l_genbin0'],acc_ggH_powheg['ggH_powheg_JHUgen_126_'+channel+'_mass4l_genbin0']]   #  [12,14,22,39,58,77]
	print "channel is ..  ", channel
        print "y_points are,,,,,,,,,,,,,,," ,  y_points

#	plt.plot(norm_chi2,label=sigPDF+','+bkgPDF+'('+region+')')
	#plt.plot(y_points,label=channel)
	#plt.plot(x_points,y_points,label=channel)
	plt.plot(x_points,y_points,label=channel,marker = 'o')
	plt.xlabel('Higgs mass points (GeV)');
	plt.ylabel('Acceptance')
	plt.legend(loc='upper right')
    #plot='Loose_'+region+'_normalizedChi2_2502.png'
    plot='Acceptancee_'+channel+'_ggH.png'
    #plt.savefig('normalizedChi2plots/'+plot,bbox_inches="tight")
    plt.savefig(plot,bbox_inches="tight")
    plt.gcf().clear()
#    return interpolate.splev(x, tck)
    return 1;
value= f(True);
#value= f(125)
print ("the value is ", value)
