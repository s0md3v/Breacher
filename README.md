# Breacher
A script to find admin login pages and EAR vulnerabilites.

#### Features
- [x] Multi-threading on demand
- [x] Big path list (482 paths)
- [x] Supports php, asp and html extensions
- [x] Checks for potential EAR vulnerabilites
- [x] Checks for robots.txt
- [x] Support for custom patns

### Usages
- Check all paths with php extension
```
python breacher -u example.com --type php
```
- Check all paths with php extension with threads
```
python breacher -u example.com --type php --fast
```
- Check all paths without threads
```
python breacher -u example.com
```
- Adding a custom path. For example if you want all paths to start with /data (example.com/data/...) you can do this:
```
python breacher -u example.com --path /data
```
<b>Note: </b> When you specify an extension using <b>--type</b> option, Breacher includes paths of that extension as well as paths with no extensions like <b>/admin/login</b>

#### Video Demo

[![Breacher](https://i.imgur.com/D9my9A5.png)](https://youtu.be/BEpt5JmcWPk)
