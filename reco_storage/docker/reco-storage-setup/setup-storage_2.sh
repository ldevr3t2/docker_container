#!/bin/bash

# Configure mongo shard router
mongo --host reco-storage-router \
    --eval "sh.addShard('shard0set/shard0-r0:27018')"

mongo --host reco-storage-router \
    --eval "sh.addShard('shard1set/shard1-r0:27019')"

mongo --host reco-storage-router \
    --eval "sh.addShard('shard2set/shard2-r0:27020')"

mongo --host reco-storage-router \
    --eval "sh.enableSharding('artist_db')"

mongo --host reco-storage-router \
    --eval "sh.shardCollection('artist_db.artist_tree', { _id : 'hashed' })"
