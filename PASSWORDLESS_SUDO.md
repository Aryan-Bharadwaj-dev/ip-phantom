# Passwordless Sudo Setup for IP Rotator

## Overview

By default, when you shut down IP Rotator (Ctrl+C), it needs to run privileged commands to clean up VPN connections and reset DNS settings. This requires entering your password, which can be inconvenient and prevents truly clean shutdown.

The passwordless sudo setup allows specific VPN-related commands to run without password prompts while maintaining system security.

## Quick Setup

The easiest way to set this up:

```bash
# From the IP Rotator directory
./ip-rotator --setup-passwordless

# Or run the script directly
./setup-passwordless-sudo.sh --install
```

## What Gets Configured

The setup creates a sudoers file at `/etc/sudoers.d/ip-rotator` that allows your user to run these specific commands without a password:

1. **VPN Process Cleanup**: `sudo pkill -f openvpn`
2. **DNS Reset**: `sudo systemctl restart systemd-resolved` 
3. **OpenVPN Connection**: `sudo openvpn --config <file>`

## Benefits

✅ **Clean Shutdown**: Ctrl+C works instantly without password prompts
✅ **Secure**: Only specific VPN commands are passwordless
✅ **User Friendly**: No interruption during demonstrations or testing
✅ **Professional**: Smooth operation for cybersecurity presentations

## Security Considerations

This configuration is secure because:

- **Limited Scope**: Only allows specific VPN-related commands
- **User Specific**: Only applies to your user account
- **Command Specific**: Other sudo operations still require password
- **Standard Practice**: Common in VPN and networking tools

## Usage Examples

### Before Setup (with password prompts)
```bash
./ip-rotator --interval 10
# ... running ...
# Press Ctrl+C
[sudo] password for user: ▌  # Password prompt during shutdown
```

### After Setup (clean shutdown)
```bash
./ip-rotator --interval 10
# ... running ...
# Press Ctrl+C
🛑 Shutting down gracefully...
✅ IP Rotator stopped safely.
```

## Management Commands

### Check Status
```bash
./setup-passwordless-sudo.sh --status
```

### Remove Configuration
```bash
./setup-passwordless-sudo.sh --uninstall
```

### Reinstall/Update
```bash
./setup-passwordless-sudo.sh --install
```

## Troubleshooting

### Configuration Not Working

1. **Check if file exists**:
   ```bash
   ls -la /etc/sudoers.d/ip-rotator
   ```

2. **Verify syntax**:
   ```bash
   sudo visudo -cf /etc/sudoers.d/ip-rotator
   ```

3. **Test manually**:
   ```bash
   sudo -n pkill -f openvpn
   # Should not prompt for password
   ```

### Manual Configuration

If the automated setup doesn't work, you can manually create the configuration:

1. **Edit sudoers file**:
   ```bash
   sudo visudo -f /etc/sudoers.d/ip-rotator
   ```

2. **Add these lines** (replace `yourusername` with your actual username):
   ```
   # IP Rotator - Passwordless sudo configuration
   yourusername ALL=(ALL) NOPASSWD: /usr/bin/pkill -f openvpn, /bin/pkill -f openvpn
   yourusername ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart systemd-resolved, /bin/systemctl restart systemd-resolved
   yourusername ALL=(ALL) NOPASSWD: /usr/sbin/openvpn --config *, /usr/bin/openvpn --config *
   ```

3. **Set proper permissions**:
   ```bash
   sudo chmod 440 /etc/sudoers.d/ip-rotator
   ```

## Alternative Solutions

If you prefer not to use passwordless sudo:

### Option 1: Use Demo Mode
```bash
./ip-rotator --demo --interval 10
# Demo mode doesn't require VPN cleanup, so no password prompts
```

### Option 2: Pre-authenticate
```bash
sudo -v  # Enter password once
./ip-rotator --interval 10  # Will use cached authentication
```

### Option 3: Accept Password Prompts
The tool will work normally, just with password prompts during shutdown.

## Integration with CI/CD

For automated testing environments, the passwordless sudo setup is especially useful:

```bash
# In your CI/CD pipeline
./setup-passwordless-sudo.sh --install
./ip-rotator --demo --interval 5 &
# ... run tests ...
killall ip-rotator  # Clean shutdown without password prompts
```

This ensures your automated tests don't hang waiting for password input.