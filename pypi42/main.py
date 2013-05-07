def pypi42():
    from fabric.main import main
    from fabric import state
    from distutils.sysconfig import get_python_lib

    print "HELLO WORLD 42"
    print(get_python_lib())
    main()
