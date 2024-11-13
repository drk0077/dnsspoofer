*****Set Up the Environment*****:
Ensure both your Kali machine and the target computer are connected to the same network.

1-- This allows your Kali machine to forward packets between the target and the gateway.
```sh
echo 1 > /proc/sys/net/ipv4/ip_forward
```
