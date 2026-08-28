---
title: "Projects"
date: 2026-08-29T00:00:00+10:00
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

A curated view of original public projects from [wan0net](https://github.com/wan0net) and [link42-au](https://github.com/link42-au) on GitHub. Forks and support-only repositories are omitted; the GitHub profiles remain the complete public index.

## link42

{{< project
  name="Link42"
  image="link42.png"
  description="Australian-built security tooling focused on useful, honest capabilities. The public repository contains the company website, learning material, blog, and the safeguards that keep its release independent from private services."
  github="https://github.com/link42-au/link42"
  url="https://link42.app/"
  tech="SvelteKit, TypeScript, GitHub Pages"
  status="Live"
>}}

### link42 apps

{{< project
  name="Rule1"
  image="rule1.png"
  description="Standalone security-controls explorer covering retained history from the Australian ISM, New Zealand ISM, Cyber Essentials, NIST CSF, and NIST SP 800-53. The catalogue runs locally in the browser from a checksum-verified SQLite snapshot."
  github="https://github.com/link42-au/rule1"
  url="https://rule1.link42.app/"
  tech="SvelteKit, TypeScript, SQLite WASM, Python"
  status="Live"
>}}

{{< project
  name="Patch8"
  image="patch8.png"
  description="Public, read-only vulnerability intelligence explorer. Its restored static interface is live while the rights-gated data pipeline and browser-local DuckDB/Parquet experience are developed in public."
  github="https://github.com/link42-au/patch8"
  url="https://link42-au.github.io/patch8/"
  tech="SvelteKit, TypeScript, DuckDB-Wasm, Parquet"
  status="In development"
>}}

{{< project
  name="Threat10"
  image="threat10.png"
  description="Browser-local explorer for structured security knowledge rather than live IOC monitoring. The static interface is public; its rights-gated ATT&CK data pipeline and immutable Parquet releases remain in development."
  github="https://github.com/link42-au/threat10"
  url="https://link42-au.github.io/threat10/"
  tech="SvelteKit, TypeScript, DuckDB-Wasm, Parquet"
  status="In development"
>}}

## games

{{< project
  name="Civilization II"
  image="civ2.png"
  description="Graphics-first browser recreation of Civilization II Multiplayer Gold Edition, preserving the original interface, rules, music, movies, and Windows-era character. Requires a legally owned copy before original game assets load."
  github="https://github.com/wan0net/civ2"
  url="https://wan0.net/civ2/"
  tech="JavaScript, Canvas 2D, Vite, Playwright"
  status="Public beta"
>}}

{{< project
  name="Spacebase DF-9"
  image="df9.png"
  description="Independent, graphics-first browser recreation of Spacebase DF-9 using the published Lua source as its behavioural reference. Rebuilds the simulation, interface, audio, and game systems in TypeScript and Three.js."
  github="https://github.com/wan0net/df9"
  tech="TypeScript, Three.js, Vite, Playwright"
  status="Public beta"
>}}

## mobile

{{< project
  name="Flare Journal"
  image="flare-journal.png"
  description="Privacy-first iOS app for tracking autoimmune disease activity across 14 conditions with 17 validated clinical scores. Longitudinal charting, daily symptom logging, and shareable reports, with health data kept on-device and in the user's iCloud."
  github="https://github.com/wan0net/flare"
  url="https://wan0.net/flare/"
  tech="Swift, SwiftUI, SwiftData, Swift Charts"
  status="Coming soon"
>}}

## embedded & hardware

{{< project
  name="ThistleOS"
  image="thistle-os.png"
  description="Portable operating system for ESP32 devices with a hardware-independent Rust kernel, loadable apps and drivers, swappable window managers, and signed over-the-air delivery."
  github="https://github.com/wan0net/thistle-os"
  url="https://wan0.net/thistle-os/"
  tech="Rust, ESP-IDF, FreeRTOS, embedded-graphics"
  status="Beta"
>}}

{{< project
  name="thistle-tk"
  description="No-std Rust widget toolkit for e-paper and LCD displays. A semantic widget tree, flexbox-style layout, themes, and display-specific colour mapping let the same application UI render across embedded displays."
  github="https://github.com/wan0net/thistle-tk"
  tech="Rust, embedded-graphics, no-std"
  status="Alpha"
>}}

{{< project
  name="ThistleOS App Store"
  image="thistle-apps.png"
  description="Public catalogue and distribution site for ThistleOS apps, drivers, firmware, window managers, and themes."
  github="https://github.com/wan0net/thistle-apps"
  url="https://wan0.net/thistle-apps/"
  tech="HTML, CSS, JavaScript"
  status="Active"
>}}

## agents & security

{{< project
  name="Pantheon Blueprint"
  image="pantheon-blueprint.png"
  description="Open reference architecture for a personal AI assistant that separates knowledge, collection, review, and tool execution behind explicit boundaries and human approval. The public repository contains architecture and sanitised examples, not live deployment state."
  github="https://github.com/wan0net/asgard"
  url="https://wan0.net/asgard/"
  tech="MkDocs, Python, Architecture, Security"
  status="Reference"
>}}

{{< project
  name="Sharkcage"
  description="Trust and sandboxing layer for OpenClaw with per-tool and per-skill kernel sandboxing, explicit capabilities, approval gates, and a tamper-evident local audit trail."
  github="https://github.com/wan0net/sharkcage"
  tech="TypeScript, Sandbox Runtime, seccomp, Seatbelt"
  status="In development"
>}}

{{< project
  name="trust0"
  image="trust0.png"
  description="Portable cryptographic identity verification with client-side proofs, signed identity history, key rotation, revocation, and document signing. Private keys remain in the user's browser."
  github="https://github.com/wan0net/trust0"
  url="https://wan0.net/trust0/"
  tech="JavaScript, WebCrypto, Ed25519, JWS"
  status="In development"
>}}

## home automation

{{< project
  name="Home Assistant Notion Kanban"
  image="homeassistant-notion-kanban.png"
  description="Custom Home Assistant integration that syncs a Notion Kanban board as a todo list with a drag-and-drop Lovelace card."
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

## infrastructure & utilities

{{< project
  name="Proton Mail Bridge Exporter"
  description="Restartable, read-only Proton Mail exporter that writes complete RFC822 messages through Proton Mail Bridge and records durable SQLite checkpoints for safe resume and deduplication."
  github="https://github.com/wan0net/proton-mail-bridge-exporter"
  tech="Python, IMAP, SQLite"
  status="Active"
>}}

{{< project
  name="Kasm Workspaces"
  description="Auditable Ubuntu 24.04 and KDE Plasma workspace images built from scratch for Kasm, with separate core and custom layers plus a Kasm-compatible registry."
  github="https://github.com/wan0net/kasm"
  tech="Shell, Docker, KDE Plasma, KasmVNC"
  status="Active"
>}}

{{< project
  name="AI Coding Bootstrap"
  image="ai-coding-bootstrap.png"
  description="Bootstrap templates for Claude Code managed software projects, with opinionated project scaffolding and CLAUDE.md conventions."
  github="https://github.com/wan0net/ai-coding-bootstrap"
  tech="Shell, Markdown"
  status="Active"
>}}

{{< project
  name="Homelab"
  image="homelab-demo.png"
  description="Infrastructure-as-code example for a multi-node homelab using Proxmox virtualisation, Docker containers, Ansible provisioning, and Terraform VM creation."
  github="https://github.com/wan0net/homelab-demo"
  tech="Shell, Ansible, Terraform, Docker"
  status="Maintained"
>}}

## resources & community

{{< project
  name="Awesome ABAC"
  image="awesome-abac.png"
  description="Curated list of applications that enable or natively support Attribute Based Access Control for security and IAM practitioners."
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
