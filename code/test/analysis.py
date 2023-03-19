import r2pipe

def r2analysis(bin_file):
    r2 = r2pipe.open(bin_file)
    # r2.cmd('ood') # open binary for debugging
    # r2.cmd('dc') # run debugger
    print(r2.cmd('aa')) # analyze all
    print(r2.cmd('afl')) # list functions
    r2.cmd('pdf @ main') # disassemble main
    r2.cmd('VV') # visualize program
    r2.cmd('s sym.imp.*') # search for imports
    r2.cmd('iz') # list strings
    r2.cmd('izz') # list strings in binary
    r2.quit()

r2analysis('/bin/ls')
