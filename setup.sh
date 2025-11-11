#!/bin/bash

SERVICE_NAME="svcmon"
TIMER_NAME="${SERVICE_NAME}-check"
SOURCE_DIR="/opt/${SERVICE_NAME}"
TARGET_DIR="/etc/systemd/system"

# 1. Create symlinks for the main service, scheduled service, and timer
sudo ln -sf "${SOURCE_DIR}/${SERVICE_NAME}.service" "${TARGET_DIR}/${SERVICE_NAME}.service"
sudo ln -sf "${SOURCE_DIR}/${TIMER_NAME}.service" "${TARGET_DIR}/${TIMER_NAME}.service"
sudo ln -sf "${SOURCE_DIR}/${TIMER_NAME}.timer" "${TARGET_DIR}/${TIMER_NAME}.timer"

# 2. Reload the systemd manager configuration
sudo systemctl daemon-reload

# 3. Enable and start the main service
sudo systemctl enable "${SERVICE_NAME}.service"
sudo systemctl start "${SERVICE_NAME}.service"

# 4. Enable and start the timer (which controls the scheduled service)
sudo systemctl enable "${TIMER_NAME}.timer"
sudo systemctl start "${TIMER_NAME}.timer"

echo "SvcMon Setup Completed."