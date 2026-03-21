---
title: "Projects"
date: 2026-03-21
draft: false
layout: "page"
showAuthor: false
showBreadcrumbs: false
showDate: false
showDateUpdated: false
showTableOfContents: true
showPagination: false
showReadingTime: false
---

A collection of software projects I'm building or maintaining. Screenshots and details below — source code is on [GitHub](https://github.com/wan0net).

## mobile

{{< project
  name="Flare Journal"
  image="flare-journal.png"
  description="Privacy-first iOS app for tracking autoimmune disease activity across 14 conditions with 17 validated clinical scores. Longitudinal charting with severity zones, daily symptom logging, and shareable reports. All data stays on-device with iCloud sync."
  url="https://wan0.net/flare/"
  tech="Swift, SwiftUI, SwiftData, Swift Charts"
  status="Active"
>}}

## embedded & hardware

{{< project
  name="ThistleOS"
  image="thistle-os.png"
  description="ESP32-S3 operating system for the LilyGo T-Deck Pro. Custom kernel, hardware abstraction layer, LVGL UI, and dynamic ELF app loading."
  github="https://github.com/wan0net/thistle-os"
  tech="C, ESP-IDF, LVGL, FreeRTOS"
  status="Active"
>}}

{{< project
  name="ThistleOS App Store"
  image="thistle-apps.png"
  description="App catalog and distribution platform for ThistleOS. Browse, download, and install apps, drivers, and firmware updates."
  github="https://github.com/wan0net/thistle-apps"
  tech="HTML, CSS, JavaScript"
  status="Active"
>}}

## home automation

{{< project
  name="Home Assistant Notion Kanban"
  image="homeassistant-notion-kanban.png"
  description="Custom Home Assistant integration that syncs a Notion Kanban board as a todo list with drag-and-drop Lovelace card."
  github="https://github.com/wan0net/homeassistant-notion-kanban"
  tech="Python, Home Assistant, Notion API"
  status="Active"
>}}

{{< project
  name="Home Assistant Notion Recipes"
  image="homeassistant-notion-recipes.png"
  description="Custom Home Assistant integration to browse and select recipes from a Notion database, with a gallery-style Lovelace card."
  github="https://github.com/wan0net/homeassistant-notion-recipes"
  tech="Python, Home Assistant, Notion API"
  status="Active"
>}}

## infrastructure & tools

{{< project
  name="Homelab"
  image="homelab-demo.png"
  description="Infrastructure-as-code for a multi-node homelab. Proxmox virtualisation, Docker containers, Ansible provisioning, and Terraform VM creation."
  github="https://github.com/wan0net/homelab-demo"
  tech="Shell, Ansible, Terraform, Docker"
  status="Active"
>}}

{{< project
  name="AI Coding Bootstrap"
  image="ai-coding-bootstrap.png"
  description="Bootstrap templates for Claude Code managed software projects. Opinionated project scaffolding with CLAUDE.md conventions."
  github="https://github.com/wan0net/ai-coding-bootstrap"
  tech="Shell, Markdown"
  status="Active"
>}}

## resources & community

{{< project
  name="Awesome ABAC"
  image="awesome-abac.png"
  description="Curated list of applications that enable or natively support Attribute Based Access Control. Community resource for security and IAM practitioners."
  github="https://github.com/wan0net/awesome-abac"
  tech="Markdown"
  status="Maintained"
>}}

{{< project
  name="ComfyCon Talks"
  image="comfycon_talks.png"
  description="Materials and resources from conference presentations at ComfyCon AU."
  github="https://github.com/wan0net/comfycon_talks"
  tech="Python"
  status="Archived"
>}}

## this website

{{< project
  name="wan0.net"
  image="wan0net-github-io.png"
  description="Personal website and blog. Hugo static site with a custom theme, Notion as CMS, and GitHub Actions for CI/CD."
  github="https://github.com/wan0net/wan0net.github.io"
  url="https://wan0.net"
  tech="Hugo, CSS, Python, GitHub Actions"
  status="Active"
>}}
