  GNU nano 7.2                                                          /home/steve/scripts/perms.sh                                                                    
#!/bin/bash
sudo chown steve:media-pod -R /mnt/union/media
sudo find /mnt/union/media/ -type d -exec chmod 0777 {} \;
sudo find /mnt/union/media/ -type f -exec chmod 0666 {} \;
