try:
    pass
except Exception as e:
    pass
except (SystemError,IOError) as e:
    pass
else:
    pass
finally:
    pass

# ========================
try:
    pass
except Exception,e:
    pass
except (SystemError,IOError),e:
    pass
else:
    pass
finally:
    pass
