# Level 1 Submission - [YourGitHubHandle]

This file demonstrates the completed Level 1 task as per the submission requirements.

---

## 1. Network Topology

A simple SOHO network was created using:

- 2 PCs
- 1 Switch
- 1 Router

![Network Topology](topology.png)

---

## 2. IP Addressing Scheme

The network is configured using the `192.168.1.0/24` range with static IP addressing.

| Device | Interface           | IP Address     | Subnet Mask     | Default Gateway |
|--------|---------------------|----------------|-----------------|-----------------|
| Router | GigabitEthernet0/0  | 192.168.1.1    | 255.255.255.0   | N/A             |
| PC0    | FastEthernet0       | 192.168.1.11   | 255.255.255.0   | 0.0.0.0         |
| PC1    | FastEthernet0       | 192.168.1.12   | 255.255.255.0   | 0.0.0.0         |

---

## 3. Ping Verification

The following output shows a successful ping from **PC0** to **PC1**, confirming end-to-end connectivity.
![Ping Verification](ping.png)


