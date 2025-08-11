#!/bin/bash
 DOMAINS=("cyber" "user" "it" "training" "supportInfra")
 PROJECT_DIR=$1
 for DOMAIN in "${DOMAINS[@]}"; do
        cd $PROJECT_DIR/domain/$DOMAIN
        bash vagrant destroy -f && vagrant box update && vagrant up
        cd ~/

        IPs=($(grep -r "IP" $PROJECT_DIR/domain/$DOMAIN/*/*.yml | 
          awk -F ':' '{gsub(/^[ \t]+/,"",$3); print $3}' |
          grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"))

        if [ -z "$IPs" ]; then
            echo "Error: IP not found"
        else
            for IP in "${IPs[@]}"; do
                echo "http://$IP here is the ip"
                if curl -k -s --head --request GET http://$IP | grep "200" > /dev/null ; then
                    echo "IP $IP is reachable"
                    if docker run -v $(pwd):/zap/wrk/:rw \
                        -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py \
                        -t "http://$IP" -r testreport_${IP//[:\/]/_}.html; then
                        echo "ZAP scan completed successfully for IP $IP"
                    else
                        echo "Error: ZAP scan failed for IP $IP"
                    fi
                else
                    echo "IP $IP is not reachable"
                fi
            done

            rm -rf /home/gitlab-runner/zap_reports/$DOMAIN
            mkdir -p zap_reports/$DOMAIN

            mv ./testreport* zap_reports/$DOMAIN
        fi
done
