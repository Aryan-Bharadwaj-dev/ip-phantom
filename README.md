# IP Rotator - Cybersecurity Tool

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security: Educational](https://img.shields.io/badge/Use-Educational%20Only-red.svg)](https://github.com/your-repo/ip-rotator)

A powerful cybersecurity tool for automated IP address rotation using VPN connections. Designed for penetration testing, security research, and privacy protection purposes.

## 🎆 **New in v2.0!** 

✨ **Professional-grade improvements:**
- 🎯 **Demo Mode** - Zero-config simulated IP rotation for presentations
- 🎨 **Beautiful Interface** - Clean, emoji-enhanced CLI output
- 🌍 **Global Installation** - Run from anywhere without `./`
- ❓ **Gorgeous Help System** - Comprehensive, beautifully formatted help
- ⚡ **Instant Response** - Professional Ctrl+C handling
- 🛡️ **Zero Errors** - Clean output with no broken pipe messages

```bash
# 🚀 One-command installation
./install.sh

# 🎯 Now works globally!
ip-rotator --demo --interval 5

# 🎨 Beautiful help system
ip-rotator --help
```

## 🔥 Features

- **🔄 Automated IP Rotation**: Changes IP address at configurable intervals (default: 3 seconds)
- **🔗 VPN Integration**: Supports OpenVPN configurations from major providers
- **🔀 Multiple Protocols**: VPN and proxy support with failover mechanisms
- **📍 Real-time Monitoring**: Live IP verification and change tracking with beautiful visual indicators
- **🛡️ Robust Error Handling**: Graceful failure recovery and professional error management
- **📊 Comprehensive Logging**: Detailed logs for security auditing with clean console output
- **💻 Cross-platform**: Linux, macOS, and Windows (WSL) support
- **🎯 Demo Mode**: Perfect for demonstrations and testing without actual VPN connections
- **⚡ Instant Response**: Responsive Ctrl+C handling and graceful shutdown
- **🎨 Beautiful Interface**: Clean, professional CLI with emojis and color-coded output
- **🔧 Zero-Config Demo**: Works out-of-the-box with simulated IP rotation

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

### Installation

#### Option 1: Quick Global Installation (Recommended)
```bash
# Clone the repository
git clone https://github.com/your-username/ip-rotator.git
cd ip-rotator

# Make scripts executable
chmod +x ip-rotator ip_rotator.py

# 🚀 Install globally (one command!)
./install.sh

# Now run from anywhere without ./
ip-rotator --demo --interval 5
```

#### Option 2: Local Installation
```bash
# Clone the repository
git clone https://github.com/your-username/ip-rotator.git
cd ip-rotator

# Make scripts executable
chmod +x ip-rotator ip_rotator.py

# Run setup wizard (optional for real VPN usage)
./ip-rotator --setup
```

### Basic Usage

#### 🌍 Global Usage (After running ./install.sh)
```bash
# 🎯 Demo mode - Perfect for testing and demonstrations!
ip-rotator --demo --interval 5

# Check current IP
ip-rotator --check-ip

# Check simulated IP in demo mode
ip-rotator --demo --check-ip

# Start rotation with 10-second intervals
ip-rotator --interval 10

# Use custom configuration with verbose output
ip-rotator --config custom-vpns.json --verbose

# 🎯 Get beautiful comprehensive help
ip-rotator --help
```

#### 📁 Local Usage (Traditional)
```bash
# All the same commands but with ./
./ip-rotator --demo --interval 5
./ip-rotator --check-ip
./ip-rotator --help
```

## 🎯 Demo Mode (New!)

Perfect for demonstrations, testing, and showcasing the tool:

```bash
# Quick demo with 3-second intervals (global)
ip-rotator --demo --interval 3

# Check simulated IP in demo mode
ip-rotator --demo --check-ip

# Verbose demo for detailed output
ip-rotator --demo --interval 5 --verbose

# Or use local version
./ip-rotator --demo --interval 3
```

**Example Demo Output:**
```
🚀 Starting IP Rotator Demo (rotating every 3s)
Press Ctrl+C to stop

📍 Initial IP: 192.168.1.100
🔄 Rotating IP: 192.168.1.100 → 203.0.113.45
✅ Rotation #1 complete
⏳ Waiting 3 seconds...

🔄 Rotating IP: 203.0.113.45 → 198.51.100.78
✅ Rotation #2 complete
⏳ Waiting 3 seconds...

🛑 Shutting down gracefully...
✅ IP Rotator stopped safely.
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

### 🎯 Beautiful Help System

Get comprehensive help with gorgeous formatting:

```bash
# Beautiful, comprehensive help page
ip-rotator --help
# or
./ip-rotator --help
```

**Features gorgeous help with:**
- 🎨 Emoji-enhanced formatting
- 📚 Complete command documentation
- 🎯 Demo mode benefits and features
- 📋 System requirements breakdown
- ✨ Quick start examples
- 🔍 Troubleshooting guide
- 🚀 Installation tips

**Example Help Output:**
```
==================================================================
                    🎯 IP ROTATOR HELP GUIDE
==================================================================

IP Rotator - Professional Cybersecurity IP Rotation Tool

📋 USAGE:
  ip-rotator [OPTIONS]

⚙️  CORE OPTIONS:
  -i, --interval SECONDS    ⏱️  Time interval between rotations (default: 3)
  --demo                   🎯 Run in demo mode (simulated IP changes)
  -h, --help               ❓ Show comprehensive help message

✨ QUICK START EXAMPLES:
  # 🎯 Demo Mode - Perfect for presentations!
  ip-rotator --demo --interval 5

🎯 DEMO MODE FEATURES:
  ✅ Zero dependencies - no VPN setup required
  ✅ Perfect for cybersecurity demonstrations
  ✅ Professional visual output with emojis
  ✅ Instant Ctrl+C response for clean shutdown
==================================================================
```

### Complete CLI Reference
```bash
Options:
  -i, --interval SECONDS    ⏱️  Time interval between rotations (default: 3)
  -c, --config FILE         📁 Configuration file path (default: config.json)
  -v, --verbose             📊 Enable verbose logging
  -h, --help               ❓ Show comprehensive help message
  --check-ip               📍 Check current IP address and exit
  --setup                  🛠️  Run initial setup wizard
  --stop                   🛑 Stop all running VPN connections
  --demo                   🎯 Run in demo mode (simulated IP changes)
```

### Command Line Examples

#### 🌍 Global Commands (After Installation)
```bash
# Basic rotation every 5 seconds
ip-rotator --interval 5

# Verbose logging with custom config
ip-rotator --interval 30 --config production.json --verbose

# Just check current IP and location
ip-rotator --check-ip

# Stop all VPN connections
ip-rotator --stop

# Beautiful help system
ip-rotator --help
```

#### 📁 Local Commands (Traditional)
```bash
# All commands work with ./
./ip-rotator --interval 5
./ip-rotator --help
./ip-rotator --demo --interval 3
```

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
- **Comprehensive logs**: Detailed logging to `ip_rotator.log` with clean console output
- **Error tracking**: Failed rotation attempts and recovery actions
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
  "rotation_method": "vpn",
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
- Bug bounty programs where IP rotation is permitted
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
ip-rotator --demo --interval 5    # Works anywhere!

# 📁 Local (still supported)
./ip-rotator --demo --interval 5  # Works in project directory
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
