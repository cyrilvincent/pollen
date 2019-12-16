import ctypes
print(ctypes.windll.kernel32)
libc = ctypes.cdll.msvcrt
print(libc.time(None))
lib = ctypes.CDLL("jakadi.dll") # windll est spécialisé pour les DLL et OleDb Windows
print(lib)
res = lib.multiplier(2,3)
print(res)
lib.dit_papa("papa")
lib.dit_papa("papa".encode('utf8'))
"""s = ctypes.c_char_p('kiwi'.encode('utf8'))
lib.jakadi(ctypes.byref(s))"""