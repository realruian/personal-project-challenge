[English](README.md) | [简体中文](README.zh-CN.md)

# Personal Project Challenge

A 12-slide, Chinese-language briefing deck for a seven-day individual product challenge: one person, one topic, and one working product that can be demonstrated online.

![Slide overview](shots/contact_sheet_1.png)

## Course Outline

The deck covers:

- Challenge rules and product-development expectations
- An AI product exploration day
- Topic selection and proposal preparation
- A midweek MVP checkpoint
- Final deliverables, demo-day review, and awards

The presentation is a self-contained HTML file with sidebar navigation, previous/next controls, and keyboard shortcuts.

## View Locally

Open 课件/index.html directly in a browser, or serve the repository:

    python3 -m http.server 4173

Then open http://127.0.0.1:4173/课件/.

Use the left and right arrow keys, Page Up and Page Down, or the on-screen controls to navigate.

## Source and Regeneration

- build.py contains the slide content and assembles the final deck.
- 课件/index.html is the generated, ready-to-use presentation.
- screenshot.py captures every slide and builds contact sheets for visual review.
- shots/ contains the current review images.

The current build script reads the coursedeck template from a local Claude Code skill path. The generated HTML works independently, but regenerating it requires that local template to be available at the path declared in build.py.

Screenshot regeneration additionally requires Playwright, Pillow, and a Playwright Chromium installation.
