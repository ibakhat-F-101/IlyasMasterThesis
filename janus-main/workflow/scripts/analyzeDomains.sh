#!/bin/bash
 DOMAINS=("cyber" "user" "it" "training" "supportInfra")
 PORTS=("8081" "8082" "8443" "8084" "8444" "8446" "8086" "8087" "8088")
 PROJECT_DIR=$1
 for DOMAIN in "${DOMAINS[@]}"; do
        cd $PROJECT_DIR/domain/$DOMAIN
        bash vagrant destroy -f && vagrant box update && vagrant up
        cd ~/

        
        # We are no longer using IPs, but separate ports for services
        #IPs=($(grep -r "IP" $PROJECT_DIR/domain/$DOMAIN/*/*.yml | 
          #awk -F ':' '{gsub(/^[ \t]+/,"",$3); print $3}' |
          #grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"))

        #if [ -z "$IPs" ]; then
            #echo "Error: IP not found"
        #else
        for PORT in "${PORTS[@]}"; do
            echo "http://127.0.0.1:$PORT here is the ip"
            if curl -k -s --head --request GET http://127.0.0.1:$PORT | grep "200" > /dev/null ; then
                echo "IP 127.0.0.1:$PORT is reachable"
                if docker run -v $(pwd):/zap/wrk/:rw \
                    -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py \
                    -t "http://127.0.0.1:$PORT" -r testreport_${PORT//[:\/]/_}.html; then
                    echo "ZAP scan completed successfully for IP 127.0.0.1:$PORT"
                else
                    echo "Error: ZAP scan failed for IP 127.0.0.1:$PORT"
                fi
            else
                echo "IP 127.0.0.1:$PORT is not reachable"
            fi
        done

            rm -rf /home/gitlab-runner/zap_reports/$DOMAIN
            mkdir -p zap_reports/$DOMAIN

            mv ./testreport* zap_reports/$DOMAIN
        #fi
done
