import numpy as np
from scipy.optimize import curve_fit

################################################################################
# First let's define a function that will perform a line fit to some set
# of data points, using standard python functions.
#
# We want this function to also return the line fit so you can just plot it
# over your data points
################################################################################

def quadratic_func(x,a,b,c): 
     return a*x**2 + b*x + c

def linear_func(x,b,m): 
     return m*x+b

def linear_fit_to_data(xpts, ypts, yerr, starting_parameters=[1.0, 1.0], verbose=False):

  print('Fit with f(x)=mx+b')

  popt, pcov = curve_fit(linear_func, xpts, ypts, p0=starting_parameters, sigma=yerr, absolute_sigma=True)

  #print(popt, pcov)

  slope = popt[1]
  slope_uncert = np.sqrt(pcov[1][1])

  intercept = popt[0]
  intercept_uncert = np.sqrt(pcov[0][0])

  fit_xpts = np.linspace(min(xpts),max(xpts),100)
  fit_ypts = linear_func(fit_xpts, intercept, slope)

  # Calculate a chi square value 
  chi2 = ((((slope*xpts + intercept) - ypts)**2)/(yerr**2)).sum()
  ndof = len(xpts) - 2

  if verbose:
      print('slope = {0:.3} +/- {1:.3}\nintercept = {2:.3} +/- {3:.3}'.format(slope,slope_uncert, intercept, intercept_uncert))
      print('Chi2 = {0:.3f}  #dof = {1}'.format(chi2, ndof))


  return slope, slope_uncert, intercept, intercept_uncert, fit_xpts, fit_ypts, chi2, ndof

################################################################################
def quadratic_fit_to_data(xpts, ypts, yerr, starting_parameters=[1.0, 1.0, 1.0], verbose=False):

  print('Fit with f(x)=ax^2 + bx + c')

  popt, pcov = curve_fit(quadratic_func, xpts, ypts, p0=starting_parameters, sigma=yerr, absolute_sigma=True)

  #print(popt, pcov)

  a = popt[0]
  a_uncert = np.sqrt(pcov[0][0])

  b = popt[1]
  b_uncert = np.sqrt(pcov[1][1])

  c = popt[2]
  c_uncert = np.sqrt(pcov[2][2])

  fit_xpts = np.linspace(min(xpts),max(xpts),100)
  fit_ypts = quadratic_func(fit_xpts,a,b,c)

  # Calculate a chi square value 
  chi2 = ((((qudratic_func(xptsa,b,c) - ypts)**2)/(yerr**2)).sum()
  ndof = len(xpts) - 2

  if verbose:
      print('a = {0:.3} +/- {1:.3}\nb = {2:.3} +/- {3:.3}\nc = {4:.3} +/- {5:.3}'.format(a,a_uncert, b, c_uncert, b, c_uncert))
      print('Chi2 = {0:.3f}  #dof = {1}'.format(chi2, ndof))


  return a, a_uncert, b, c_uncert, b, c_uncert, fit_xpts, fit_ypts, chi2, ndof

