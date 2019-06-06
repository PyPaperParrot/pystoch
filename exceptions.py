#exceptions for SDE parameters

def _check_positive_value(val):
    if val <= 0:
        raise ValueError('Value must be positive')

def _non_negative_value(val):
    if val < 0:
        raise ValueError('Value must be nonnegative')

def _check_nSteps(val):
    if not isinstance(val, int):
        raise TypeError('Value must be integer')
    _check_positive_value(val)

def _check_params(T, nSteps, t_0):
    _non_negative_value(T)
    _non_negative_value(t_0)
    _check_nSteps(nSteps)
