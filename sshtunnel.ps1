while($true) {
    echo "Starting Proxy"
    ssh -N -g -R 8096:192.168.1.21:8096 -R 7878:192.168.1.21:7878 -R 8989:192.168.1.21:8989 -R 9117:192.168.1.21:9117 -R 9091:192.168.1.21:9091 -o ExitOnForwardFailure=yes ubuntu@x.x.x.x
    echo "Connection Error"
    echo "Sleeping 10s"
    ssh ubuntu@x.x.x.x "sudo fuser -k 8096/tcp"
    Start-Sleep -Seconds 10
}
