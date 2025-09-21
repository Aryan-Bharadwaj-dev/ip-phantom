# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

IP Rotator is a cybersecurity tool for automated IP address rotation using VPN connections. It's designed for penetration testing, security research, and privacy protection purposes. The tool rotates IP addresses at configurable intervals and provides comprehensive logging and monitoring capabilities.

## Architecture

### Core Components

1. **IPRotator Class** (`ip_rotator.py`) - Main orchestrator that handles:
   - Configuration management and JSON parsing
   - VPN connection management via OpenVPN subprocess calls
   - IP verification using multiple external services (httpbin.org, ipify, jsonip)
   - Signal handling for graceful shutdown
   - Logging and error handling

2. **Bash Wrapper** (`ip-rotator`) - User-friendly CLI interface that:
   - Provides colored terminal output and ASCII banner
   - Handles argument parsing and validation
   - Performs dependency checks (python3, openvpn, curl)
   - Includes setup wizard for initial configuration
   - Manages VPN connection cleanup

3. **Configuration System** - JSON-based configuration supporting:
   - Multiple VPN providers with OpenVPN configs
   - Proxy configurations (SOCKS5)
   - Rotation methods and timing settings
   - IP verification service URLs

### Key Design Patterns

- **Strategy Pattern**: VPN vs proxy rotation methods
- **Template Method**: Consistent connection/disconnection flow
- **Observer Pattern**: Real-time IP change verification
- **Command Pattern**: CLI argument handling and execution

## Common Development Commands

### Basic Operations
```bash
# Check current IP without starting rotation
./ip-rotator --check-ip

# Start rotation with 10-second intervals
./ip-rotator --interval 10

# Use custom configuration with verbose logging
./ip-rotator --config custom-vpns.json --verbose

# Run setup wizard to configure VPN connections
./ip-rotator --setup

# Stop all running VPN connections
./ip-rotator --stop
```

### Python Direct Usage
```bash
# Check IP using Python directly
python3 ip_rotator.py --check-ip --verbose

# Start rotation with custom settings
python3 ip_rotator.py --interval 30 --config production.json
```

### Development and Testing
```bash
# Install optional development dependencies
pip3 install -r requirements.txt

# Format code (if black is installed)
black ip_rotator.py

# Lint code (if flake8 is installed)  
flake8 ip_rotator.py

# Run tests (if pytest is installed)
python -m pytest tests/

# Make scripts executable after changes
chmod +x ip-rotator ip_rotator.py
```

### System Integration
```bash
# Test OpenVPN configuration manually
sudo openvpn --config /path/to/server.ovpn

# Check OpenVPN service status
systemctl status openvpn

# Monitor application logs
tail -f ip_rotator.log

# Search for errors in logs
grep -i error ip_rotator.log
```

## Configuration Management

### VPN Configuration Structure
The tool expects OpenVPN configuration files (.ovpn) and uses JSON for managing multiple connections:

```json
{
  "vpn_configs": [
    {
      "name": "descriptive-name",
      "type": "openvpn", 
      "config_file": "/absolute/path/to/config.ovpn",
      "enabled": true
    }
  ],
  "rotation_method": "vpn",
  "check_ip_url": "https://httpbin.org/ip"
}
```

### Security Considerations
- VPN credentials should be stored separately in auth files with 600 permissions
- Configuration files should be secured with appropriate file permissions
- The tool requires sudo privileges for VPN operations but should not be run as root
- All VPN connections are automatically cleaned up on exit via signal handlers

## Integration Points

### External Dependencies
- **OpenVPN**: Core VPN client functionality via subprocess calls
- **curl**: HTTP requests for IP verification
- **systemd-resolved**: DNS management during VPN transitions
- **sudo**: Elevated privileges for network operations

### Network Services
- Multiple IP checking services for reliability (httpbin.org, ipify.org, jsonip.com)
- Automatic failover between IP verification services
- Support for both VPN and proxy rotation methods

## Error Handling Patterns

The codebase implements comprehensive error handling with:
- Graceful degradation when services are unavailable
- Detailed logging for troubleshooting
- Signal handlers for clean shutdown
- Retry logic for failed connections
- DNS leak protection and cleanup procedures

## Development Notes

- The tool is designed for educational and authorized security testing only
- Always test VPN configurations manually before adding to automated rotation
- Monitor logs during development to understand connection behavior
- Use verbose mode (`--verbose`) for debugging connection issues
- The bash wrapper provides user-friendly error messages and dependency checking