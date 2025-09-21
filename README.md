# 👻 IP Phantom - Anonymous IP Address Changer

[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Tor Network](https://img.shields.io/badge/Tor-Network-purple.svg)](https://www.torproject.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-macOS%20|%20Linux%20|%20Windows-lightgrey.svg)]()

> **👻 A professional cybersecurity tool that makes your real IP vanish and reappear with a new anonymous identity using the Tor network - completely FREE!**

## 🌐 **IP Phantom - Tor-Based Anonymous IP Changing**

✨ **Real Anonymous IP Changing:**
- 🆓 **100% Free** - No VPN subscriptions or paid services required
- 🌐 **Tor Network** - Uses the Tor anonymity network for real IP changes
- 👻 **Automatic IP Rotation** - Changes your public IP address every specified interval
- 🛡️ **Anonymous Browsing** - Routes all traffic through Tor network
- ⚡ **Easy Setup** - Tor installed and configured automatically
- 🔧 **Zero Cost** - Completely free alternative to paid VPN services
- 🎯 **Demo Mode** - Available for testing and presentations

```bash
# 🆓 Real IP changing with Tor network (main feature)
ip-phantom --interval 10

# 📍 Check your current IP address
ip-phantom --check-ip

# 🎯 Demo mode (for testing/presentations)
ip-phantom --demo --interval 3
```

**Example Real Output:**
```
👻 Starting IP Phantom with Tor (changing IP every 10s)
🌐 Using Tor network for anonymous IP changing
Press Ctrl+C to stop

📍 Initial IP: 14.194.135.206
🔄 Changing IP address...
✓ Tor started successfully
👻 IP changed via Tor: 14.194.135.206 → 185.220.101.32
✅ Identity change #1 complete
⏳ Waiting 10 seconds...
```

## 🌟 Features

- **🌐 Real IP Changing** - Actually changes your public IP address using Tor network
- **🆓 100% Free** - No VPN subscriptions or paid services required
- **🛡️ Anonymous Browsing** - Routes all traffic through Tor for complete anonymity
- **⚡ Automatic Setup** - Tor installed and configured automatically
- **👻 Circuit Renewal** - Forces new Tor circuits for fresh IP addresses
- **📍 Real-time Verification** - Confirms successful IP changes immediately
- **⏱️ Customizable Intervals** - Set IP changing frequency (1-86400 seconds)
- **🔧 Cross-Platform** - Works on macOS, Linux, and Windows
- **📈 Security Logging** - Detailed logs for security auditing
- **⚡ Professional UI** - Clean terminal output with visual indicators
- **🔒 Security Focused** - Built with cybersecurity best practices
- **🎯 Demo Mode** - Available for testing and presentations
- **⚡ Graceful Shutdown** - Responsive Ctrl+C handling

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

#### Option 1: Automatic Installation (Recommended)
```bash
git clone https://github.com/yourusername/ip-phantom.git
cd ip-phantom
chmod +x install.sh
./install.sh
```
This will:
- Install Tor automatically if not present
- Set up global `ip-phantom` command
- Configure all necessary permissions

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

# Test the installation
./ip-phantom --check-ip
```

## ⚡ Quick Reference

### Most Common Commands
```bash
# Quick start - change IP every 10 seconds
ip-phantom --interval 10

# Check what your current IP is
ip-phantom --check-ip

# Test with demo mode (no actual IP changes)
ip-phantom --demo --interval 5

# Run with detailed output
ip-phantom --interval 15 --verbose

# Show all available options
ip-phantom --help
```

### Typical Workflow
1. **Install**: Run `./install.sh` once for global access
2. **Test**: Use `ip-phantom --demo --check-ip` to verify
3. **Real Use**: Run `ip-phantom --interval 10` for actual IP rotation
4. **Stop**: Press `Ctrl+C` to gracefully shutdown

### Usage

#### 🌐 Real IP Changing with Tor (Primary Feature)
```bash
# Start IP changing every 10 seconds
ip-phantom --interval 10

# Start with verbose logging
ip-phantom --interval 15 --verbose

# Check current IP address
ip-phantom --check-ip

# View all options
ip-phantom --help
```

#### 🔧 Direct Python Usage (Alternative)
```bash
# Using Python directly
python3 ip_phantom.py --interval 10
python3 ip_phantom.py --check-ip
python3 ip_phantom.py --verbose --interval 5
```

#### 🎯 Demo Mode (Testing Only)
For presentations and testing without real IP changes:
```bash
ip-phantom --demo --interval 3
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
- **Network**: Internet connection for Tor network (real mode only)
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB free space
- **Privileges**: Standard user privileges (no sudo required for demo mode)

### Dependencies
**For Real Mode (Tor):**
- `python3` - Core runtime (3.6+)
- `tor` - Tor network client (auto-installed if missing)
- `curl` - HTTP requests for IP checking
- Internet connection for Tor network access

**For Demo Mode:**
- `python3` - Core runtime (3.6+)
- `curl` - HTTP requests for IP checking (simulation)

## 📚 Usage Examples

### 🎯 Command Line Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--interval N` | `-i N` | IP change interval in seconds (1-86400) | `--interval 10` |
| `--config FILE` | `-c FILE` | Custom configuration file path | `--config my_config.json` |
| `--verbose` | `-v` | Enable detailed logging output | `--verbose` |
| `--check-ip` | | Check current IP address and exit | `--check-ip` |
| `--demo` | | Demo mode with simulated IP changes | `--demo` |
| `--help` | `-h` | Show comprehensive help message | `--help` |


## 🛡️ Security Features

### 🔒 Operational Security
- **No credential storage**: No personal information stored locally
- **Minimal privileges**: Standard user privileges, no sudo required for core functionality
- **Encrypted connections**: All traffic routed through Tor's encrypted network
- **DNS leak protection**: Automatic DNS routing through Tor network
- **Clean disconnect**: Graceful Tor circuit cleanup on exit
- **Safe shutdown**: Professional error handling with responsive Ctrl+C

### 📈 Monitoring & Logging
- **Real-time IP verification**: Confirms successful IP changes via Tor with visual indicators
- **Comprehensive logs**: Detailed logging to `ip_phantom.log` with clean console output
- **Error tracking**: Failed Tor circuit attempts and recovery actions
- **Circuit audit**: Tor circuit creation/renewal events
- **Professional output**: Clean, emoji-enhanced status messages with country detection

### 🔐 Privacy Protection
- **No data retention**: No personal information stored locally
- **Secure file permissions**: Configuration files secured with 600 permissions
- **Memory safety**: Credentials cleared from memory after use
- **Demo mode safety**: Test functionality without exposing real IP addresses

## 🌐 How Tor Integration Works

### Real Mode (Tor Network)
- **Automatic Tor Daemon**: Starts and manages Tor process automatically
- **Circuit Renewal**: Forces new Tor circuits to change IP addresses
- **SOCKS Proxy**: Routes traffic through Tor's SOCKS5 proxy (127.0.0.1:9050)
- **Control Port**: Uses Tor's control interface (9051) for circuit management
- **IP Verification**: Confirms IP changes via Tor-routed HTTP requests

### Demo Mode vs Real Mode
| Feature | Demo Mode | Real Mode (Tor) |
|---------|-----------|------------------|
| **IP Changes** | Simulated | Actually changes your public IP |
| **Network Traffic** | No routing changes | All traffic through Tor |
| **Dependencies** | Python + curl only | Python + Tor + curl |
| **Speed** | Instant simulation | ~3-5 seconds per change |
| **Use Case** | Presentations, testing | Real anonymity and privacy |

## 🔧 Configuration

### Tor Configuration
The tool automatically creates and manages Tor configuration. For advanced users:
1. **Edit Tor config**: `torrc` file in project directory
2. **Edit IP Phantom config**: `config.json`
3. **Custom intervals**: Use `--interval` option

### Sample Configuration

**config.json (IP Phantom Configuration):**
```json
{
  "vpn_configs": [],
  "proxy_configs": [
    {
      "name": "tor-proxy",
      "type": "socks5",
      "host": "127.0.0.1",
      "port": 9050,
      "enabled": true
    }
  ],
  "phantom_method": "tor",
  "check_ip_url": "https://httpbin.org/ip"
}
```

**torrc (Tor Network Configuration):**
```
# SOCKS proxy on port 9050
SocksPort 9050

# Control port for circuit management (IP rotation)
ControlPort 9051

# Allow connections from localhost only
SocksBindAddress 127.0.0.1

# Enable control port authentication
CookieAuthentication 1
CookieAuthFile /tmp/tor-control-cookie

# Circuit settings for better IP rotation
NewCircuitPeriod 60
MaxCircuitDirtiness 300

# Directory for Tor data
DataDirectory /tmp/tor-data
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
# Test basic functionality without dependencies
ip-phantom --demo --check-ip
# or
./ip-phantom --demo --check-ip

# Test IP changing with verbose output
ip-phantom --demo --verbose --interval 5
```

### Common Issues

#### Permission Errors
```bash
# Fix script permissions
chmod +x ip-phantom ip_phantom.py

# Verify Python access
python3 --version
```

#### Python Errors
```bash
# Test in demo mode (no dependencies needed)
python3 ip_phantom.py --demo --check-ip

# Test Python script directly
python3 ip_phantom.py --check-ip --verbose
```

## 🤝 Contributing

We welcome contributions from the cybersecurity community!

### Contribution Guidelines
- Follow Python PEP 8 style guidelines
- Add tests for new functionality
- Update documentation for changes
- Ensure security best practices
- Test on multiple platforms
- Test both real Tor mode and demo mode

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenVPN community for excellent VPN software
- Security researchers who inspired this project
- VPN providers who enable privacy protection
- Open-source cybersecurity community

---

**⚠️ Remember: With great power comes great responsibility. Use this tool ethically and legally! ⚠️**
