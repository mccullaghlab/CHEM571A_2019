
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.cm as cm
import numpy as np

# define function for making figures
def define_figure(xlabel="X",ylabel="Y"):
    # setup plot parameters
    fig = plt.figure(figsize=(12,8), dpi= 80, facecolor='w', edgecolor='k')
    ax = plt.subplot(111)
    ax.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
    ax.set_xlabel(xlabel,size=20)
    ax.set_ylabel(ylabel,size=20)
    plt.tick_params(axis='both',labelsize=20)
    return fig, ax

def plot_square_matrix(square_matrix,figure_name,axes_label='',cbar_label='',plotting_cmap='bwr',v_range=None,minor_ticks=10,major_ticks=100,xlabels=[],ylabels=[]):
        """
        """
        nNodes = len(square_matrix)
        node_range = range(nNodes+1)
        fig, ax = plt.subplots()
        ax.tick_params(which='major',length=6,width=2)
        ax.tick_params(which='minor',length=3,width=1)
        ax.xaxis.set_minor_locator(MultipleLocator(minor_ticks))
        ax.xaxis.set_major_locator(MultipleLocator(major_ticks))
        ax.yaxis.set_minor_locator(MultipleLocator(minor_ticks))
        ax.yaxis.set_major_locator(MultipleLocator(major_ticks))
        if xlabels == []:
            xlabels = [str(int(x)+1) for x in temp.axes.get_xticks()[:]]
        if ylabels == []:
            ylabels = [str(int(y)+1) for y in temp.axes.get_yticks()[:]]

        if v_range != None:
                temp = plt.pcolormesh(node_range,node_range,square_matrix,cmap=plotting_cmap,vmin=v_range[0],vmax=v_range[1])
        else:
                temp = plt.pcolormesh(node_range,node_range,square_matrix,cmap=plotting_cmap)
        cb1 = plt.colorbar()
        cb1.set_label(r'%s'%(cbar_label))

        temp.axes.set_xticks(temp.axes.get_xticks(minor=True)[:]+0.5,minor=True)
        temp.axes.set_xticks(temp.axes.get_xticks()[:]+0.5)
        temp.axes.set_yticks(temp.axes.get_yticks(minor=True)[:]+0.5,minor=True)
        temp.axes.set_yticks(temp.axes.get_yticks()[:]+0.5)
        temp.axes.set_xticklabels(xlabels)
        temp.axes.set_yticklabels(ylabels)

        plt.xlim((0,nNodes))
        plt.ylim((0,nNodes))
        plt.xlabel(axes_label,size=14)
        plt.ylabel(axes_label,size=14)
        ax.set_aspect('equal')
        plt.tight_layout()
        #plt.plot(np.arange(0,nNodes,0.01),np.arange(0,nNodes,0.01),'--',lw=2,color='k')
        plt.savefig(figure_name,dpi=600,transparent=True)
        plt.close()

def plot_square_matrix_inline(square_matrix,axes_label='',cbar_label='',plotting_cmap='bwr',v_range=None,minor_ticks=10,major_ticks=100):
        """
        """
        nNodes = len(square_matrix)
        node_range = range(nNodes+1)
        fig, ax = plt.subplots()
        ax.tick_params(which='major',length=6,width=2)
        ax.tick_params(which='minor',length=3,width=1)
        ax.xaxis.set_minor_locator(MultipleLocator(minor_ticks))
        ax.xaxis.set_major_locator(MultipleLocator(major_ticks))
        ax.yaxis.set_minor_locator(MultipleLocator(minor_ticks))
        ax.yaxis.set_major_locator(MultipleLocator(major_ticks))

        if v_range != None:
                temp = plt.pcolormesh(node_range,node_range,square_matrix,cmap=plotting_cmap,vmin=v_range[0],vmax=v_range[1])
        else:
                temp = plt.pcolormesh(node_range,node_range,square_matrix,cmap=plotting_cmap)
        cb1 = plt.colorbar()
        cb1.set_label(r'%s'%(cbar_label))

        xlabels = [str(int(x)+1) for x in temp.axes.get_xticks()[:]]
        ylabels = [str(int(y)+1) for y in temp.axes.get_yticks()[:]]
        temp.axes.set_xticks(temp.axes.get_xticks(minor=True)[:]+0.5,minor=True)
        temp.axes.set_xticks(temp.axes.get_xticks()[:]+0.5)
        temp.axes.set_yticks(temp.axes.get_yticks(minor=True)[:]+0.5,minor=True)
        temp.axes.set_yticks(temp.axes.get_yticks()[:]+0.5)
        temp.axes.set_xticklabels(xlabels)
        temp.axes.set_yticklabels(ylabels)

        plt.xlim((0,nNodes))
        plt.ylim((0,nNodes))
        plt.xlabel(axes_label,size=14)
        plt.ylabel(axes_label,size=14)
        ax.set_aspect('equal')
        plt.tight_layout()
        plt.plot(np.arange(0,nNodes,0.01),np.arange(0,nNodes,0.01),'--',lw=2,color='k')


def plot_igps_sq_mat(sq_data, figure_name, cbar_label, vmin=0.000001, vmax=1.0, cmap=plt.cm.inferno_r):

#    cbar_label = 'Hessian'

    plotting_cmap = cmap
    plotting_cmap.set_under(color='white')

    tick_labels = list(range(50,253,50)) + list(range(50,201,50))
    tick_labels = [str(x) for x in tick_labels]
    tick_locations = np.array(list(range(50,253,50)) + list(range(304,455,50))) + 0.5
    minor_tick_locations = np.array(list(range(0,254,10)) + list(range(254,445,10))) + 0.5

    nNodes = len(sq_data)
    node_range = range(nNodes+1)
    fig, ax = plt.subplots()
    ax.tick_params(which='major',length=6,width=2)
    ax.tick_params(which='minor',length=3,width=1)

    temp = plt.pcolormesh(node_range,node_range,sq_data,cmap=plotting_cmap,vmin=vmin,vmax=vmax)
    cb1 = plt.colorbar()
    cb1.set_label(r'%s'%(cbar_label))
    temp.axes.set_yticks(tick_locations)
    temp.axes.set_yticks(minor_tick_locations,minor=True)
    temp.axes.set_yticklabels(tick_labels)
    temp.axes.set_xticks(tick_locations)
    temp.axes.set_xticks(minor_tick_locations,minor=True)
    temp.axes.set_xticklabels(tick_labels)

    ## plot segnaming boundary beside the segname labels
    plt.plot([0,454],[-65,-65],'k--',lw=1,clip_on=False)
    plt.plot([253.5,253.5],[-60,-70],'k-',lw=1.5,clip_on=False)
    plt.plot([-60,-60],[0,454],'k--',lw=1,clip_on=False)
    plt.plot([-55,-65],[253.5,253.5],'k-',lw=1.5,clip_on=False)

    ## segnaming beside/underneath axes
    plt.xlabel('Residue Index',size=14,labelpad=25)
    plt.ylabel('Residue Index',size=14,labelpad=25)
    plt.text(127.0,-55.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(354.0,-55.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(-75.0,127.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)
    plt.text(-75.0,354.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)

    plt.xlim((-0.5,nNodes+0.5))
    plt.ylim((-0.5,nNodes+0.5))
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(figure_name,dpi=600,transparent=True)
    plt.close()


def plot_igps_covar(sq_data, figure_name, cbar_label, vmin=-0.5, vmax=0.5, cmap="bwr"):

#    cbar_label = 'Hessian'

    plotting_cmap = cmap

    tick_labels = list(range(50,253,50)) + list(range(50,201,50))
    #tick_labels[0] += 1
    tick_labels = [str(x) for x in tick_labels]
    tick_locations = np.array(list(range(50,253,50)) + list(range(304,455,50))) + 0.5
    minor_tick_locations = np.array(list(range(0,254,10)) + list(range(254,445,10))) + 0.5

    nNodes = len(sq_data)
    node_range = range(nNodes+1)
    fig, ax = plt.subplots()
    ax.tick_params(which='major',length=6,width=2)
    ax.tick_params(which='minor',length=3,width=1)

    temp = plt.pcolormesh(node_range,node_range,sq_data,cmap=plotting_cmap,vmin=vmin,vmax=vmax)
    cb1 = plt.colorbar()
    cb1.set_label(r'%s'%(cbar_label))
    temp.axes.set_yticks(tick_locations)
    temp.axes.set_yticks(minor_tick_locations,minor=True)
    temp.axes.set_yticklabels(tick_labels)
    temp.axes.set_xticks(tick_locations)
    temp.axes.set_xticks(minor_tick_locations,minor=True)
    temp.axes.set_xticklabels(tick_labels)

    ## plot segnaming boundary beside the segname labels
    plt.plot([0,454],[-65,-65],'k--',lw=1,clip_on=False)
    plt.plot([253.5,253.5],[-60,-70],'k-',lw=1.5,clip_on=False)
    plt.plot([-60,-60],[0,454],'k--',lw=1,clip_on=False)
    plt.plot([-55,-65],[253.5,253.5],'k-',lw=1.5,clip_on=False)

    ## segnaming beside/underneath axes
    plt.xlabel('Residue Index',size=14,labelpad=25)
    plt.ylabel('Residue Index',size=14,labelpad=25)
    plt.text(127.0,-55.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(354.0,-55.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(-75.0,127.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)
    plt.text(-75.0,354.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)

    plt.xlim((-0.5,nNodes+0.5))
    plt.ylim((-0.5,nNodes+0.5))
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(figure_name,dpi=600,transparent=True)
    plt.close()


def plot_igps_3N_covar(sq_data, figure_name, cbar_label, vmin=-0.5, vmax=0.5, cmap="bwr"):

#    cbar_label = 'Hessian'

    plotting_cmap = cmap

    tick_labels = list(range(100,759,100)) + list(range(100,603,100))
    #tick_labels[0] += 1
    tick_labels = [str(x) for x in tick_labels]
    tick_locations = np.array(list(range(100,759,100)) + list(range(859,1362,100))) + 0.5
    minor_tick_locations = np.array(list(range(0,759,50)) + list(range(809,1362,50))) + 0.5

    nNodes = len(sq_data)
    node_range = range(nNodes+1)
    fig, ax = plt.subplots()
    ax.tick_params(which='major',length=6,width=2)
    ax.tick_params(which='minor',length=3,width=1)

    temp = plt.pcolormesh(node_range,node_range,sq_data,cmap=plotting_cmap,vmin=vmin,vmax=vmax)
    cb1 = plt.colorbar()
    cb1.set_label(r'%s'%(cbar_label))
    temp.axes.set_yticks(tick_locations)
    temp.axes.set_yticks(minor_tick_locations,minor=True)
    temp.axes.set_yticklabels(tick_labels)
    temp.axes.set_xticks(tick_locations)
    temp.axes.set_xticks(minor_tick_locations,minor=True)
    temp.axes.set_xticklabels(tick_labels)

    ## plot segnaming boundary beside the segname labels
    plt.plot([0,1362],[-85,-85],'k--',lw=1,clip_on=False)
    plt.plot([759.5,759.5],[-80,-90],'k-',lw=1.5,clip_on=False)
    plt.plot([-80,-80],[0,1362],'k--',lw=1,clip_on=False)
    plt.plot([-75,-85],[759.5,759.5],'k-',lw=1.5,clip_on=False)

    ## segnaming beside/underneath axes
    plt.xlabel('Residue Index',size=14,labelpad=25)
    plt.ylabel('Residue Index',size=14,labelpad=25)
    plt.text(381.0,-105.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(1062.0,-105.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(-105.0,381.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)
    plt.text(-105.0,1062.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)

    plt.xlim((-0.5,nNodes+0.5))
    plt.ylim((-0.5,nNodes+0.5))
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(figure_name,dpi=600,transparent=True)
    plt.close()


def plot_igps_pnode(data, labels, figure_name):

    tick_labels = list(range(50,253,50)) + list(range(50,201,50))
    tick_labels = [str(x) for x in tick_labels]
    tick_locations = np.array(list(range(50,253,50)) + list(range(304,455,50))) + 0.5
    minor_tick_locations = np.array(list(range(0,254,10)) + list(range(254,445,10))) + 0.5

    nSets = data.shape[1]
    nNodes = data.shape[0]
    node_range = range(nNodes+1)
    fig, ax = plt.subplots()
    ax.tick_params(which='major',length=6,width=2)
    ax.tick_params(which='minor',length=3,width=1)

    ## plot segnaming boundary beside the segname labels
    plt.plot([0,454],[-0.75,-0.75],'k--',lw=1,clip_on=False)
    plt.plot([253.5,253.5],[-0.70,-0.80],'k-',lw=1.5,clip_on=False)

    ## segnaming beside/underneath axes
    plt.xlabel('Residue Index',size=14,labelpad=25)
    plt.ylabel("P$_{node}$",size=14,labelpad=25)
    plt.text(127.0,-1.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(354.0,-1.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center')

    ## plot data
    #for i in range(nSets):
    #    ax.plot(data[:,i],lw=2,label=labels[i])

    plt.xlim((-0.5,nNodes+0.5))
    plt.ylim((0,np.amax(data)*1.05))
    plt.legend(fontsize=14)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(figure_name,dpi=600,transparent=True)
    plt.close()


def plot_igps_3N_covar(sq_data, figure_name, cbar_label, vmin=-0.5, vmax=0.5, cmap="bwr"):

#    cbar_label = 'Hessian'

    plotting_cmap = cmap

    tick_labels = list(range(100,759,100)) + list(range(100,603,100))
    #tick_labels[0] += 1
    tick_labels = [str(x) for x in tick_labels]
    tick_locations = np.array(list(range(100,759,100)) + list(range(859,1362,100))) + 0.5
    minor_tick_locations = np.array(list(range(0,759,50)) + list(range(809,1362,50))) + 0.5

    nNodes = len(sq_data)
    node_range = range(nNodes+1)
    fig, ax = plt.subplots()
    ax.tick_params(which='major',length=6,width=2)
    ax.tick_params(which='minor',length=3,width=1)

    temp = plt.pcolormesh(node_range,node_range,sq_data,cmap=plotting_cmap,vmin=vmin,vmax=vmax)
    cb1 = plt.colorbar()
    cb1.set_label(r'%s'%(cbar_label))
    temp.axes.set_yticks(tick_locations)
    temp.axes.set_yticks(minor_tick_locations,minor=True)
    temp.axes.set_yticklabels(tick_labels)
    temp.axes.set_xticks(tick_locations)
    temp.axes.set_xticks(minor_tick_locations,minor=True)
    temp.axes.set_xticklabels(tick_labels)

    ## plot segnaming boundary beside the segname labels
    plt.plot([0,1362],[-85,-85],'k--',lw=1,clip_on=False)
    plt.plot([759.5,759.5],[-80,-90],'k-',lw=1.5,clip_on=False)
    plt.plot([-80,-80],[0,1362],'k--',lw=1,clip_on=False)
    plt.plot([-75,-85],[759.5,759.5],'k-',lw=1.5,clip_on=False)

    ## segnaming beside/underneath axes
    plt.xlabel('Residue Index',size=14,labelpad=25)
    plt.ylabel('Residue Index',size=14,labelpad=25)
    plt.text(381.0,-105.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(1062.0,-105.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(-105.0,381.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)
    plt.text(-105.0,1062.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)

    plt.xlim((-0.5,nNodes+0.5))
    plt.ylim((-0.5,nNodes+0.5))
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(figure_name,dpi=600,transparent=True)
    plt.close()


def plot_ns3_covar(sq_data, figure_name, cbar_label, vmin=-0.5, vmax=0.5, cmap="bwr"):

#    cbar_label = 'Hessian'

    plotting_cmap = cmap

    tick_labels = list(range(200,451+167,50)) 
    #tick_labels[0] += 1
    tick_labels = [str(x) for x in tick_labels]
    tick_locations = np.array(list(range(33,451,50)) ) + 0.5
    minor_tick_locations = np.array(list(range(3,451,10)) ) + 0.5

    nNodes = len(sq_data)
    node_range = range(nNodes+1)
    fig, ax = plt.subplots()
    ax.tick_params(which='major',length=6,width=2)
    ax.tick_params(which='minor',length=3,width=1)

    temp = plt.pcolormesh(node_range,node_range,sq_data,cmap=plotting_cmap,vmin=vmin,vmax=vmax)
    cb1 = plt.colorbar()
    cb1.set_label(r'%s'%(cbar_label))
    temp.axes.set_yticks(tick_locations)
    temp.axes.set_yticks(minor_tick_locations,minor=True)
    temp.axes.set_yticklabels(tick_labels)
    temp.axes.set_xticks(tick_locations)
    temp.axes.set_xticks(minor_tick_locations,minor=True)
    temp.axes.set_xticklabels(tick_labels)

    ## plot segnaming boundary beside the segname labels
#    plt.plot([0,454],[-65,-65],'k--',lw=1,clip_on=False)
#    plt.plot([253.5,253.5],[-60,-70],'k-',lw=1.5,clip_on=False)
#    plt.plot([-60,-60],[0,454],'k--',lw=1,clip_on=False)
#    plt.plot([-55,-65],[253.5,253.5],'k-',lw=1.5,clip_on=False)

    ## segnaming beside/underneath axes
    plt.xlabel('Residue Index',size=14,labelpad=25)
    plt.ylabel('Residue Index',size=14,labelpad=25)
#    plt.text(127.0,-55.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center')
#    plt.text(354.0,-55.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center')
#    plt.text(-75.0,127.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)
#    plt.text(-75.0,354.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)

    plt.xlim((-0.5,nNodes+0.5))
    plt.ylim((-0.5,nNodes+0.5))
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(figure_name,dpi=600,transparent=True)
    plt.close()


def plot_igps_3N_covar(sq_data, figure_name, cbar_label, vmin=-0.5, vmax=0.5, cmap="bwr"):

#    cbar_label = 'Hessian'

    plotting_cmap = cmap

    tick_labels = list(range(100,759,100)) + list(range(100,603,100))
    #tick_labels[0] += 1
    tick_labels = [str(x) for x in tick_labels]
    tick_locations = np.array(list(range(100,759,100)) + list(range(859,1362,100))) + 0.5
    minor_tick_locations = np.array(list(range(0,759,50)) + list(range(809,1362,50))) + 0.5

    nNodes = len(sq_data)
    node_range = range(nNodes+1)
    fig, ax = plt.subplots()
    ax.tick_params(which='major',length=6,width=2)
    ax.tick_params(which='minor',length=3,width=1)

    temp = plt.pcolormesh(node_range,node_range,sq_data,cmap=plotting_cmap,vmin=vmin,vmax=vmax)
    cb1 = plt.colorbar()
    cb1.set_label(r'%s'%(cbar_label))
    temp.axes.set_yticks(tick_locations)
    temp.axes.set_yticks(minor_tick_locations,minor=True)
    temp.axes.set_yticklabels(tick_labels)
    temp.axes.set_xticks(tick_locations)
    temp.axes.set_xticks(minor_tick_locations,minor=True)
    temp.axes.set_xticklabels(tick_labels)

    ## plot segnaming boundary beside the segname labels
    plt.plot([0,1362],[-85,-85],'k--',lw=1,clip_on=False)
    plt.plot([759.5,759.5],[-80,-90],'k-',lw=1.5,clip_on=False)
    plt.plot([-80,-80],[0,1362],'k--',lw=1,clip_on=False)
    plt.plot([-75,-85],[759.5,759.5],'k-',lw=1.5,clip_on=False)

    ## segnaming beside/underneath axes
    plt.xlabel('Residue Index',size=14,labelpad=25)
    plt.ylabel('Residue Index',size=14,labelpad=25)
    plt.text(381.0,-105.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(1062.0,-105.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(-105.0,381.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)
    plt.text(-105.0,1062.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)

    plt.xlim((-0.5,nNodes+0.5))
    plt.ylim((-0.5,nNodes+0.5))
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(figure_name,dpi=600,transparent=True)
    plt.close()


def plot_igps_pnode(data, labels, figure_name):

    tick_labels = list(range(50,253,50)) + list(range(50,201,50))
    tick_labels = [str(x) for x in tick_labels]
    tick_locations = np.array(list(range(50,253,50)) + list(range(304,455,50))) + 0.5
    minor_tick_locations = np.array(list(range(0,254,10)) + list(range(254,445,10))) + 0.5

    nSets = data.shape[1]
    nNodes = data.shape[0]
    node_range = range(nNodes+1)
    fig, ax = plt.subplots()
    ax.tick_params(which='major',length=6,width=2)
    ax.tick_params(which='minor',length=3,width=1)

    ## plot segnaming boundary beside the segname labels
    plt.plot([0,454],[-0.75,-0.75],'k--',lw=1,clip_on=False)
    plt.plot([253.5,253.5],[-0.70,-0.80],'k-',lw=1.5,clip_on=False)

    ## segnaming beside/underneath axes
    plt.xlabel('Residue Index',size=14,labelpad=25)
    plt.ylabel("P$_{node}$",size=14,labelpad=25)
    plt.text(127.0,-1.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(354.0,-1.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center')

    ## plot data
    #for i in range(nSets):
    #    ax.plot(data[:,i],lw=2,label=labels[i])

    plt.xlim((-0.5,nNodes+0.5))
    plt.ylim((0,np.amax(data)*1.05))
    plt.legend(fontsize=14)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(figure_name,dpi=600,transparent=True)
    plt.close()


def plot_igps_3N_covar(sq_data, figure_name, cbar_label, vmin=-0.5, vmax=0.5, cmap="bwr"):

#    cbar_label = 'Hessian'

    plotting_cmap = cmap

    tick_labels = list(range(100,759,100)) + list(range(100,603,100))
    #tick_labels[0] += 1
    tick_labels = [str(x) for x in tick_labels]
    tick_locations = np.array(list(range(100,759,100)) + list(range(859,1362,100))) + 0.5
    minor_tick_locations = np.array(list(range(0,759,50)) + list(range(809,1362,50))) + 0.5

    nNodes = len(sq_data)
    node_range = range(nNodes+1)
    fig, ax = plt.subplots()
    ax.tick_params(which='major',length=6,width=2)
    ax.tick_params(which='minor',length=3,width=1)

    temp = plt.pcolormesh(node_range,node_range,sq_data,cmap=plotting_cmap,vmin=vmin,vmax=vmax)
    cb1 = plt.colorbar()
    cb1.set_label(r'%s'%(cbar_label))
    temp.axes.set_yticks(tick_locations)
    temp.axes.set_yticks(minor_tick_locations,minor=True)
    temp.axes.set_yticklabels(tick_labels)
    temp.axes.set_xticks(tick_locations)
    temp.axes.set_xticks(minor_tick_locations,minor=True)
    temp.axes.set_xticklabels(tick_labels)

    ## plot segnaming boundary beside the segname labels
    plt.plot([0,1362],[-85,-85],'k--',lw=1,clip_on=False)
    plt.plot([759.5,759.5],[-80,-90],'k-',lw=1.5,clip_on=False)
    plt.plot([-80,-80],[0,1362],'k--',lw=1,clip_on=False)
    plt.plot([-75,-85],[759.5,759.5],'k-',lw=1.5,clip_on=False)

    ## segnaming beside/underneath axes
    plt.xlabel('Residue Index',size=14,labelpad=25)
    plt.ylabel('Residue Index',size=14,labelpad=25)
    plt.text(381.0,-105.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(1062.0,-105.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center')
    plt.text(-105.0,381.0,'HisF',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)
    plt.text(-105.0,1062.0,'HisH',fontsize=14,horizontalalignment='center',verticalalignment='center',rotation=90)

    plt.xlim((-0.5,nNodes+0.5))
    plt.ylim((-0.5,nNodes+0.5))
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(figure_name,dpi=600,transparent=True)
    plt.close()


