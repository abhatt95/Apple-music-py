import applemusicpy

secret_key = open('AuthKey_HMX423V2Z5.p8', 'rb').read()
key_id = 'HMX423V2Z5'
team_id = 'P748547DT7'

am = applemusicpy.AppleMusic(secret_key=secret_key, key_id=key_id, team_id=team_id)

results = am.search('travis scott', types=['albums'], limit=5)
for item in results['results']['albums']['data']:
    print(item['attributes']['name'])