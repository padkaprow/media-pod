#!/bin/bash
podman volume create jellyfin-cache
podman volume create jellyfin-config
podman volume create media
podman network create --subnet 10.0.0.0/16 media-net
podman run -d -p 8096:8096 -h=jellyfin-srv --network=media-net --pull=always --restart=on-failure:3 --replace --tz=America/New_York -v jellyfin-cache:/cache -v jellyfin-config:/config -v media:/media --name jellyfin docker.io/jellyfin/jellyfin:latest