# Title of the incident

**Title:** Connection timeout for ssh server.

**Name:** Ing. Victor Zuluaga Ramirez.

**Date:** Saturday, Febrary 06, 2021 3:34:pm.

**Last modified:** Saturday, Febrary 06, 2021 3:34:pm.

## Context

**On Monday 16 November 2020 (GMT-5)**. Working on servers, I had the responsibility of setting up, installing, and maintaining the webserver. Then, I installed Nginx web server, set it up, and installed all packages and dependencies required.

## issue Summary

**On Tuesday 17 November 2020 (GMT-5) 9:00 AM start the issue detected,** Newly tried login into a server. But, this was not responding. The network was unavailable for a duration of 4 hours 15minutes. Tuesday 17 November 2020 (GMT-5) 1:15 PM end. Now, I understand how important the flexibility to install new resources and scale up, is for our users, and apologize for this incident.

When I was trying to set OpenSSH-server connection, I’m having some issues connecting.

 - Error message: Connection timeout for ssh server.

## Impact

The impact was the process to deploy a new application it set back. Fortunately, was an internal error and was detected before get out to production.

## Root Cause

The issue was triggered by the firewall, among the settings up that I did, enable the firewall, this by default no enable the port 22/TCP for SSH connections. Manually must indicate it to the firewall that allows port 22/tcp connection remotes via SSH. Otherwise, all attempts via SSH the firewall it will deny.

## Remediation and prevention

To resolve the issue, the engineer had to destroy the server and start one again and setting it up and install it all again. Having special matter when it manipulates the firewall in a server.
