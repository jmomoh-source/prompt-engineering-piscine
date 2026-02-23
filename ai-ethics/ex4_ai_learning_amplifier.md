# Phase 1: Build Foundation
***Self-explanation***
- Wireless routing protocols are like AODV, DSR and OLSR are designed to enable communication in decentralized Mobile Ad hoc Networks (MANETSs) without a fixed structure.

- They fall into two categories: reactive(on-demand) and proactive(table-driven) and hybrid types.

- Reactive (on-demand) Protocols only search for a route when a node needs to send data.

- Proactive (Table-Driven) Protocols maintain up-to-date routing information for every node in the network at all times.

- Hybrid protocols combines both proactive and reactive features to balance efficiency and speed.


***simple scenario design (5–10 devices)***

### Small Office Wireless Network

***Devices***
- Router (Wireless Access Point) – central device connecting all wireless clients and the internet.

- Laptop 1 – employee workstation.

- Laptop 2 – employee workstation.

- Smartphone 1 – mobile device for communication.

- Smartphone 2 – mobile device for remote access.

- Printer (Wireless-enabled) – shared printing for the office.

- Network-attached Storage (NAS) – shared storage for team files


### Justification for Wireless Routing Protocol
- In most office Wi-Fi setups, just having everything run through the main router works fine, but if you ever want to set up a mesh or ad-hoc network, protocols like OLSR or AODV are the way to go.



# Phase 2: Strategic AI Use

- Prompt- "How can it be better?"
***AI answers***
- Add a second Access point
- Use a mesh network
- Segment the network
- Upgrade wireless standard
- Add redundancy for critical devices
- Monitor and Optimize



# Phase 3: Real Application

***Devices*** 
- 1000 IoT sensors
- 50 Traffic lights
- 10 emergency vehicles

***Network Design***
- IoT sensors connect wirelessly to local edge gateways using LoRaWAN or Zigbee for low-power, long-range coverage.

- Traffic lights connect to gateways using Wi-Fi 6 (802.11ax) or LTE/5G for real-time control.

- Emergency vehicles connect via cellular 4G/5G for mobility and low-latency priority communications.

- Edge gateways aggregate sensor and traffic light data, then communicate with a central city control server using MQTT over TCP/IP for lightweight, reliable messaging.

- Cloud server stores historical data, performs analytics, and sends control commands back through the gateways.


### Protocols and Justification
| Device / Layer             | Protocol                       | Justification                                                                             |
| -------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------- |
| IoT Sensors                | **LoRaWAN / Zigbee**           | Low power, long battery life, supports thousands of sensors, good for city-wide coverage. |
| Traffic Lights             | **Wi-Fi 6 / LTE / 5G**         | Fast, reliable, supports real-time traffic control, high throughput.                      |
| Emergency Vehicles         | **5G / LTE with QoS priority** | Mobile connectivity, low latency, can preempt traffic control messages.                   |
| Sensor → Gateway Messaging | **MQTT**                       | Lightweight, supports publish/subscribe model, scalable for thousands of devices.         |
| Gateway → Cloud            | **HTTPS / MQTT over TCP**      | Secure, reliable, easy to integrate with analytics and control apps.                      |
| Network Management         | **SNMP / REST APIs**           | Easy monitoring and configuration of devices and gateways.                                |


***Failure points***
- Power outage
- Device malfunction
- Security breaches
- Network congestion

***AI feedback***
- Adding redundancy
- Prioritizing traffic
- Security improvements
- implementing failover protocols


# Reflection:

### human judgment vs. AI contribution
It was a fair work and AI was mostly my learning tool, safe to say me 40% AI 60%

### Could you defend decisions without AI?
Yes, but my reasoning would be slower.

### What will you still remember in 6 months?
Core protocol behaviors, the trade-offs, and design principles for IoT networks.

### Did AI make you sharper, or think for you?
AI sharpened my reasoning by questioning my assumptions, suggesting overlooked scenerios and highlighting tradeoffs not replacing my thinking nor judgement.