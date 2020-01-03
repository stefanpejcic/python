import screenconnect
sc = screenconnect.ScreenConnect('http://nes.to/', auth=('user', 'pass'))

sc.server_version
sc.get_eligible_hosts()
