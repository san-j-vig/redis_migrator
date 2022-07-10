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

if __name__=="__main__":
    source_client = get_client('Source')
    destination_client = get_client('Destination')
    print("Source: Pinging Redis", source_client, source_client.ping())
    print("Destination: Pinging Redis", destination_client, destination_client.ping())
