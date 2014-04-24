"""This script should contain the default parameters for any given project when importing BEM-solver text data."""

#################################################################################
################################# From setDC  ###################################
#################################################################################
trap = 'C:\\Python27\\trap_simulation_software\\data\\temporary_full.pkl' # note that this is defined in project_parameters as well
multipoleControls = False         # sets the control parameters to be the U's (true), or the alpha parameters
regularize = True                 # determining whether the output is to be regularized or not; also in project_parameters as reg
# (by regularization I mean minimizing the norm of el with addition of vectors belonging to the kernel of tf.config.multipoleCoefficients)
frequencyRF = 100                 # frequency of RF drive; same as driveFrequency
E = [0,0,0]                       # Stray electric field at the ion E = [Ex,Ey.Ez] (valid if multipoleControls == True); also in project_parameters
U1,U2,U3,U4,U5 = .2,1,.2,0,0 # DC Quadrupoles that I want the trap to generate at the ion (valid if multipoleControls == True)
U1,U2,U3,U4,U5 = U1*10**-6,U2*10**-6,U3*10**-6,U4*10**-6,U5*10**-6 # rescaling
U1,U2,U3,U4,U5 = U3,U4,U2,U5,U1   # convert from convenient matlab order (U1=x**2-y**2) to mathematical order (U1=xy)
# x*y,z*y,2*z**2-x**2-y**2,z*x,x**2-y**2 (python/math) to x**2-y**2,2*z**2-x**2-y**2,x*y,z*y,x*z (matlab/experiment)
ax = -0.002                       # Mathieu alpha_x parameter (valid only if multipoleControls == False)  
az = 4.5e-3                       # Mathieu alpha_z parameter (valid only if multipoleControls == False) 
phi = 0                           # Angle of rotation of DC multipole wrt RF multipole (valid only if multipoleControls == False)

#################################################################################
################################# From ppt2  ####################################
#################################################################################
#instance config
driveAmplitude = 100     # Applied RF amplitude for ppt3 analysis
driveFrequency = 40e6    # RF frequency for ppt3 analysis
findEfield       = False # determine the stray electric field for given dc voltages
justAnalyzeTrap  = True  # do not optimize, just analyze the trap, assuming everything is ok
rfplot = '1D plots' # dimensions to plot RF with plotpot
dcplot = '1D plots' # dimensions to plot DC with plotpot


