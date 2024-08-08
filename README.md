# This Podman YAML file defines a multi-container application for media management.

## This file creates a Pod named "media" consisting of nine containers:
jellyfin: A media server for streaming videos and music.\
sabnzbd: A newsgrabber for downloading Usenet content.\
prowlarr: An indexer for finding Usenet content.\
lidarr: A music library manager for organizing and downloading music.\
sonarr: A TV show library manager for organizing and downloading TV shows.\
radarr: A movie library manager for organizing and downloading movies.#
readarr: An ebook library manager for organizing and downloading ebooks.\
jellyseerr: A companion app for Jellyfin providing additional features.\
heimdall: A reverse proxy for managing multiple web applications under a single domain.

## Key Points:
All containers are configured to run with user ID (PUID) and group ID (PGID) set to 1001.
Timezone is set to America/New York (TZ).
Several host directory paths are mounted as volumes within the containers for data persistence.
Specific container ports are mapped to corresponding host ports for external access.
Automatic restart is enabled for all containers (restart: always).

## Additional Notes:

This configuration uses images from docker.io but can be adapted for other registries.
Annotations are included for potential integration with auto-update tools.
Comments can be added to the YAML file for better readability.
For detailed information on each container and its functionalities, refer to the respective project documentation.
