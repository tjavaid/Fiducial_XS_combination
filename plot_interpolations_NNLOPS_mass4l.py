import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
#x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
#y = np.sin(x)
#tck = interpolate.splrep(x, y, s=0)
#xnew = np.arange(0, 2*np.pi, np.pi/50)
#ynew = interpolate.splev(xnew, tck, der=0)
#plt.figure()
#plt.plot(x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')
#plt.legend(['Linear', 'Cubic Spline', 'True'])
#plt.axis([-0.05, 6.33, -1.05, 1.05])
#plt.title('Cubic-spline interpolation')
#plt.show()
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
    print acc_ggH_powheg['ggH_NNLOPS_JHUgen_125_2e2mu_mass4l_genbin0']
#    lists = sorted(acc_ggH_powheg.items())
#    #x, y = zip(*acc_ggH_powheg)
#    x, y = zip(*lists)
#    plt.plot(x, y)
#    plt.show()
   # print acc_ggH_powheg['ggH_NNLOPS_JHUgen_'+mass+'_'+channel+'_mass4l_genbin0']
    pdfunc_ggH_powheg = _temp.pdfUncert
    qcdunc_ggH_powheg = _temp.qcdUncert
# ggH_NNLOPS_JHUgen_126_2e2mu_mass4l_genbin0
#from scipy import interpolate
#
#def f(x):
    #x_points = [ 0, 1, 2, 3, 4, 5]
    #x_points = [124, 125, 126]
    points=['o',',','v','s']
    #x_points = ['124', '125', '125.38','126']
    x_points = ['125', '125.38'] #NNLOPS
    channels=['4mu','2e2mu','4e','4l']
    #y_points = [12,14,22,39,58,77]
    #y_points = [acc_ggH_powheg['ggH_NNLOPS_JHUgen_124_2e2mu_mass4l_genbin0'],acc_ggH_powheg['ggH_NNLOPS_JHUgen_125_2e2mu_mass4l_genbin0'],acc_ggH_powheg['ggH_NNLOPS_JHUgen_126_2e2mu_mass4l_genbin0']]   #  [12,14,22,39,58,77]
    for channel in channels:
	#thread='ggH_NNLOPS_JHUgen_'+str(x)+'_'+channel+'_mass4l_genbin0'
	#acceptance[thread]=0.0
        #y_points = [acc_ggH_powheg['ggH_NNLOPS_JHUgen_124_'+channel+'_mass4l_genbin0'],acc_ggH_powheg['ggH_NNLOPS_JHUgen_125_'+channel+'_mass4l_genbin0'],acc_ggH_powheg['ggH_NNLOPS_JHUgen_126_'+channel+'_mass4l_genbin0']]   #  [12,14,22,39,58,77]
        y_points = [acc_ggH_powheg['ggH_NNLOPS_JHUgen_125_'+channel+'_mass4l_genbin0'],acc_ggH_powheg['ggH_NNLOPS_JHUgen_125.38_'+channel+'_mass4l_genbin0']]   #  [12,14,22,39,58,77]
	print "channel is ..  ", channel
        print "y_points are,,,,,,,,,,,,,,," ,  y_points

#	plt.plot(norm_chi2,label=sigPDF+','+bkgPDF+'('+region+')')
	#plt.plot(y_points,label=channel)
	#plt.plot(x_points,y_points,label=channel)
	plt.plot(x_points,y_points,label=channel,marker = 'o')
	plt.xlabel('Higgs mass points (GeV)');
	plt.ylabel('Acceptance (NNLOPS)')
	plt.legend(loc='upper right')
    #plot='Loose_'+region+'_normalizedChi2_2502.png'
    #plot='Acceptancee_'+channel+'_ggH.png'
    plot='Acceptancee_'+channel+'_NNLOPS.png'
    #plt.savefig('normalizedChi2plots/'+plot,bbox_inches="tight")
    plt.savefig(plot,bbox_inches="tight")
    plt.gcf().clear()
#    fig, ax = plt.subplots(figsize=(10, 6))
#    ax.plot(x_points, y_points)





#	dictionary = {channel: y_points}
#	print "dictionary is ... ", dictionary
##	lists = sorted(dictionary.items())
#	#print "lists are ", lists
#	#plt.plot(list(dictionary.keys()),list(dictionary.values()))
#
#	w=1;
##	x_axis = np.arange(0, len(out.keys())*w, w) 
##
#	fig, ax = plt.subplots(1)
##	#ax.bar(x_axis, out.values(), width = w, color='g', align='center')
#	ax.bar(channels, list(dictionary.values()), width = w, color='g', align='center')
#	ax.set_xticks(channels)
#	ax.set_xticklabels(list(dictionary.keys()), rotation=90)
#	plt.show()
    #x, y = zip(*acc_ggH_powheg)
#        x, y = zip(*lists)
#        plt.plot(x, y)
#        plt.show()
    #tck = interpolate.splrep(x_points, y_points)
#        tck = interpolate.splrep(x_points, y_points, k=2)
#	thread='ggH_NNLOPS_JHUgen_'+str(x)+'_'+channel+'_mass4l_genbin0'
#	print 'the thread is .. ', thread
#    #with open('accUnc_mass4l.py', 'w') as f:
#	#acceptance[thread]=interpolate.splev(x, tck)
#	acceptance[thread]=float(interpolate.splev(x, tck))
#	acc_ggH_powheg.update(acceptance)
#        #with open('test.py', 'w') as f:
#        with open('accUnc_mass4l.py', 'w') as f:
#            print "going write interpolated values   "
#        #f.write('acc = '+str(acceptance)+' \n')
#            #f.write('acc = '+str(interpolate.splev(x, tck))+' \n')
##	    acc.update(acceptance)
#            #f.write('acc = '+str(acceptance)+' \n')
#            f.write('acc = '+str(acc_ggH_powheg)+' \n')
#            f.write('qcdUncert = '+str(qcdunc_ggH_powheg)+' \n')
#            f.write('pdfUncert = '+str(pdfunc_ggH_powheg)+' \n')
#            #f.write(acc.update (str(acceptance)))
#    #        return interpolate.splev(x, tck)
#
#    return interpolate.splev(x, tck)
    return 1;
value= f(True);
#value= f(125)
print ("the value is ", value)
