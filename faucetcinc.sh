#!/bin/sh

FAUCET_HOME=/Users/sapiean/dev/FaucetCinc/
ES_VERSION=1.5.2
LS_VERSION=1.5.0
KB_VERSION=4.0.2

#TODO: Create start, stop, status functions
#TODO: paramatize paths, versions
#TODO: move each component into seperate function
#TODO: figure out how to echo startup errors to shell

#Start up Elasticsearch first
./elasticsearch-1.5.2/bin/elasticsearch -d -p $FAUCET_HOME/es.pid

echo "ElasticSearch Started"


#Startup Kibana
./kibana-4.0.2/bin/kibana 1>>kibana.log &


#Startup Logstash
./logstash-1.5.0/bin/logstash agent -f ./logstash-1.5.0/config/ 1>>logstash.log &


#Stop services....
#kill $(<es.pid)





