import os


def pypi42_dirty():
    from fabric.main import main
    from distutils.sysconfig import get_python_lib

    savedpath = os.getcwd()
    fabpath = get_python_lib() + '/pypi42/'
    os.chdir(fabpath)
    main()
    os.chdir(savedpath)


def pypi42_clean():
    from fabric.main import main
    from distutils.sysconfig import get_python_lib

    fabpath = get_python_lib() + '/pypi42/'
    fabfile = fabpath + 'fabfile.py'
    fabfile = [fabfile]
    main(fabfile)
