#!/bin/bash

# Define variables
INSTALL_DIR="$HOME/.local/bin"
EXECUTABLE_NAME="./src/gcal" 
BASHRC="$HOME/.bashrc"
EXPORT_CMD="export PATH=\$PATH:$INSTALL_DIR"

echo "Executing Makefile"
make -C ./src/

# Create the installation directory
echo "Creating install directory: $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

# Copy the executable to the installation directory
cp "$EXECUTABLE_NAME" "$INSTALL_DIR/"

echo "Updating PATH in $BASHRC"
    
echo "$EXPORT_CMD" >> "$BASHRC"
   


echo "Installation complete."
