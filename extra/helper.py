def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


def linearSolver(x1,y1, x2,y2):
	m = (y1-y2)/(x1-x2);
	c = int(x1 - (m*y1));
	m = truncate(m, 2);
	return [m,c];

def paSolver(x1,y1, x2,y2):
	# p = xsin(a) + ycoz(a);
	# p/cos(a) - x tan(a) = y
	# 