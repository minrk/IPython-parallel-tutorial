from IPython.parallel.error import RemoteError
from IPython.parallel import Reference

def remote_iterator(view,name):
    """Return an iterator on an object living on a remote engine.
    """
    view.execute('it%s=iter(%s)' % (name,name), block=True)
    while True:
        try:
            result = view.apply_sync(lambda x: x.next(), Reference('it'+name))
        # This causes the StopIteration exception to be raised.
        except RemoteError as e:
            if e.ename == 'StopIteration':
                raise StopIteration
            else:
                raise e
        else:
            yield result

