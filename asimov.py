try:
    import sys
    sys.path.append('/home')
except ModuleNotFoundError:
    ...


print(*sys.path, sep='\n')
