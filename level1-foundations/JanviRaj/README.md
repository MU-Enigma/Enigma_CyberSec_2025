# Level 1: Network Foundations Submission 

## Contributor: [Janvi75](https://github.com/Janvi75)

## Objective

Design and implement a functional SOHO (Small Office/Home Office) network in Cisco Packet Tracer using:

- **2 PCs**
- **1 Switch**
- **1 Router**

The goal is to ensure full end-to-end connectivity between the devices using static IP addressing.

This file demonstrates the completed Level 1 task as per the submission requirements.

---

## 1. Network Topology

A simple SOHO network was created using:

- **Router Model:** 1941 Router0
- **Switch Model:** 2960-24TT Switch0
- **PCs:** PC0, PC1


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


