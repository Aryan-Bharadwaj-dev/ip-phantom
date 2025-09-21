#!/usr/bin/env python3
"""
IP Rotator - Cybersecurity Tool for Automated IP Address Changing
This tool rotates IP addresses at specified intervals using VPN/proxy services.
For educational and legitimate security testing purposes only.
"""

import time
import sys
import signal
import logging
import argparse
import subprocess
import json
import random
from typing import Optional, Dict, List
from datetime import datetime


class SafeStreamHandler(logging.StreamHandler):
    """Stream handler that gracefully handles broken pipe errors."""
    
    def emit(self, record):
        try:
            super().emit(record)
            self.flush()
        except (BrokenPipeError, ConnectionResetError):
            # Silently ignore broken pipe errors
            pass
        except Exception:
            # Let other exceptions bubble up
            self.handleError(record)


def safe_print(*args, **kwargs):
    """Print function that gracefully handles broken pipe errors."""
    try:
        print(*args, **kwargs)
        sys.stdout.flush()
    except (BrokenPipeError, ConnectionResetError):
        # Silently ignore broken pipe errors
        pass


class IPRotator:
    """Main class for handling IP rotation functionality."""
    
    def __init__(self, interval: int = 3, config_file: str = "config.json", demo_mode: bool = False):
        self.interval = interval
        self.config_file = config_file
        self.running = True
        self.current_ip = None
        self.vpn_configs = []
        self.demo_mode = demo_mode
        self.demo_ips = ["192.168.1.100", "203.0.113.45", "198.51.100.78", "203.0.113.92", "192.0.2.146"]
        self.demo_counter = 0
        self.shutting_down = False
        self.setup_logging()
        self.load_configuration()
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def setup_logging(self):
        """Setup logging configuration."""
        # Create a custom formatter for clean output
        formatter = logging.Formatter('%(message)s')
        
        # File handler with detailed logs
        file_handler = logging.FileHandler('ip_rotator.log')
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        
        # Console handler with clean output - wrapped to handle broken pipes
        console_handler = SafeStreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        
        # Configure logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        # Suppress other loggers
        logging.getLogger().setLevel(logging.WARNING)
    
    def load_configuration(self):
        """Load VPN/proxy configurations from config file."""
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.vpn_configs = config.get('vpn_configs', [])
                self.proxy_configs = config.get('proxy_configs', [])
                self.logger.info(f"Loaded {len(self.vpn_configs)} VPN configs and {len(self.proxy_configs)} proxy configs")
        except FileNotFoundError:
            self.logger.warning(f"Config file {self.config_file} not found. Using default settings.")
            self.create_default_config()
        except json.JSONDecodeError as e:
            self.logger.error(f"Error parsing config file: {e}")
            sys.exit(1)
    
    def create_default_config(self):
        """Create a default configuration file."""
        default_config = {
            "vpn_configs": [
                {
                    "name": "openvpn_server1",
                    "type": "openvpn",
                    "config_file": "/path/to/server1.ovpn",
                    "enabled": True
                },
                {
                    "name": "openvpn_server2", 
                    "type": "openvpn",
                    "config_file": "/path/to/server2.ovpn",
                    "enabled": True
                }
            ],
            "proxy_configs": [
                {
                    "name": "socks_proxy1",
                    "type": "socks5",
                    "host": "127.0.0.1",
                    "port": 9050,
                    "enabled": True
                }
            ],
            "rotation_method": "vpn",  # "vpn", "proxy", or "mixed"
            "check_ip_url": "https://httpbin.org/ip"
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(default_config, f, indent=4)
        self.logger.info(f"Created default config file: {self.config_file}")
    
    def get_current_ip(self) -> Optional[str]:
        """Get current external IP address."""
        if self.demo_mode:
            # Return simulated IP for demo purposes
            return self.demo_ips[self.demo_counter % len(self.demo_ips)]
        
        try:
            # Using multiple IP check services for reliability
            ip_services = [
                "https://httpbin.org/ip",
                "https://api.ipify.org?format=json",
                "https://jsonip.com"
            ]
            
            for service in ip_services:
                try:
                    result = subprocess.run([
                        'curl', '-s', '--connect-timeout', '10', service
                    ], capture_output=True, text=True, timeout=15, stderr=subprocess.DEVNULL)
                    
                    if result.returncode == 0:
                        response = json.loads(result.stdout)
                        # Handle different response formats
                        ip = response.get('origin') or response.get('ip')
                        if ip:
                            # Clean IP (remove port if present)
                            ip = ip.split(',')[0].strip()
                            return ip
                except (subprocess.TimeoutExpired, json.JSONDecodeError, KeyError, BrokenPipeError):
                    continue
            
            self.logger.error("Failed to get current IP from all services")
            return None
            
        except (BrokenPipeError, ConnectionResetError):
            # Silently ignore broken pipe errors
            return None
        except Exception as e:
            if "BrokenPipeError" not in str(e):
                self.logger.error(f"Error getting current IP: {e}")
            return None
    
    def disconnect_current_vpn(self):
        """Disconnect current VPN connection."""
        if self.demo_mode:
            return  # No actual VPN to disconnect in demo mode
            
        try:
            # Kill existing OpenVPN processes
            subprocess.run(['sudo', 'pkill', '-f', 'openvpn'], 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
            
            # Reset DNS settings
            subprocess.run(['sudo', 'systemctl', 'restart', 'systemd-resolved'], 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
            
            time.sleep(2)  # Wait for disconnection
            if not self.shutting_down:
                self.logger.info("Disconnected from current VPN")
            
        except Exception as e:
            if not self.shutting_down:
                self.logger.error(f"Error disconnecting VPN: {e}")
    
    def connect_vpn(self, vpn_config: Dict) -> bool:
        """Connect to a VPN server."""
        try:
            config_file = vpn_config.get('config_file')
            if not config_file:
                self.logger.error(f"No config file specified for VPN: {vpn_config['name']}")
                return False
            
            # Disconnect current VPN first
            self.disconnect_current_vpn()
            
            # Connect to new VPN
            cmd = ['sudo', 'openvpn', '--config', config_file, '--daemon']
            result = subprocess.run(cmd, capture_output=True, text=True, stderr=subprocess.DEVNULL)
            
            if result.returncode == 0:
                self.logger.info(f"Connected to VPN: {vpn_config['name']}")
                time.sleep(5)  # Wait for connection to establish
                return True
            else:
                # Only log actual errors, not normal termination messages
                if result.stderr and "BrokenPipeError" not in str(result.stderr):
                    self.logger.error(f"Failed to connect to VPN {vpn_config['name']}: {result.stderr}")
                else:
                    self.logger.error(f"Failed to connect to VPN {vpn_config['name']}")
                return False
                
        except (BrokenPipeError, ConnectionResetError):
            # Silently ignore broken pipe errors - these are expected during VPN switching
            pass
        except Exception as e:
            if "BrokenPipeError" not in str(e):
                self.logger.error(f"Error connecting to VPN {vpn_config['name']}: {e}")
            return False
    
    def set_proxy(self, proxy_config: Dict) -> bool:
        """Configure system to use proxy."""
        try:
            host = proxy_config.get('host', '127.0.0.1')
            port = proxy_config.get('port', 9050)
            proxy_type = proxy_config.get('type', 'socks5')
            
            # Set proxy environment variables
            proxy_url = f"{proxy_type}://{host}:{port}"
            
            import os
            os.environ['http_proxy'] = proxy_url
            os.environ['https_proxy'] = proxy_url
            os.environ['HTTP_PROXY'] = proxy_url
            os.environ['HTTPS_PROXY'] = proxy_url
            
            self.logger.info(f"Set proxy: {proxy_config['name']} ({proxy_url})")
            return True
            
        except Exception as e:
            self.logger.error(f"Error setting proxy {proxy_config['name']}: {e}")
            return False
    
    def rotate_ip(self) -> bool:
        """Rotate to a new IP address."""
        try:
            if self.demo_mode:
                # Demo mode: simulate successful IP rotation
                old_ip = self.get_current_ip()
                
                # Simulate rotation delay
                time.sleep(1)
                self.demo_counter += 1
                
                new_ip = self.get_current_ip()
                self.current_ip = new_ip
                safe_print(f"🔄 Rotating IP: {old_ip} → {new_ip}")
                return True
            
            # Check for valid VPN configurations
            available_configs = [cfg for cfg in self.vpn_configs if cfg.get('enabled', True)]
            
            # Filter for configs with existing files
            valid_configs = []
            for cfg in available_configs:
                config_file = cfg.get('config_file')
                if config_file and config_file != "/path/to/server1.ovpn" and config_file != "/path/to/server2.ovpn":
                    import os
                    if os.path.exists(config_file):
                        valid_configs.append(cfg)
            
            if not valid_configs:
                self.logger.warning("No valid VPN configuration files found. Use --demo for demonstration mode.")
                return False
            
            # Select random VPN configuration
            selected_config = random.choice(valid_configs)
            
            self.logger.info(f"Attempting to rotate IP using: {selected_config['name']}")
            
            # Get current IP before rotation
            old_ip = self.get_current_ip()
            self.logger.info(f"Current IP: {old_ip}")
            
            # Connect to new VPN
            if self.connect_vpn(selected_config):
                # Verify IP change
                time.sleep(3)
                new_ip = self.get_current_ip()
                
                if new_ip and new_ip != old_ip:
                    self.current_ip = new_ip
                    self.logger.info(f"✓ IP successfully rotated: {old_ip} → {new_ip}")
                    return True
                else:
                    self.logger.warning(f"IP rotation may have failed. New IP: {new_ip}")
                    return False
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error during IP rotation: {e}")
            return False
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully."""
        if self.shutting_down:
            return  # Already shutting down
            
        self.shutting_down = True
        self.running = False
        
        try:
            safe_print("\n🛑 Shutting down gracefully...")
            
            # Cleanup: disconnect VPN only if not in demo mode
            if not self.demo_mode:
                try:
                    self.disconnect_current_vpn()
                except Exception:
                    pass  # Silent cleanup
            
            safe_print("✅ IP Rotator stopped safely.")
        except (BrokenPipeError, ConnectionResetError):
            # Silently ignore broken pipe errors during shutdown
            pass
        sys.exit(0)
    
    def run(self):
        """Main execution loop."""
        if self.demo_mode:
            safe_print(f"🚀 Starting IP Rotator Demo (rotating every {self.interval}s)")
        else:
            safe_print(f"🚀 Starting IP Rotator with {self.interval}s interval")
        safe_print("Press Ctrl+C to stop")
        safe_print()
        
        # Get initial IP
        initial_ip = self.get_current_ip()
        if initial_ip:
            safe_print(f"📍 Initial IP: {initial_ip}")
            self.current_ip = initial_ip
        
        rotation_count = 0
        
        try:
            while self.running:
                # Perform IP rotation
                if self.rotate_ip():
                    rotation_count += 1
                    if self.demo_mode:
                        safe_print(f"✅ Rotation #{rotation_count} complete")
                else:
                    safe_print("⚠️  Rotation failed, retrying...")
                
                # Wait for specified interval with countdown
                if self.running:
                    safe_print(f"⏳ Waiting {self.interval} seconds...")
                    for i in range(self.interval):
                        if not self.running:
                            break
                        try:
                            time.sleep(1)
                        except KeyboardInterrupt:
                            raise  # Re-raise to be caught by outer handler
                    if self.running:  # Only print if we haven't been interrupted
                        safe_print()
                    
        except KeyboardInterrupt:
            self.signal_handler(signal.SIGINT, None)
        except Exception as e:
            safe_print(f"❌ Unexpected error: {e}")
            sys.exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="IP Rotator - Automated IP Address Changer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 ip_rotator.py --interval 10    # Rotate every 10 seconds
  python3 ip_rotator.py --config my_vpns.json  # Use custom config
  python3 ip_rotator.py --check-ip       # Just check current IP
        """
    )
    
    parser.add_argument(
        '--interval', '-i',
        type=int,
        default=3,
        help='Time interval between IP rotations in seconds (default: 3)'
    )
    
    parser.add_argument(
        '--config', '-c',
        type=str,
        default='config.json',
        help='Configuration file path (default: config.json)'
    )
    
    parser.add_argument(
        '--check-ip',
        action='store_true',
        help='Check current IP address and exit'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run in demo mode with simulated IP changes (for demonstrations)'
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Just check IP and exit
    if args.check_ip:
        rotator = IPRotator(interval=args.interval, config_file=args.config, demo_mode=args.demo)
        current_ip = rotator.get_current_ip()
        if current_ip:
            if args.demo:
                safe_print(f"📍 Demo IP: {current_ip}")
            else:
                safe_print(f"📍 Current IP: {current_ip}")
        else:
            safe_print("❌ Failed to get current IP")
            sys.exit(1)
        return
    
    # Validate interval
    if args.interval < 1:
        safe_print("Error: Interval must be at least 1 second")
        sys.exit(1)
    
    # Start IP rotator
    rotator = IPRotator(interval=args.interval, config_file=args.config, demo_mode=args.demo)
    if args.demo:
        safe_print("\n🔍 DEMO MODE - Simulated IP rotation for demonstration")
        safe_print("Perfect for showcasing cybersecurity tool functionality\n")
    rotator.run()


if __name__ == "__main__":
    main()