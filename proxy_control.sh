#!/bin/bash

# Proxy Control Script for IP Phantom
# This script enables/disables system-wide SOCKS proxy on macOS

PROXY_HOST="127.0.0.1"
PROXY_PORT="9050"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

show_help() {
    echo -e "${YELLOW}Proxy Control for IP Phantom${NC}"
    echo ""
    echo "Usage: $0 [enable|disable|status]"
    echo ""
    echo "Commands:"
    echo "  enable   - Enable system-wide Tor proxy (route all traffic through Tor)"
    echo "  disable  - Disable system-wide proxy (return to normal internet)"
    echo "  status   - Show current proxy status"
    echo ""
    echo "Example workflow:"
    echo "  1. Start IP Phantom: ip-phantom --interval 10"
    echo "  2. Enable proxy: $0 enable"
    echo "  3. Browse normally - all traffic goes through Tor with changing IPs"
    echo "  4. Disable proxy: $0 disable (when done)"
}

get_network_service() {
    # Get the active network service name
    networksetup -listnetworkserviceorder | grep "$(route get default | grep interface | awk '{print $2}')" | head -1 | sed 's/^.*) //'
}

enable_proxy() {
    SERVICE=$(get_network_service)
    if [ -z "$SERVICE" ]; then
        echo -e "${RED}Error: Could not detect active network service${NC}"
        exit 1
    fi
    
    echo -e "${YELLOW}Enabling system-wide SOCKS proxy...${NC}"
    echo "Network Service: $SERVICE"
    echo "Proxy: ${PROXY_HOST}:${PROXY_PORT}"
    
    # Enable SOCKS proxy
    networksetup -setsocksfirewallproxy "$SERVICE" $PROXY_HOST $PROXY_PORT
    networksetup -setsocksfirewallproxystate "$SERVICE" on
    
    echo -e "${GREEN}✅ System-wide proxy enabled!${NC}"
    echo -e "${GREEN}All network traffic now routes through Tor${NC}"
    echo ""
    echo -e "${YELLOW}⚠️  Remember to disable when done: $0 disable${NC}"
}

disable_proxy() {
    SERVICE=$(get_network_service)
    if [ -z "$SERVICE" ]; then
        echo -e "${RED}Error: Could not detect active network service${NC}"
        exit 1
    fi
    
    echo -e "${YELLOW}Disabling system-wide proxy...${NC}"
    echo "Network Service: $SERVICE"
    
    # Disable SOCKS proxy
    networksetup -setsocksfirewallproxystate "$SERVICE" off
    
    echo -e "${GREEN}✅ System-wide proxy disabled!${NC}"
    echo -e "${GREEN}Network traffic restored to normal${NC}"
}

show_status() {
    SERVICE=$(get_network_service)
    if [ -z "$SERVICE" ]; then
        echo -e "${RED}Error: Could not detect active network service${NC}"
        exit 1
    fi
    
    echo -e "${YELLOW}Current Proxy Status:${NC}"
    echo "Network Service: $SERVICE"
    echo ""
    
    # Check SOCKS proxy status
    PROXY_STATE=$(networksetup -getsocksfirewallproxy "$SERVICE")
    echo "$PROXY_STATE"
    
    if echo "$PROXY_STATE" | grep -q "Yes"; then
        echo -e "${GREEN}✅ System-wide proxy is ENABLED${NC}"
        echo -e "${GREEN}Traffic is routing through Tor${NC}"
    else
        echo -e "${RED}❌ System-wide proxy is DISABLED${NC}"
        echo -e "${RED}Traffic is using direct connection${NC}"
    fi
}

# Main script logic
case "$1" in
    enable)
        enable_proxy
        ;;
    disable)
        disable_proxy
        ;;
    status)
        show_status
        ;;
    *)
        show_help
        ;;
esac