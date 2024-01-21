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

The intent behind this series of posts is to demonstrate the value of a homelab to a Cyber Security Professional, especially if you are trying to interact with operations or architects. Before we get to that point though, I feel a brief history lesson of how I've gone through homelabs over the years, how it's evolved, and what I've learnt through the process. Whilst I'm not going to go through every interation (there was a lot of changes over the years), I am going to talk about what the most "iconic" setups were.

## prehistory:
Way back when, when @wan0net was a small, 17 year old, waiting to start his university degree, he wanted to try things out at home. He wanted to try out Linux, and he wanted to run a home server so that he could run [](znc), an IRC bouncer for the IRC servers he was on for gaming (yes, I know I'm showing my age here). He had no money, but he'd broken his second laptop ever, an Acer XXXXXXXX that was bought for him for passing his GCSE's two years ago. So he says, what the hell, why not install Linux on here?

And so my rabbit hole down the path of Linux began, and the first time I went "Oh crap I just killed my Windows install."

First I made the mistake of trying Gentoo. This was the time when bandwidth caps existed (Our house had a monthly cap of 12Gb(!), except Bigpond had a trick where the last day of the month they uncapped you. Thats when we did all our downloading), and the Gentoo ISO looked significantly smaller than anything else I could find. Oh how I was wrong, and lets just not talk about that one. And because I didn't have a reinstall disk for Windows at the time... I was stuck with Linux.

Then I tried OpenSUSE because I went to a gaming cafe and they had a spare CD, and that lasted for a while. At this point I wasn't running a "headless" server, I basically had the laptop on a cabinet by the side of my bed, with a keyboard and mouse in my lap in bed, and a monitor on a side table. I wish I had a photo because it is just the image of a teenage boy who broke his equipment and then needs to find a way to make it work.

Finally, I met Ubuntu, which started a longstanding relationship with the distro. In those days (and I think still now?) you could order an Ubuntu CD to be delivered to your house, with stickers, free of charge. No bandwidth issues anymore! Based on what is terrible memory I'm going to say that I started with Hardy (8.04 LTS), and every since then, I've used every single LTS edition of Ubuntu without fail, and ignored the other editions.

## homelab v1: eeePC + external drives (2009)

![](homelab_v1.jpg)

### Specs

- Asus eeePC 904HA
  - Intel Atom B270 @ 1.6GHz
  - 1Gb DDR2
  - 160Gb HDD
  - Wifi 802.11 b/g
  - 1Gb Ethernet
- 2 x Seagate 


### History

## homelab v2: the microserver and the whitebox (2013)

![](homelab_v2.jpg)

### Specs

### History
This is when I started to move into dedicated machines. I don't think I can find a photo of the Microserver, which is an utter embuggerance to be honest, but we are talking the OG HP N40L Microserver as seen below:

This thing was an utter dream. Did you know you could fit 6 3.5" drives in this? Through searching of random forums (probably [Whirlpool]()), I found a bracket that PC Case Gear sold that would go in the 5 1/2" bay of the Microserver and allow two drives to be mounted instead of one, due to clearance. Where did the extra SATA come from you ask? The back of the Microserver, which had an eSATA port! 

On this box I ran Ubuntu for a bit, then I heard of ZFS and FreeNAS, and I wanted some of that.


## homelab v3: custom built nodes (2016)
![](homelab_v3.jpg)

## homelab v4: the allbids special (2018)
![](homelab_v4.jpg)

## homelab v5: the initial hit of ubiquiti (2019)
![](homelab_v5.jpg)

## homelab v6: full on ubiquiti madness (2020)
![](homelab_v6.jpg)

## homelab v7: the dark ages (2021)
I didn't do a lot with the homelab after 2020 to be honest. I ripped out most of the ubiquiti gear as I'd had too many issues keeping it running (when the UDM-PRO had an update the RJ45 SFP+ would stop working for example) and replaced it with an Asus XT-8 Mesh key that was utterly amazing. I bought a new DX1215 for the Synology NAS so that I could upgrade the storage to XXX Tb. And all I really did was run docker containers - nothing fancy, just a few apps here and there.

Life got far too busy for me to do things. I had two dogs who arrived to live with me, I became incredibly sick, and work was very busy. I just didn't *feel* like fiddling and tinkering. It's the same feeling I had when I swapped from Android to iPhone way back in 2016 - I just wanted something that worked.

## homelab v8: the golden age (2023)