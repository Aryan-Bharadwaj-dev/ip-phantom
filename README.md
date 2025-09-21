# 👻 IP Phantom - Anonymous IP Address Changer

[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Tor Network](https://img.shields.io/badge/Tor-Network-purple.svg)](https://www.torproject.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-macOS%20|%20Linux%20|%20Windows-lightgrey.svg)]()

> **👻 A professional cybersecurity tool that makes your real IP vanish and reappear with a new anonymous identity using the Tor network - completely FREE!**

## 🎆 **New in v3.0 - IP Phantom!**

✨ **Revolutionary FREE IP Rotation:**
- 🆓 **100% Free** - No VPN subscriptions required!
- 🌐 **Tor Integration** - Real IP changing using Tor network
- 👻 **Phantom Mode** - Your real IP vanishes, new anonymous identity appears
- 🎯 **Demo Mode** - Still available for presentations
- 🛡️ **Anonymous Browsing** - Routes traffic through Tor network
- ⚡ **Easy Setup** - Tor installed and configured automatically
- 🔧 **Zero Cost** - Completely free alternative to paid VPNs

```bash
# 🆓 FREE real IP changing with Tor
python3 ip_phantom.py --interval 5

# 🎯 Demo mode for presentations
python3 ip_phantom.py --demo --interval 3

# 📍 Check your current IP
python3 ip_phantom.py --check-ip
```

**Example Real Output:**
```
👻 Starting IP Phantom with Tor (changing IP every 5s)
🌐 Using Tor network for anonymous IP changing

📍 Connected to United States (New York) server
📍 Current IP: 185.220.101.32
🔄 Changing IP address...
✓ Connected to Germany (Frankfurt) server
👻 IP changed: 185.220.101.32 → 146.70.173.85
✅ Identity change #1 complete
⏳ Waiting 5 seconds...
```

## 🌟 Features

- **🆓 100% Free** - No VPN subscriptions required
- **👻 Real IP Changing** - Actually changes your IP address using Tor
- **🎯 Demo Mode** - Perfect for presentations and demonstrations
- **🔒 Anonymous Browsing** - Routes traffic through Tor network
- **⚡ Easy to Use** - One command to start rotating IPs
- **🛡️ Security Focused** - Built with cybersecurity best practices
- **🎨 Professional UI** - Clean terminal output with emojis
- **⏱️ Customizable Intervals** - Set IP changing frequency (1-86400 seconds)
- **🔧 Cross-Platform** - Works on macOS, Linux, and Windows
- **🌐 Tor Integration** - Automatic Tor daemon management
- **👻 Circuit Renewal** - Forces new Tor circuits for fresh IPs
- **📍 IP Verification** - Real-time IP change confirmation
- **📈 Comprehensive Logging** - Detailed logs for security auditing
- **⚡ Instant Response** - Responsive Ctrl+C handling and graceful shutdown

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
- **Tool Demonstrations**: Perfect demo mode for showcasing capabilities

## 🚀 Quick Start

### Prerequisites
- **Python 3.6+** 🐍
- **Tor** (automatically installed)
- **curl** (for IP checking)

### Installation

#### Option 1: One-Click Setup
```bash
git clone https://github.com/yourusername/ip-phantom.git
cd ip-phantom
chmod +x install.sh
./install.sh
```

#### Option 2: Manual Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/ip-phantom.git
cd ip-phantom

# Install Tor (macOS)
brew install tor

# Install Tor (Ubuntu/Debian)
sudo apt update && sudo apt install tor

# Install Tor (CentOS/RHEL)
sudo yum install tor

# Make scripts executable
chmod +x ip-phantom ip_phantom.py
```

### Usage

#### 🎯 Demo Mode (No Dependencies)
Perfect for demonstrations and testing:
```bash
python3 ip_phantom.py --demo --interval 3
```

#### 🌐 Real IP Changing with Tor
```bash
# Start IP changing (default: every 3 seconds)
python3 ip_phantom.py

# Custom interval (10 seconds)
python3 ip_phantom.py --interval 10

# Check current IP
python3 ip_phantom.py --check-ip

# Verbose logging
python3 ip_phantom.py --verbose --interval 5
```

#### 🔧 CLI Wrapper (After Installation)
```bash
# Global usage (after running install.sh)
ip-phantom --demo
ip-phantom --interval 10
ip-phantom --check-ip
ip-phantom --help
```

## 🎯 Demo Mode Features

**Example Demo Output:**
```
🚀 Starting IP Phantom Demo (changing IP every 3s)
📍 Connected to United States (New York) server
📍 Current IP: 185.220.101.32

🔄 Changing IP address...
✓ Connected to Germany (Frankfurt) server
👻 IP changed: 185.220.101.32 → 146.70.173.85
✅ Identity change #1 complete
⏳ Waiting 3 seconds...

🔄 Changing IP address...
✓ Connected to United Kingdom (London) server
👻 IP changed: 146.70.173.85 → 51.89.153.122
✅ Identity change #2 complete

🛁 Shutting down gracefully...
✅ IP Phantom stopped safely.
```

## 📋 Requirements

### System Requirements
- **OS**: Linux, macOS, or Windows with WSL
- **Python**: 3.6 or higher
- **Privileges**: sudo access for VPN operations (not needed for demo mode)
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB free space

### Dependencies
- `python3` - Core runtime
- `openvpn` - VPN client software (not needed for demo mode)
- `curl` - HTTP requests for IP checking
- `sudo` - Administrative privileges (not needed for demo mode)

## 📚 Usage Examples

### 🎯 Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--interval N` | IP change interval in seconds (1-86400) | `--interval 10` |
| `--demo` | Demo mode with simulated IP changes | `--demo` |
| `--check-ip` | Check current IP and exit | `--check-ip` |
| `--verbose` | Enable detailed logging | `--verbose` |
| `--config FILE` | Custom configuration file | `--config my_config.json` |
| `--help` | Show help message | `--help` |


## 🛡️ Security Features

### 🔒 Operational Security
- **No credential storage**: Secure credential handling via separate auth files
- **Minimal privileges**: Requests sudo only when needed for VPN operations  
- **Encrypted connections**: All VPN connections use strong encryption
- **DNS leak protection**: Automatic DNS configuration management
- **Clean disconnect**: Graceful VPN cleanup on exit with zero error messages
- **Safe shutdown**: Professional error handling with no broken pipe errors

### 📊 Monitoring & Logging
- **Real-time IP verification**: Confirms successful IP changes with visual indicators
- **Comprehensive logs**: Detailed logging to `ip_phantom.log` with clean console output
- **Error tracking**: Failed connection attempts and recovery actions
- **Connection audit**: VPN connection/disconnection events
- **Professional output**: Clean, emoji-enhanced status messages

### 🔐 Privacy Protection
- **No data retention**: No personal information stored locally
- **Secure file permissions**: Configuration files secured with 600 permissions
- **Memory safety**: Credentials cleared from memory after use
- **Demo mode safety**: Test functionality without exposing real IP addresses

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
  "phantom_method": "tor",
  "check_ip_url": "https://httpbin.org/ip"
}
```

## 🚨 Legal Disclaimer

⚠️ **IMPORTANT: READ CAREFULLY BEFORE USE** ⚠️

This tool is provided for **educational and authorized security testing purposes only**. Users must ensure compliance with all applicable laws and regulations.

### Acceptable Use
✅ **ALLOWED:**
- Authorized penetration testing with written permission
- Personal privacy protection on your own systems
- Academic research and cybersecurity education
- Security testing of systems you own or have explicit permission to test
- Bug bounty programs where IP changing is permitted
- Demonstrations and training in controlled environments

❌ **PROHIBITED:**
- Unauthorized access to systems or networks
- Circumventing geographic restrictions for illegal purposes
- Any activity that violates terms of service or laws
- Malicious hacking or cyberattacks
- Copyright infringement or piracy
- Fraud, identity theft, or other criminal activities

## 🔍 Troubleshooting

### 🚀 Global Installation Benefits

#### One-Click Installation
```bash
./install.sh
```

**What it does:**
- ✅ Creates global symbolic links
- ✅ Sets proper permissions
- ✅ Verifies installation
- ✅ Shows usage examples
- ✅ Works from any directory

#### Usage Flexibility
```bash
# 🌍 Global (recommended)
ip-phantom --demo --interval 5    # Works anywhere!

# 📁 Local (still supported)
./ip-phantom --demo --interval 5  # Works in project directory
```

### Quick Debug with Demo Mode
```bash
# Test basic functionality without VPN dependencies
ip-rotator --demo --check-ip
# or
./ip-rotator --demo --check-ip

# Test rotation with verbose output
ip-rotator --demo --verbose --interval 5
```

### Common Issues

#### Permission Errors
```bash
# Fix script permissions
chmod +x ip-rotator ip_rotator.py

# Verify Python access
python3 --version
```

#### Python Errors
```bash
# Test in demo mode (no dependencies needed)
python3 ip_rotator.py --demo --check-ip

# Test Python script directly
python3 ip_rotator.py --check-ip --verbose
```

## 🤝 Contributing

We welcome contributions from the cybersecurity community!

### Contribution Guidelines
- Follow Python PEP 8 style guidelines
- Add tests for new functionality
- Update documentation for changes
- Ensure security best practices
- Test on multiple platforms
- Test both real VPN mode and demo mode

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenVPN community for excellent VPN software
- Security researchers who inspired this project
- VPN providers who enable privacy protection
- Open-source cybersecurity community

---

**⚠️ Remember: With great power comes great responsibility. Use this tool ethically and legally! ⚠️**
