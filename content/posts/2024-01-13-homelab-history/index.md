---
title: 'homelab part 1: the history'
date: 2024-01-13
preview: ""
draft: false
layout: "post"
description: "homelab part 1: the history"
#preview: vault-secrets.png
#thumb: vault-secrets.png
#cover: vault-secrets.png
#feature: vault-secrets.png
slug: homelab-pt1-history
---

I had a lot of time over Christmas, and I decided to rebuild my homelab. The intent behind this series of posts is to describe my process, whilst demonstrating the value of a homelab to a Cyber Security Professional, especially if you are trying to interact with operations or architects. 

Before we get to that point though, I feel a brief history lesson of how I've gone through homelabs over the years, how it's evolved, and what I've learnt through the years. Whilst I'm not going to go through every iteration (there was a lot of changes over the years), I am going to talk about what the most "iconic" setups were.

## prehistory:
Way back when, @wan0net was a small, 17 year old, waiting to start his university degree. He wanted to try out Linux. So he took his trusty Acer TravelMate laptop that was bought for him for passing his GCSE's two years ago and  says, what the hell, why not install Linux on here?

And so his rabbit hole down the path of Linux began, and the first time he went "Oh crap I just killed my Windows install."

First I made the mistake of trying Gentoo. This was the time when bandwidth caps existed (Our house had a monthly cap of 12Gb(!), except Bigpond had a trick where the last day of the month they uncapped you. Thats when we did all our downloading), and the Gentoo ISO looked significantly smaller than anything else I could find. Oh how I was wrong, and lets just not talk about that one. And because I didn't have a reinstall disk for Windows at the time... I was stuck with Linux.

Then I tried OpenSUSE because I went to a gaming cafe one day and they just happened to have a spare CD. That lasted for a while. At this point, the hinges on my laptop had actually broken, so I had the laptop on a cabinet by the side of my bed, a keyboard and mouse in my lap in bed, and a monitor on a side table. I wish I had a photo because it is just the epitome of a teenage boy who broke his toys and then needed to find a way to make it work.

Finally, I met Ubuntu, which started a longstanding relationship with the distro. In those days (and I think still now?) you could order an Ubuntu CD to be delivered to your house, with stickers, free of charge. No bandwidth issues anymore! Based on what is terrible memory I'm going to say that I started with Hardy (8.04 LTS), and ever since then I've used every single LTS edition of Ubuntu without fail, and ignored the other editions.

An accurate representation of this entire story can be seen below:

![](meme-ricky.png)

This all happened pre- me having a dedicated "lab" compared to my normal "prod", but it's good context for where I went next.

## homelab v1: eeePC + external drives (2010)

![](homelab_v1.jpg)

### Specs

- 1 x Server - Asus eeePC 904HA
  - Intel Atom B270 @ 1.6GHz
  - 1Gb DDR2
  - 160Gb HDD
  - Wifi 802.11 b/g
  - 1Gb Ethernet
- 2 x Seagate 2TB External HDD


### History
In great IT tradition, my first spelunk into homelabs was through reusing equipment that I no longer used day-to-day. I was in my second year of university, and had just bought a new Acer Netbook (I think it had Windows 7 on it). So my old Asus eeePC was turned into an Ubuntu Server NAS, with two external Seagate drives that were purchased from Harvey Norman for $99 in the NY sales (a deal at the time). This is where I started playing about with things like [XBMC, now Kodi](https://kodi.tv) and [znc](https://wiki.znc.in/ZNC), running them on the server and accessing them from my netbook. 

## homelab v2: the microserver and the whitebox (2013)

![](homelab_v2.jpg)

### Specs

- 1 x NAS - HP N54L Microserver
  - 8GB DDR2 RAM
  - 4 x 2TB Seagate Shucked HDD in RAID5

- 1 x Compute Host - Whitebox
  - AMD FX-6300 
  - 16Gb DDR3
  - 120 Gb Intel 520 SSD

- 1 x Netgear GS108Tv2 Managed Switch 
    
### History

The N54L Microserver is a well known part of a homelabbers arsenal, and I am no different. This thing was an utter dream. Did you know you could fit 6 3.5" drives in this? Through searching of random forums (probably [Whirlpool](https://whirlpool.net.au/)), I found a bracket that PC Case Gear sold that would go in the 5 1/2" bay of the Microserver and allow two drives to be mounted instead of one, due to clearance. Where did the extra SATA come from you ask? The back of the Microserver, which had an eSATA port! I can’t find a photo of it, which is an utter embuggerance to be honest, so you’ll have to use your imagination.

On this box I ran Ubuntu for a bit with LVM and ext4, then I heard of ZFS and FreeNAS, and I wanted some of that. Would have. been RAIDZ1 on this box. This ran as an SMB media host for our family, and our TV’s used… Wii’s to connect over SMB to it to watch TV. Yep, a Homebrew Wii was our equivalent of a Chromecast back then. 

Attached to this via a Netgear Managed Switch (I was playing about with VLANs and LAGG at this point) was a white box PC, using an AMD CPU as they had more cores than Intel at the time. This was before the resurgence with Zen, and was using ol’ Bulldozer or Piledriver cores. The performance was _okay_, and it was a good way to learn how to use ESX (which came in handy for my first job)

## homelab v3: custom built nodes (2016)
![](homelab_v3.jpg)

### Specs

- 2 x Compute Host - Whitebox
  - Supermicro A1SRi-C2758F
  - 32GB DDR3 SODIMM
  - 500GB Samsung 850 Evo SSD
  - Antec ISK300 Case
- 1 x NAS - HP N54L Microserver
  - 8GB DDR2 RAM
  - 6 x 3TB WD Red HDD in RAID5
- 1 x Compute Host - Intel NUC D4250WYK
  - 120Gb Intel 520 SSD
- 1 x Ubiquiti EdgeRouter ERLite
- 1 x DLink DGS-1024D Switch
- 1 x Asus AC68u Router 

Even though I was living at home still at this point, I wanted to own my entire network. I still had to connect upstream to my parents, but I segregate myself off a little subnet using my ERLite, used a smidgeon of spectrum through my own Asus AC68u router, and then hooked them both up to a 24 port managed DLink switch.

I had heard about the Intel Atom C2xxx series chips and thought, they seem great! 8 cores, low power, small boards, perfect! So I ended up shipping a bunch of parts from Newegg to Australia, including the [Supermicro A1SRi-C2758F](https://www.supermicro.com/products/motherboard/atom/x10/a1sri-2758f.cfm) board, and built two nodes of a very quiet, very power sipping homelab. I even included a Noctua 80mm Fan to ensure there was good airflow, and not a huge amount of noise, as ultimately this thing lived in my living room (yes, at home I had my own living room). It wasn’t till a couple of years later we learnt about the timing bug in these things - I was never affected, but I eventually moved off the platform entirely.

My Microserver also got an upgrade, moving from 6TB usable storage to 30TB usable storage. I’ve still actually got a heap of these 3TB drives at home, that I still use for when I want to transfer data.

This is when I started running an actual “cluster” of VMware at home. I ran [www.plex.tv](Plex) at home, connecting to my XBOX One, and also set it up so that when I was living in a hotel for 6 months, I could use still access it. 

_Side note, when stuck in that hotel for 6 months in Canberra, I bought a router from an Optus subsidiary VividWireless, who provided a 4G connection at 10Mbit for $89 a month. I bought a projector, and used a wall of my hotel room to play TV through my XBOX One S (which I’d brought in my luggage) which connected back to Plex, running on my NAS in Adelaide at my parents. Good times…_

![](photo_from_hotel_room.jpg)


## homelab v4: the allbids special (2018)
![](homelab_v4.jpg)

### Specs

- 1 x NAS - Whitebox
  - Supermicro A1SRi-C2758F
  - 32Gb DDR3 SODIMM
  - 8 x 6Tb Seagate Ironwolf HDD in RAIDZ2
  - Fractal Design Node 804
- 1 x PFSense Gateway - Whitebox
  - Supermicro A1SRi-C2758F
  - 32Gb DDR3 SODIMM
  - 500Gb Samsung 850 Evo SSD
  - Antec ISK300 Case
- 3 x Compute Host - Dell R710
  - Intel X5650
  - 128Gb DDR3 RAM
  - 2 x 3Tb WD Red HDD in RAID1 
- 1 x HP KVM Console  
- 1 x DLink DGS-1024D Switch
- 1 x Asus AC68u Router 

This is where things start to get a bit more frequent, so I’m only going to pull out the biggest changes. It’s also when I moved into my own place, and therefore I had a whole two bedroom unit, and a garage, all to myself - including the electrical bill (which was to be my downfall).

For those who don’t live in Canberra, [Allbids](www.allbids.com.au) is a well known auction site of ex-Government and Business computers, furniture, everything. I’d heard about it from work, and I started splurging. Hard. Over a number of months and auctions, I ended up picking 3 of the R710 boxes, of different specs, and started to make them the same. This is where sites like [AliExpress](www.aliexpress.com) really come in handy - if you want refurbished parts, they’re the place to go. I bought rails, CPUs and RAM, iDRAC cards, even the front fascia plates as well! I wanted my own little data centre in my spare room. I even had a KVM console hooked up so I could be all cool and do management.

I repurposed one of my Supermicro boxes as a NAS, using the amazing Fractal Design Node 804 case (this thing, at the time at least, blew my mind with two chambers for airflow), and the other as a PFSense gateway for my NBN FTTN/VDSL2 connection, which at least ran at 100Mbit. 

Eventually I got all the boxes consistent and then… I didn’t really do anything with it. I installed ESXi and vCentre, ran a few VMs (but nothing to really use the capacity). This was a really hectic time at work, and quite a stressful point of my life (in some cases that I’d rather forget). I also think I was excited by the idea of having my own rack,  So rather than move house with this, I sold all the server bits off, and moved to a less power hungry solution. Which brings us to…

## homelab v5: the initial hit of ubiquiti (2019)
![](homelab_v5.jpg)

### Specs
- 1 x NAS - Synology 3617xs+
  - Intel Xeon D-1521
  - 16Gb DDR3 SODIMM
  - 12 x 6Tb Seagate Ironwolf HDD in RAID6
- 3 x Compute Host - Dell R210 ii
  - Intel E3-1240
  - 32Gb DDR3 RAM
  - 2 x 3Tb WD Red Drives in RAID1
- 1 x Ubiquiti Unifi Cloud Key Gen 2
- 1 x Ubiquiti Unifi Security Gateway Pro
- 1 x Ubiquiti Unifi Switch 24 Port
- 1 x Ubiquiti Unifi Access Point Long Range
- 3 x Ubiquiti Unifi Switch 8 Port

## homelab v6: full on ubiquiti madness (2020)
![](homelab_v6.jpg)

### Specs
- 1 x NAS - Synology 3617xs+
  - Xeon D-1521
  - 48Gb DDR3 SODIMM
  - 12 x 6Tb Seagate Ironwolf HDD in RAID6
  - 10GBe Card
- 3 x Compute Host - Dell R210 ii
  - Intel E3-1240
  - 32Gb DDR3 RAM
  - 1 x 250Gb Crucial M500 SSD
  - 1 x 3Tb WD Red Drives in RAID1
- 1 x Ubiquiti Unifi Dream Machine Pro
- 2 x Ubiquiti Unifi Aggregation Switch
- 1 x Ubiquiti Unifi flexHD AP
- 2 x Ubiquiti Unifi nanoHD AP
- Ubiquiti Unifi Access Point Long Range

The first year of the COVID pandemic I moved into a much larger 4 bedroom house. That meant I needed, or at least I thought I needed, a more substantial networking setup. I ran conduit through the house against the baseboards with the ultra thin Monoprice CAT6 RJ45 cabling, and created a 10Gbe backbone from my garage rack, to the front room. There were 3 access points, 2 Unifi nanoHD’s and a flexHD (exact same electronics just a different form factor), all connected using a Unifi Aggregation Switch to a Unifi Dream Machine Pro. It was… overkill to say the least. But it worked, other than a small furry thing who moved in and realised that if he ate the purple cable near the living room, his papi would come out of his office because the WiFi had died!

Compute wise I bought a whole bunch of Dell R210 ii servers. Well, technically I bought Riverbed devices, and then reflashed the BIOS back to Dell, and went from there. 

_Side Note: In the picture it appears there is a Dell R520… I did have one, but for a *very* short amount of time. I think my intent was to fill it with WD Green drives, and run it as a shared storage solution for the R210iis. Again, power wise, too much, and in summer (noting this was all in my garage) it did not fare well._

## homelab v7: the dark ages (2021)

### Specs
- 1 x NAS - Synology 3617xs+
  - Xeon-D 1521
  - 48Gb DDR3 RAM
  - 12 x 6TB Seagate Ironwolf HDD in RAID6
  - 10GBe Card
- 1 x Disk Array - Synology DX1215
  - 10 x 10TB Seagate Ironwolf HDD in RAID6  
  - 2 x 500GB WD Green SATA SSD in RAID1
- 1 x Plex Host - Dell Optiplex 7040
  - Intel i5 6500T
  - 16Gb DDR4 RAM
  - nVidia   
  - 250 Gb Crucial M500
- 2 x Asus XT8 Access Point

I didn't do a lot with the homelab after 2020 to be honest. I ripped out most of the Ubiquiti gear as I'd had too many issues keeping it running (when the UDM-PRO had an update the RJ45 SFP+ would stop working for example), and the non-ethernet-uplink mesh performance was complete and utter garbage. I replaced my entire Ubiquiti setup with a set of two Asus XT8 that was, and continues to be, utterly amazing. I bought a new DX1215 for the Synology NAS so that I could upgrade the storage to ~120Tb usable. The Dell Desktop was bought so I could enable transcoding through either Intel Quicksync or nVidia NVENC. But all I really did was run docker containers - nothing fancy, just a few apps here and there like [Calibre Web](), [Plex]().

Life got far too busy for me to do things. I had two dogs who lived with me, I went through some major health challenges, and work was very busy. I just didn't *feel* like fiddling and tinkering. It's the same feeling I had when I swapped from Android to iPhone way back in 2016 - I just wanted something that worked.

## homelab v8: the golden age (2023)

### Specs
- 1 x NAS - Synology 3617xs+
  - Xeon-D 1521
  - 48Gb DDR3 SODIMM
  - 12 x 6TB Seagate Ironwolf HDD in RAID6
  - 10GBe Card
- 1 x Disk Array - Synology DX1215
  - 10 x 10TB Seagate Ironwolf HDD in RAID6  
  - 2 x 500GB WD Green SSD in RAID1
- 1 x OPNSense Gateway - Lenovo ThinkStation M720q 
  - Intel Pentium G5400T
  - 16Gb DDR4 RAM
  - 128Gb NVME SSD 
  - 4 x 2.5 Gbe Network Card (Intel i225-v3)
- 3 x Compute Host - Lenovo ThinkStation M920q
  - Intel i5 8500T
  - 32Gb DDR4 RAM
  - 256Gb NVMe SSD
  - 500Gb WD Green SATA SSD
  - 2.5Gbe USB Ethernet Adapter
- 1 x Services Host - Lenovo ThinkStation M910q
  - Intel i5 7500T
  - 32Gb DDR4 RAM
  - 256Gb NVMe SSD
  - 500Gb WD Green SATA SSD
  - 2.5Gbe USB Ethernet Adapter 
- 1 x KeepLink 8 Port 2.5Gbe Switch
- 1 x TP-Link 8 Port 1Gbe Switch     
- 2 x Asus XT8

And this is what we have currently. I can’t promise it’s going to stay this way for long - I’m looking at swapping the M910q for a M920q, and maybe upping the RAM on the compute nodes - but it’s where we are now.  