#!/bin/bash

# IP Phantom Global Installation Script
# This script installs ip-phantom globally so you can run it from anywhere without ./

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Banner
echo -e "${BLUE}"
echo "=================================================================="
echo "                👻 IP PHANTOM GLOBAL INSTALLER"
echo "=================================================================="
echo -e "${NC}"

# Check if we're in the right directory
if [[ ! -f "ip-phantom" ]] || [[ ! -f "ip_phantom.py" ]]; then
    echo -e "${RED}Error: Please run this script from the ip-phantom directory${NC}"
    echo "Make sure you're in the directory containing ip-phantom and ip_phantom.py files"
    exit 1
fi

# Check if already installed
if command -v ip-phantom &> /dev/null && [[ "$(which ip-phantom)" != "$(pwd)/ip-phantom" ]]; then
    echo -e "${YELLOW}IP Phantom is already installed globally at: $(which ip-phantom)${NC}"
    read -p "Do you want to reinstall? (y/N): " -r
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled."
        exit 0
    fi
fi

# Get current directory
CURRENT_DIR="$(pwd)"
INSTALL_DIR="/usr/local/bin"

echo -e "${GREEN}Installing IP Phantom globally...${NC}"
echo "Current directory: $CURRENT_DIR"
echo "Install directory: $INSTALL_DIR"
echo ""

# Check if /usr/local/bin exists
if [[ ! -d "$INSTALL_DIR" ]]; then
    echo -e "${YELLOW}Creating $INSTALL_DIR directory...${NC}"
    sudo mkdir -p "$INSTALL_DIR"
fi

# Create symbolic links
echo -e "${YELLOW}Creating symbolic links...${NC}"

# Remove existing links if they exist
sudo rm -f "$INSTALL_DIR/ip-phantom" 2>/dev/null
sudo rm -f "$INSTALL_DIR/ip_phantom.py" 2>/dev/null

# Create new symbolic links
if sudo ln -s "$CURRENT_DIR/ip-phantom" "$INSTALL_DIR/ip-phantom"; then
    echo -e "${GREEN}✅ Successfully created symbolic link for ip-phantom${NC}"
else
    echo -e "${RED}❌ Failed to create symbolic link for ip-phantom${NC}"
    echo "You might need to run this script with sudo privileges"
    exit 1
fi

if sudo ln -s "$CURRENT_DIR/ip_phantom.py" "$INSTALL_DIR/ip_phantom.py"; then
    echo -e "${GREEN}✅ Successfully created symbolic link for ip_phantom.py${NC}"
else
    echo -e "${RED}❌ Failed to create symbolic link for ip_phantom.py${NC}"
    echo "You might need to run this script with sudo privileges"
    exit 1
fi

# Make scripts executable
echo -e "${YELLOW}Setting executable permissions...${NC}"
chmod +x ip-phantom ip_phantom.py

# Verify installation
echo -e "${YELLOW}Verifying installation...${NC}"
if command -v ip-phantom &> /dev/null; then
    echo -e "${GREEN}✅ Installation successful!${NC}"
    echo ""
    echo -e "${BLUE}🎉 You can now run IP Phantom from anywhere:${NC}"
    echo ""
    echo -e "${GREEN}# Demo mode (recommended for first try)${NC}"
    echo "ip-phantom --demo --interval 5"
    echo ""
    echo -e "${GREEN}# Check current IP${NC}"
    echo "ip-phantom --check-ip"
    echo ""
    echo -e "${GREEN}# Get help${NC}"
    echo "ip-phantom --help"
    echo ""
    echo -e "${GREEN}# Basic IP changing${NC}"
    echo "ip-phantom --interval 10"
    echo ""
    echo -e "${YELLOW}Note: The original files remain in: $CURRENT_DIR${NC}"
    echo -e "${YELLOW}The global command points to these files via symbolic link${NC}"
else
    echo -e "${RED}❌ Installation verification failed${NC}"
    echo "You may need to add $INSTALL_DIR to your PATH"
    echo "Add this to your ~/.zshrc or ~/.bash_profile:"
    echo "export PATH=\"\$PATH:$INSTALL_DIR\""
fi

echo ""
echo -e "${BLUE}==================================================================${NC}"