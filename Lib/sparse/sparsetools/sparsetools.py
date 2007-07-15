# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.32
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _sparsetools
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types




def csrtocsc(*args):
  """
    csrtocsc(int n_row, int n_col, int Ap, int Aj, int Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bi, std::vector<(int)> Bx)
    csrtocsc(int n_row, int n_col, int Ap, int Aj, long Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bi, std::vector<(long)> Bx)
    csrtocsc(int n_row, int n_col, int Ap, int Aj, float Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bi, std::vector<(float)> Bx)
    csrtocsc(int n_row, int n_col, int Ap, int Aj, double Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bi, std::vector<(double)> Bx)
    csrtocsc(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(npy_cfloat)> Bx)
    csrtocsc(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(npy_cdouble)> Bx)
    """
  return _sparsetools.csrtocsc(*args)

def csctocsr(*args):
  """
    csctocsr(int n_row, int n_col, int Ap, int Ai, int Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(int)> Bx)
    csctocsr(int n_row, int n_col, int Ap, int Ai, long Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(long)> Bx)
    csctocsr(int n_row, int n_col, int Ap, int Ai, float Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(float)> Bx)
    csctocsr(int n_row, int n_col, int Ap, int Ai, double Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(double)> Bx)
    csctocsr(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_cfloat)> Bx)
    csctocsr(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_cdouble)> Bx)
    """
  return _sparsetools.csctocsr(*args)

def csrtocoo(*args):
  """
    csrtocoo(int n_row, int n_col, int Ap, int Aj, int Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(int)> Bx)
    csrtocoo(int n_row, int n_col, int Ap, int Aj, long Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(long)> Bx)
    csrtocoo(int n_row, int n_col, int Ap, int Aj, float Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(float)> Bx)
    csrtocoo(int n_row, int n_col, int Ap, int Aj, double Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(double)> Bx)
    csrtocoo(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(npy_cfloat)> Bx)
    csrtocoo(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(npy_cdouble)> Bx)
    """
  return _sparsetools.csrtocoo(*args)

def csctocoo(*args):
  """
    csctocoo(int n_row, int n_col, int Ap, int Ai, int Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(int)> Bx)
    csctocoo(int n_row, int n_col, int Ap, int Ai, long Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(long)> Bx)
    csctocoo(int n_row, int n_col, int Ap, int Ai, float Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(float)> Bx)
    csctocoo(int n_row, int n_col, int Ap, int Ai, double Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(double)> Bx)
    csctocoo(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(npy_cfloat)> Bx)
    csctocoo(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(npy_cdouble)> Bx)
    """
  return _sparsetools.csctocoo(*args)

def cootocsr(*args):
  """
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, int Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(int)> Bx)
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, long Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(long)> Bx)
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, float Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(float)> Bx)
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, double Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(double)> Bx)
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, npy_cfloat Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_cfloat)> Bx)
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, npy_cdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_cdouble)> Bx)
    """
  return _sparsetools.cootocsr(*args)

def cootocsc(*args):
  """
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, int Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(int)> Bx)
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, long Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(long)> Bx)
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, float Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(float)> Bx)
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, double Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(double)> Bx)
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, npy_cfloat Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(npy_cfloat)> Bx)
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, npy_cdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(npy_cdouble)> Bx)
    """
  return _sparsetools.cootocsc(*args)

def csrmucsr(*args):
  """
    csrmucsr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bj, int Bx, std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(int)> Cx)
    csrmucsr(int n_row, int n_col, int Ap, int Aj, long Ax, int Bp, 
        int Bj, long Bx, std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(long)> Cx)
    csrmucsr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    csrmucsr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    csrmucsr(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        int Bp, int Bj, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cfloat)> Cx)
    csrmucsr(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        int Bp, int Bj, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cdouble)> Cx)
    """
  return _sparsetools.csrmucsr(*args)

def cscmucsc(*args):
  """
    cscmucsc(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bi, int Bx, std::vector<(int)> Cp, std::vector<(int)> Ci, 
        std::vector<(int)> Cx)
    cscmucsc(int n_row, int n_col, int Ap, int Ai, long Ax, int Bp, 
        int Bi, long Bx, std::vector<(int)> Cp, std::vector<(int)> Ci, 
        std::vector<(long)> Cx)
    cscmucsc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(float)> Cx)
    cscmucsc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(double)> Cx)
    cscmucsc(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        int Bp, int Bi, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cfloat)> Cx)
    cscmucsc(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        int Bp, int Bi, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cdouble)> Cx)
    """
  return _sparsetools.cscmucsc(*args)

def csrmux(*args):
  """
    csrmux(int n_row, int n_col, int Ap, int Aj, int Ax, int Xx, 
        std::vector<(int)> Yx)
    csrmux(int n_row, int n_col, int Ap, int Aj, long Ax, long Xx, 
        std::vector<(long)> Yx)
    csrmux(int n_row, int n_col, int Ap, int Aj, float Ax, float Xx, 
        std::vector<(float)> Yx)
    csrmux(int n_row, int n_col, int Ap, int Aj, double Ax, double Xx, 
        std::vector<(double)> Yx)
    csrmux(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        npy_cfloat Xx, std::vector<(npy_cfloat)> Yx)
    csrmux(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        npy_cdouble Xx, std::vector<(npy_cdouble)> Yx)
    """
  return _sparsetools.csrmux(*args)

def cscmux(*args):
  """
    cscmux(int n_row, int n_col, int Ap, int Ai, int Ax, int Xx, 
        std::vector<(int)> Yx)
    cscmux(int n_row, int n_col, int Ap, int Ai, long Ax, long Xx, 
        std::vector<(long)> Yx)
    cscmux(int n_row, int n_col, int Ap, int Ai, float Ax, float Xx, 
        std::vector<(float)> Yx)
    cscmux(int n_row, int n_col, int Ap, int Ai, double Ax, double Xx, 
        std::vector<(double)> Yx)
    cscmux(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        npy_cfloat Xx, std::vector<(npy_cfloat)> Yx)
    cscmux(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        npy_cdouble Xx, std::vector<(npy_cdouble)> Yx)
    """
  return _sparsetools.cscmux(*args)

def csr_elmul_csr(*args):
  """
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bj, int Bx, std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(int)> Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, long Ax, int Bp, 
        int Bj, long Bx, std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(long)> Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        int Bp, int Bj, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cfloat)> Cx)
    csr_elmul_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        int Bp, int Bj, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cdouble)> Cx)
    """
  return _sparsetools.csr_elmul_csr(*args)

def csr_eldiv_csr(*args):
  """
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bj, int Bx, std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(int)> Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, long Ax, int Bp, 
        int Bj, long Bx, std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(long)> Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        int Bp, int Bj, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cfloat)> Cx)
    csr_eldiv_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        int Bp, int Bj, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cdouble)> Cx)
    """
  return _sparsetools.csr_eldiv_csr(*args)

def csr_plus_csr(*args):
  """
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bj, int Bx, std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(int)> Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, long Ax, int Bp, 
        int Bj, long Bx, std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(long)> Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        int Bp, int Bj, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cfloat)> Cx)
    csr_plus_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        int Bp, int Bj, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cdouble)> Cx)
    """
  return _sparsetools.csr_plus_csr(*args)

def csr_minus_csr(*args):
  """
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, int Ax, int Bp, 
        int Bj, int Bx, std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(int)> Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, long Ax, int Bp, 
        int Bj, long Bx, std::vector<(int)> Cp, std::vector<(int)> Cj, 
        std::vector<(long)> Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        int Bp, int Bj, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cfloat)> Cx)
    csr_minus_csr(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        int Bp, int Bj, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cdouble)> Cx)
    """
  return _sparsetools.csr_minus_csr(*args)

def csc_elmul_csc(*args):
  """
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bi, int Bx, std::vector<(int)> Cp, std::vector<(int)> Ci, 
        std::vector<(int)> Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, long Ax, int Bp, 
        int Bi, long Bx, std::vector<(int)> Cp, std::vector<(int)> Ci, 
        std::vector<(long)> Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(float)> Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(double)> Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        int Bp, int Bi, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cfloat)> Cx)
    csc_elmul_csc(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        int Bp, int Bi, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cdouble)> Cx)
    """
  return _sparsetools.csc_elmul_csc(*args)

def csc_eldiv_csc(*args):
  """
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bi, int Bx, std::vector<(int)> Cp, std::vector<(int)> Ci, 
        std::vector<(int)> Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, long Ax, int Bp, 
        int Bi, long Bx, std::vector<(int)> Cp, std::vector<(int)> Ci, 
        std::vector<(long)> Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(float)> Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(double)> Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        int Bp, int Bi, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cfloat)> Cx)
    csc_eldiv_csc(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        int Bp, int Bi, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cdouble)> Cx)
    """
  return _sparsetools.csc_eldiv_csc(*args)

def csc_plus_csc(*args):
  """
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bi, int Bx, std::vector<(int)> Cp, std::vector<(int)> Ci, 
        std::vector<(int)> Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, long Ax, int Bp, 
        int Bi, long Bx, std::vector<(int)> Cp, std::vector<(int)> Ci, 
        std::vector<(long)> Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(float)> Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(double)> Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        int Bp, int Bi, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cfloat)> Cx)
    csc_plus_csc(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        int Bp, int Bi, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cdouble)> Cx)
    """
  return _sparsetools.csc_plus_csc(*args)

def csc_minus_csc(*args):
  """
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, int Ax, int Bp, 
        int Bi, int Bx, std::vector<(int)> Cp, std::vector<(int)> Ci, 
        std::vector<(int)> Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, long Ax, int Bp, 
        int Bi, long Bx, std::vector<(int)> Cp, std::vector<(int)> Ci, 
        std::vector<(long)> Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(float)> Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(double)> Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        int Bp, int Bi, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cfloat)> Cx)
    csc_minus_csc(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        int Bp, int Bi, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cdouble)> Cx)
    """
  return _sparsetools.csc_minus_csc(*args)

def spdiags(*args):
  """
    spdiags(int n_row, int n_col, int n_diag, int offsets, int diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(int)> Ax)
    spdiags(int n_row, int n_col, int n_diag, int offsets, long diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(long)> Ax)
    spdiags(int n_row, int n_col, int n_diag, int offsets, float diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(float)> Ax)
    spdiags(int n_row, int n_col, int n_diag, int offsets, double diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(double)> Ax)
    spdiags(int n_row, int n_col, int n_diag, int offsets, npy_cfloat diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(npy_cfloat)> Ax)
    spdiags(int n_row, int n_col, int n_diag, int offsets, npy_cdouble diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(npy_cdouble)> Ax)
    """
  return _sparsetools.spdiags(*args)

def csrtodense(*args):
  """
    csrtodense(int n_row, int n_col, int Ap, int Aj, int Ax, int Mx)
    csrtodense(int n_row, int n_col, int Ap, int Aj, long Ax, long Mx)
    csrtodense(int n_row, int n_col, int Ap, int Aj, float Ax, float Mx)
    csrtodense(int n_row, int n_col, int Ap, int Aj, double Ax, double Mx)
    csrtodense(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        npy_cfloat Mx)
    csrtodense(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        npy_cdouble Mx)
    """
  return _sparsetools.csrtodense(*args)

def densetocsr(*args):
  """
    densetocsr(int n_row, int n_col, int Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(int)> Ax)
    densetocsr(int n_row, int n_col, long Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(long)> Ax)
    densetocsr(int n_row, int n_col, float Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(float)> Ax)
    densetocsr(int n_row, int n_col, double Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(double)> Ax)
    densetocsr(int n_row, int n_col, npy_cfloat Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(npy_cfloat)> Ax)
    densetocsr(int n_row, int n_col, npy_cdouble Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(npy_cdouble)> Ax)
    """
  return _sparsetools.densetocsr(*args)

def sort_csr_indices(*args):
  """
    sort_csr_indices(int n_row, int n_col, int Ap, int Aj, int Ax)
    sort_csr_indices(int n_row, int n_col, int Ap, int Aj, long Ax)
    sort_csr_indices(int n_row, int n_col, int Ap, int Aj, float Ax)
    sort_csr_indices(int n_row, int n_col, int Ap, int Aj, double Ax)
    sort_csr_indices(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax)
    sort_csr_indices(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax)
    """
  return _sparsetools.sort_csr_indices(*args)

def sort_csc_indices(*args):
  """
    sort_csc_indices(int n_row, int n_col, int Ap, int Ai, int Ax)
    sort_csc_indices(int n_row, int n_col, int Ap, int Ai, long Ax)
    sort_csc_indices(int n_row, int n_col, int Ap, int Ai, float Ax)
    sort_csc_indices(int n_row, int n_col, int Ap, int Ai, double Ax)
    sort_csc_indices(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax)
    sort_csc_indices(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax)
    """
  return _sparsetools.sort_csc_indices(*args)

def sum_csr_duplicates(*args):
  """
    sum_csr_duplicates(int n_row, int n_col, int Ap, int Aj, int Ax)
    sum_csr_duplicates(int n_row, int n_col, int Ap, int Aj, long Ax)
    sum_csr_duplicates(int n_row, int n_col, int Ap, int Aj, float Ax)
    sum_csr_duplicates(int n_row, int n_col, int Ap, int Aj, double Ax)
    sum_csr_duplicates(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax)
    sum_csr_duplicates(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax)
    """
  return _sparsetools.sum_csr_duplicates(*args)

def sum_csc_duplicates(*args):
  """
    sum_csc_duplicates(int n_row, int n_col, int Ap, int Ai, int Ax)
    sum_csc_duplicates(int n_row, int n_col, int Ap, int Ai, long Ax)
    sum_csc_duplicates(int n_row, int n_col, int Ap, int Ai, float Ax)
    sum_csc_duplicates(int n_row, int n_col, int Ap, int Ai, double Ax)
    sum_csc_duplicates(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax)
    sum_csc_duplicates(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax)
    """
  return _sparsetools.sum_csc_duplicates(*args)

