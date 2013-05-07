import os


def pypi42():
    from fabric.main import main
    from fabric import state
    from distutils.sysconfig import get_python_lib

    print "HELLO WORLD 42"
    savedpath = os.getcwd()
    fabpath = get_python_lib() + '/pypi42'
    #os.chdir(fabpath)
    #fabfile = fabpath + 'fabfile.py'
    main(fabpath)
    #os.chdir(savedpath)
