# IP Rotator - Cybersecurity Tool

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security: Educational](https://img.shields.io/badge/Use-Educational%20Only-red.svg)](https://github.com/your-repo/ip-rotator)

A powerful cybersecurity tool for automated IP address rotation using VPN connections. Designed for penetration testing, security research, and privacy protection purposes.

## 🔥 Features

- **Automated IP Rotation**: Changes IP address at configurable intervals (default: 3 seconds)
- **VPN Integration**: Supports OpenVPN configurations from major providers
- **Multiple Protocols**: VPN and proxy support with failover mechanisms
- **Real-time Monitoring**: Live IP verification and change tracking
- **Robust Error Handling**: Graceful failure recovery and connection management
- **Comprehensive Logging**: Detailed logs for security auditing
- **Cross-platform**: Linux, macOS, and Windows (WSL) support
- **CLI Interface**: Easy-to-use command-line interface with rich options

## 🎯 Use Cases

### Legitimate Security Testing
- **Penetration Testing**: Evade IP-based detection during authorized security assessments
- **Security Research**: Analyze geo-restricted content and regional security policies
- **Privacy Protection**: Protect personal identity during security research
- **Load Testing**: Test applications with traffic from different geographical locations
- **Threat Hunting**: Investigate threats while maintaining operational security

### Educational Purposes
- **Cybersecurity Training**: Learn network security and anonymity techniques
- **Academic Research**: Study network behavior and security mechanisms
- **Security Awareness**: Demonstrate IP tracking and geolocation concepts

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/your-username/ip-rotator.git
cd ip-rotator

# Make scripts executable
chmod +x ip-rotator ip_rotator.py

# Run setup wizard
./ip-rotator --setup
```

### Basic Usage
```bash
# Check current IP
./ip-rotator --check-ip

# Start rotation with 10-second intervals
./ip-rotator --interval 10

# Use custom configuration
./ip-rotator --config custom-vpns.json --verbose

# Get help
./ip-rotator --help
```

## 📋 Requirements

### System Requirements
- **OS**: Linux, macOS, or Windows with WSL
- **Python**: 3.6 or higher
- **Privileges**: sudo access for VPN operations
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB free space

### Dependencies
- `python3` - Core runtime
- `openvpn` - VPN client software
- `curl` - HTTP requests for IP checking
- `sudo` - Administrative privileges

### Optional Enhancements
```bash
pip3 install -r requirements.txt
```

## 🔧 Configuration

### VPN Setup
1. **Get VPN configurations** from your provider
2. **Run setup wizard**: `./ip-rotator --setup`
3. **Edit config file**: `config.json`

### Sample Configuration
```json
{
  "vpn_configs": [
    {
      "name": "US-East-1",
      "type": "openvpn",
      "config_file": "/home/user/vpn-configs/us-east-1.ovpn",
      "enabled": true
    },
    {
      "name": "EU-West-1",
      "type": "openvpn",
      "config_file": "/home/user/vpn-configs/eu-west-1.ovpn",
      "enabled": true
    }
  ],
  "proxy_configs": [
    {
      "name": "tor-proxy",
      "type": "socks5",
      "host": "127.0.0.1",
      "port": 9050,
      "enabled": false
    }
  ],
  "rotation_method": "vpn",
  "check_ip_url": "https://httpbin.org/ip"
}
```

## 📚 Usage Examples

### Command Line Options
```bash
# Basic rotation every 5 seconds
./ip-rotator --interval 5

# Verbose logging with custom config
./ip-rotator --interval 30 --config production.json --verbose

# Just check current IP and location
./ip-rotator --check-ip

# Stop all VPN connections
./ip-rotator --stop
```

### Python API Usage
```python
from ip_rotator import IPRotator

# Initialize rotator
rotator = IPRotator(interval=10, config_file='config.json')

# Check current IP
current_ip = rotator.get_current_ip()
print(f"Current IP: {current_ip}")

# Start rotation (blocking)
rotator.run()
```

### Advanced Configuration
```bash
# Run with systemd service
sudo systemctl enable ip-rotator
sudo systemctl start ip-rotator

# Use with cron for scheduled rotation
*/5 * * * * /path/to/ip-rotator --interval 60 >> /var/log/ip-rotator-cron.log 2>&1
```

## 🛡️ Security Features

### Operational Security
- **No credential storage**: Secure credential handling via separate auth files
- **Minimal privileges**: Requests sudo only when needed for VPN operations  
- **Encrypted connections**: All VPN connections use strong encryption
- **DNS leak protection**: Automatic DNS configuration management
- **Clean disconnect**: Graceful VPN cleanup on exit

### Monitoring & Logging
- **Real-time IP verification**: Confirms successful IP changes
- **Comprehensive logs**: Detailed logging to `ip_rotator.log`
- **Error tracking**: Failed rotation attempts and recovery actions
- **Connection audit**: VPN connection/disconnection events

### Privacy Protection
- **No data retention**: No personal information stored locally
- **Secure file permissions**: Configuration files secured with 600 permissions
- **Memory safety**: Credentials cleared from memory after use

## 🚨 Legal Disclaimer

⚠️ **IMPORTANT: READ CAREFULLY BEFORE USE** ⚠️

This tool is provided for **educational and authorized security testing purposes only**. Users must ensure compliance with all applicable laws and regulations.

### Acceptable Use
✅ **ALLOWED:**
- Authorized penetration testing with written permission
- Personal privacy protection on your own systems
- Academic research and cybersecurity education
- Security testing of systems you own or have explicit permission to test
- Bug bounty programs where IP rotation is permitted

❌ **PROHIBITED:**
- Unauthorized access to systems or networks
- Circumventing geographic restrictions for illegal purposes
- Any activity that violates terms of service or laws
- Malicious hacking or cyberattacks
- Copyright infringement or piracy
- Fraud, identity theft, or other criminal activities

### Legal Responsibilities
- **User Responsibility**: Users are solely responsible for compliance with applicable laws
- **No Warranty**: This software is provided "as-is" without warranties
- **Indemnification**: Users agree to indemnify developers against any legal issues
- **Jurisdiction**: Subject to laws of your jurisdiction and target systems' jurisdiction

### Ethical Guidelines
- Always obtain proper authorization before testing systems
- Respect rate limits and avoid system disruption
- Report security vulnerabilities through responsible disclosure
- Use minimal access necessary for legitimate purposes
- Document and justify all security testing activities

## 🔍 Troubleshooting

### Common Issues

#### VPN Connection Failures
```bash
# Test VPN config manually
sudo openvpn --config /path/to/server.ovpn

# Check OpenVPN service status
systemctl status openvpn

# View detailed logs
tail -f /var/log/openvpn.log
```

#### IP Not Changing
```bash
# Verify VPN configurations
./ip-rotator --check-ip --verbose

# Test internet connectivity
curl https://httpbin.org/ip

# Check DNS settings
cat /etc/resolv.conf
```

#### Permission Errors
```bash
# Verify sudo access
sudo -v

# Check script permissions
ls -la ip-rotator ip_rotator.py

# Fix permissions
chmod +x ip-rotator ip_rotator.py
```

#### Python Errors
```bash
# Check Python version
python3 --version

# Install missing modules
pip3 install -r requirements.txt

# Test Python script directly
python3 ip_rotator.py --check-ip --verbose
```

### Debug Mode
Enable verbose logging for detailed troubleshooting:
```bash
./ip-rotator --verbose --interval 30
```

### Log Analysis
```bash
# View recent logs
tail -f ip_rotator.log

# Search for errors
grep -i error ip_rotator.log

# Monitor in real-time
watch -n 1 "tail -n 20 ip_rotator.log"
```

## 🤝 Contributing

We welcome contributions from the cybersecurity community!

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/your-username/ip-rotator.git
cd ip-rotator

# Create development environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Format code
black ip_rotator.py
flake8 ip_rotator.py
```

### Contribution Guidelines
- Follow Python PEP 8 style guidelines
- Add tests for new functionality
- Update documentation for changes
- Ensure security best practices
- Test on multiple platforms

## 📊 Project Statistics

- **Language**: Python 3.6+
- **Architecture**: Modular design with CLI interface
- **Platform Support**: Linux, macOS, Windows (WSL)
- **Dependencies**: Minimal (uses system tools)
- **Security**: Multiple layers of protection

## 🔗 Related Projects

- **OpenVPN**: Open-source VPN software
- **Tor**: Anonymous communication network
- **ProxyChains**: Proxy chain tool
- **Nmap**: Network discovery and security auditing
- **Metasploit**: Penetration testing framework

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 IP Rotator Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## 🙏 Acknowledgments

- OpenVPN community for excellent VPN software
- Security researchers who inspired this project
- VPN providers who enable privacy protection
- Open-source cybersecurity community

## 📞 Support

- **Documentation**: [Installation Guide](INSTALL.md)
- **Issues**: [GitHub Issues](https://github.com/your-username/ip-rotator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/ip-rotator/discussions)
- **Security**: Report security issues privately via email

---

**⚠️ Remember: With great power comes great responsibility. Use this tool ethically and legally! ⚠️**