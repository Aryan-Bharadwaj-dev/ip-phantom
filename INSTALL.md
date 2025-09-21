# IP Rotator Installation Guide

## Prerequisites

### System Requirements
- **Operating System**: Linux (Ubuntu/Debian/CentOS/Arch), macOS, or Windows with WSL
- **Python**: 3.6 or higher
- **Privileges**: sudo access for VPN operations
- **Network**: Internet connection for IP verification

### Required Software
1. **Python 3.6+**
   ```bash
   # Ubuntu/Debian
   sudo apt update && sudo apt install python3 python3-pip
   
   # CentOS/RHEL
   sudo yum install python3 python3-pip
   
   # macOS (with Homebrew)
   brew install python3
   
   # Arch Linux
   sudo pacman -S python python-pip
   ```

2. **OpenVPN Client**
   ```bash
   # Ubuntu/Debian
   sudo apt install openvpn
   
   # CentOS/RHEL
   sudo yum install openvpn
   
   # macOS (with Homebrew)
   brew install openvpn
   
   # Arch Linux
   sudo pacman -S openvpn
   ```

3. **curl** (usually pre-installed)
   ```bash
   # Ubuntu/Debian
   sudo apt install curl
   
   # CentOS/RHEL
   sudo yum install curl
   
   # macOS (usually pre-installed)
   # Arch Linux
   sudo pacman -S curl
   ```

## Installation

### 1. Download or Clone the Project
```bash
# If you have git
git clone <repository-url>
cd ip-rotator

# Or download and extract the files manually
```

### 2. Make Scripts Executable
```bash
chmod +x ip-rotator
chmod +x ip_rotator.py
```

### 3. Install Optional Python Dependencies
```bash
# Install optional packages for enhanced functionality
pip3 install -r requirements.txt

# Or install minimal dependencies
pip3 install requests psutil colorama
```

## VPN Configuration

### Supported VPN Providers
The tool works with any OpenVPN-compatible provider:
- ExpressVPN
- NordVPN
- Surfshark
- ProtonVPN
- Private Internet Access (PIA)
- CyberGhost
- Any custom OpenVPN server

### Getting VPN Configuration Files

#### For Commercial VPN Services:
1. **Sign up** with a VPN provider
2. **Log in** to your account dashboard
3. **Download OpenVPN configuration files** (.ovpn files)
4. **Save them** to a secure directory (e.g., `~/vpn-configs/`)

#### For Self-Hosted OpenVPN:
1. Set up your OpenVPN server
2. Generate client certificates
3. Create .ovpn configuration files
4. Transfer them securely to your client machine

### Configuration File Setup
1. **Run the setup wizard**:
   ```bash
   ./ip-rotator --setup
   ```

2. **Or manually edit** `config.json`:
   ```json
   {
     "vpn_configs": [
       {
         "name": "US-Server-1",
         "type": "openvpn",
         "config_file": "/path/to/us-server-1.ovpn",
         "enabled": true
       },
       {
         "name": "UK-Server-1",
         "type": "openvpn", 
         "config_file": "/path/to/uk-server-1.ovpn",
         "enabled": true
       }
     ]
   }
   ```

### Credentials Setup (if required)
Some VPN providers require username/password authentication:

1. **Create auth file**:
   ```bash
   echo "your_username" > /secure/path/auth.txt
   echo "your_password" >> /secure/path/auth.txt
   chmod 600 /secure/path/auth.txt
   ```

2. **Modify .ovpn files** to include:
   ```
   auth-user-pass /secure/path/auth.txt
   ```

## Testing Installation

### 1. Check Dependencies
```bash
./ip-rotator --help
```

### 2. Test IP Checking
```bash
./ip-rotator --check-ip
```

### 3. Test Configuration
```bash
# This will show current config and any errors
python3 ip_rotator.py --check-ip --verbose
```

## Troubleshooting

### Common Issues

#### Permission Denied Errors
```bash
# Make sure scripts are executable
chmod +x ip-rotator ip_rotator.py

# Check sudo access
sudo -v
```

#### OpenVPN Connection Failures
```bash
# Test VPN config manually
sudo openvpn --config /path/to/your/config.ovpn

# Check OpenVPN logs
sudo journalctl -u openvpn
```

#### Python Module Not Found
```bash
# Install Python dependencies
pip3 install -r requirements.txt

# Or use system package manager
sudo apt install python3-requests python3-psutil
```

#### DNS Resolution Issues
```bash
# Restart DNS service
sudo systemctl restart systemd-resolved

# Or flush DNS cache
sudo systemctl flush-dns
```

### Log Files
- **Application logs**: `ip_rotator.log` (in project directory)
- **OpenVPN logs**: `/var/log/openvpn/` or `journalctl -u openvpn`
- **System logs**: `/var/log/syslog` or `journalctl`

## Security Considerations

### File Permissions
```bash
# Secure configuration files
chmod 600 config.json
chmod 600 /path/to/vpn/configs/*.ovpn
chmod 600 /path/to/auth.txt

# Secure the project directory
chmod 700 ~/Projects/ip-rotator
```

### Network Security
- Use only trusted VPN providers
- Verify VPN configuration authenticity
- Monitor network traffic during testing
- Use DNS leak protection

### Operational Security
- Run with minimal required privileges
- Regularly update VPN configurations
- Monitor logs for suspicious activity
- Use dedicated testing environment

## Next Steps
1. Read the main [README.md](README.md) for usage instructions
2. Review the [Legal Disclaimer](README.md#legal-disclaimer)
3. Test in a safe environment before production use
4. Configure firewall rules as needed
5. Set up monitoring and alerting if required

## Support
- Check log files for error details
- Review configuration file syntax
- Test VPN connections manually
- Verify network connectivity
- Check system requirements