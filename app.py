from config import config
import redis
import os
import json

NUM_DBS = 15 # This is the maximum number of DBs redis can have
master_data = {} # This will hold the entire Redis DB data in key-list-key format

'''
src_dst: Source/Destination
'''
def get_client(src_dst:str = "Source", db:int = 0):
    return redis.StrictRedis(
            host=config[src_dst]['Host'],
            port=config[src_dst]['Port'],
            ssl=config[src_dst].get('SSL', False),
            password=config[src_dst].get('Password', None),
            db=db
    )

# This fetches the entire redis database
def get_data():

    for x in range(0, NUM_DBS):

        # Create DB Entry in master_data variable
        master_data[x] = []

        # Initiate redis client and fetch all keys in the DB 'x'
        client = get_client('Source', x)
        print(client, client.ping())
        keys = client.keys('*')
        print(keys)
        pass

        if keys:
            for k in keys:

                # Skip unsupported keys
                if ":" in str(k):
                    continue

                # Get the key:value pair
                k = k.decode('UTF-8')
                val = client.get(k).decode('UTF-8')

                # Try to convert to JSON
                try:
                    val = json.loads(val)
                except:
                    pass
                
                # Finally append the key:value pair in the master_data Dictionary
                master_data[x].append({'key': k, 'val': val})
    
    return True

# This restores the entire redis database
def set_data():

    for x in range(0, NUM_DBS):

        # If the DB index value in master_data dictionary is empty, skip
        if not master_data[x]:
            continue
        
        # Initiate redis client with the DB number
        client = get_client('Destination', x)

        # Iterate the master_data dictionary index
        for k in master_data[x]:

            key = k['key']
            val = k['val']

            # Try to convert from JSON
            try:
                val = json.dumps(val)
            except:
                pass
            
            # Finally set the key in redis DB
            client.set(key, val)

if __name__=="__main__":
    if get_data():
        set_data()
