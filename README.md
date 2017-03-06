## OctoPrint Kodi notification

Using [OctoPrint's event hooks][hook] and this script, Kodi can display
usefully information from OctoPrint.

Something like the following will need to get added to ```config.yaml```:

```events:
  enabled: True
  subscriptions:
  - event: Disconnected
    command: python ~/kodi-notification.py --title "OctoPrint" --message "Lost connection to printer"
    type: system
  - event: PrintStarted
    command: python ~/kodi-notification.py --title "OctoPrint" --message "Starting {file}"
    type: system
  - event: PrintDone
    command: python ~/kodi-notification.py --title "OctoPrint" --message "Completed {file}"
    type: system
```


[hook]: http://docs.octoprint.org/en/master/events/index.html
