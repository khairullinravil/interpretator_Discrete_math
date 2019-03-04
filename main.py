from lexer import lexer
from lexer import parser
from expressions import *

if __name__ == '__main__':
    # s = 'x1 : RAST'                             # empty
    # s = 'x1 : NAT'                              # empty
    # s = '+ 1'                                   # (1)+
    s = '+ 1 2'                                 # 3
    # s = '+ +'                                   # mismatch
    # s = '1 +'                                   # mismatch
    # s = '+ 1 x2'                                # x2 does not exist
    # s = '+ x1 x2'                               # x1 does not exist
    # s = 'lambda x1.+ 1 3'                       # x1 does not exist
    # s = 'x1 : NAT\nlambda x1.+ 1 x2'            # x2 does not exist
    # s = 'x12 : NAT\n* 1 2'                      # 2
    # s = 'x1 : NAT\n+ x1 1'                      # + x1 1
    # s = 'x1 : NAT\n+ 1 x1'                      # (1)+ x1
    # s = 'x1 : NAT -> NAT\n+ x1 1'               # mismatch
    # s = 'x1 : NAT\nx2 : NAT\n+ x1 x2'           # + x1 x2
    # s = 'x1 : NAT\nx2 : NAT -> NAT\n+ x1 x2'    # mismatch
    # s = 'x1 : NAT -> NAT -> NAT -> NAT -> NAT\nx2 : NAT\nx1 + x2'   # x1 + x2
    # s = 'x1 : NAT\n x2 : NAT\n(lambda x1.+ x1 3)lambda x2.+ 7 6'    # 16
    # s = 'x1: NAT\n x2:NAT\n(lambda x1.+ x2 x1)2'                    # + x2 2
    # s = 'x1 : NAT\nx2 : NAT\n(lambda x1.+ x2 x1)2'                  # + x2 2
    # s = 'x1 : NAT\n(lambda x1.+ 1 x1)2'                             # 3
    # s = 'x1 : NAT -> NAT\nlambda x1.+ x1 3'                         # mismatch
    # s = 'x1 : NAT\nlambda x1.+ x1 3'                                # lambda x1.+ x1 3
    # s = 'x1 : NAT -> NAT\nlambda x1.+ 1 3'                          # 4
    # s = 'x1 : NAT\n(lambda x1.+ 1 3)2'                              # 4
    # s = 'x1 : NAT -> NAT -> NAT\n(lambda x1.x1 1 3)+'               # 4
    # s = 'x1 : NAT\n(lambda x1.x1 1 3)+'                             # mismatch

    print('input:', s, sep='\n')
    p = parser.parse(s)

    if p is not None:
        print()
        e = p.evaluate()
        print('type(p) :', type(p))
        print('      p :', p)
        print(' p.eval :', e)
        if (e != None):
            if (e.find('x') == -1):
                if ( (e[-1] != '+') & (e[-1] != '*') ):
                    print(' p.eval =', eval(e))